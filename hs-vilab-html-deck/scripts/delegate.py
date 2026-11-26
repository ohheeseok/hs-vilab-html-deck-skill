"""Hand one pass to another AI CLI on this machine and get its answer back as a file.

Usage:
    python delegate.py which                                   # which CLIs are here, per role
    python delegate.py text     --prompt-file brief.md  --dir <ref> --out outline.md
    python delegate.py review   --prompt-file critic.md --dir <ref> --out review/critic.md
    python delegate.py research --prompt-file questions.md          --out review/research.md
    python delegate.py vision   --prompt-file brief.md  --dir <bundle> --out review/visual.md

Roles and who fills them (ORDER): the draft, revision and Korean edit go to codex; critique,
verification, research and visual review go to agy. Each falls back to the other CLI, and when
neither is installed the script exits 3 and says so — the conductor then runs that role as a
subagent and names the fallback in the delivery report. A silent fallback is not allowed.

<dir> is the folder the delegate may read (paper.txt, paper.pdf, outline.md, captures, rules).
Both CLIs run read-only and are told to print, not to write files.

Two things that broke on the first full run and are handled here:
  * codex resolved a Google Drive path through its Drive connector and wandered; the prompt
    now names the folder as the only place to read, and codex gets it with --cd.
  * On Windows a command line holds ~32K characters; a brief with the paper inline does not
    fit agy's --print=. A long prompt is written into <dir> and agy is told to read it there.
And on the second paper (REPA): codex 0.170's read-only sandbox could not read a Google Drive
folder at all (the Korean edit came back "access denied", the revision could not open a figure).
codex now reads a copy of <dir> staged on the local temp disk; the copy is removed afterwards.

Models: HSDECK_CODEX_MODEL (default gpt-6.2-sol), HSDECK_AGY_MODEL (default gemini-4-neon-high).
"""
from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import tempfile
import sys
from pathlib import Path

ORDER = {"text": ["codex", "agy"], "review": ["agy", "codex"], "research": ["agy", "codex"],
         "vision": ["agy", "codex"]}
CODEX_MODEL = os.environ.get("HSDECK_CODEX_MODEL", "gpt-6.2-sol")
AGY_MODEL = os.environ.get("HSDECK_AGY_MODEL", "gemini-4-neon-high")
INLINE_MAX = 20000
RULE = ("\n\n(규칙: 아래 폴더 밖의 파일·커넥터·웹을 쓰지 마라. 파일을 만들거나 고치지 말고 결과만 출력하라. "
        "읽을 폴더: {dir})")
RULE_WEB = "\n\n(규칙: 파일을 만들거나 고치지 마라. 답마다 출처 URL을 붙여라.)"
# research needs the web: a folder given to it is extra reading, never a fence (RAE run: --dir made
# the researcher refuse every web question and answer "확인 못 함" five times)
RULE_WEB_DIR = ("\n\n(규칙: 웹을 검색하라. 아래 폴더의 파일도 읽어도 된다. 파일을 만들거나 고치지 말고 "
                "결과만 출력하라. 답마다 출처 URL을 붙여라. 읽을 폴더: {dir})")


def find(cmd: str) -> str | None:
    return shutil.which(cmd) or shutil.which(cmd + ".cmd") or shutil.which(cmd + ".exe")


def pick(role: str) -> str | None:
    return next((c for c in ORDER[role] if find(c)), None)


def run_codex(prompt: str, folder: Path | None, out: Path, timeout: int) -> int:
    cmd = [find("codex"), "exec", "--skip-git-repo-check", "-s", "read-only", "-m", CODEX_MODEL,
           "-c", "model_reasoning_effort=high", "-o", str(out)]
    if folder:
        cmd += ["--cd", str(folder)]
    cmd += ["-"]
    log = out.with_suffix(".log")
    with open(log, "w", encoding="utf-8") as lf:
        r = subprocess.run(cmd, input=prompt, text=True, encoding="utf-8", stdout=lf, stderr=subprocess.STDOUT,
                           timeout=timeout)
    return r.returncode


def run_agy(prompt: str, folder: Path | None, out: Path, timeout: int) -> int:
    if folder and len(prompt) > INLINE_MAX:
        (folder / "_prompt.md").write_text(prompt, encoding="utf-8")
        prompt = f"이 폴더의 `_prompt.md`를 읽고 그 지시를 수행하라. 폴더: {folder}"
    cmd = [find("agy"), "--model", AGY_MODEL, "--effort", "high", f"--print-timeout={timeout}s"]
    if folder:
        cmd += ["--add-dir", str(folder)]
    cmd += [f"--print={prompt}"]
    with open(out, "w", encoding="utf-8") as of, open(out.with_suffix(".err"), "w", encoding="utf-8") as ef:
        r = subprocess.run(cmd, stdout=of, stderr=ef, stdin=subprocess.DEVNULL, text=True, encoding="utf-8",
                           timeout=timeout + 60)
    return r.returncode


def main() -> int:
    for st in (sys.stdout, sys.stderr):
        try:
            st.reconfigure(encoding="utf-8")
        except Exception:  # noqa: BLE001
            pass
    ap = argparse.ArgumentParser()
    ap.add_argument("role", choices=["which", *ORDER])
    ap.add_argument("--prompt-file")
    ap.add_argument("--dir", help="the only folder the delegate may read (research: extra reading; it still searches the web)")
    ap.add_argument("--out")
    ap.add_argument("--timeout", type=int, default=1800)
    a = ap.parse_args()
    if a.role == "which":
        for role in ORDER:
            print(f"{role:9s} -> {pick(role) or 'none (run as a subagent and say so)'}")
        return 0
    who = pick(a.role)
    if not who:
        print(f"{a.role}: neither codex nor agy is installed. Run this role as a subagent and name the "
              "fallback in the delivery report.", file=sys.stderr)
        return 3
    if who != ORDER[a.role][0]:
        print(f"{a.role}: {ORDER[a.role][0]} is missing, falling back to {who} — say so in the delivery.")
    folder = Path(a.dir).resolve() if a.dir else None
    out = Path(a.out).resolve()
    out.parent.mkdir(parents=True, exist_ok=True)
    prompt = Path(a.prompt_file).read_text(encoding="utf-8")
    # codex's Windows read-only sandbox is denied on a Google Drive (virtual) drive: it then answers
    # "access denied" with nothing read. Give it a copy of the folder on the local temp disk.
    stage = None
    if folder and who == "codex":
        stage = Path(tempfile.mkdtemp(prefix="hsdeck-"))
        shutil.copytree(folder, stage, dirs_exist_ok=True)
    run_dir = stage or folder
    if a.role == "research":
        prompt += RULE_WEB_DIR.format(dir=run_dir) if run_dir else RULE_WEB
    else:
        prompt += RULE.format(dir=run_dir) if run_dir else RULE_WEB
    try:
        rc = (run_codex if who == "codex" else run_agy)(prompt, run_dir, out, a.timeout)
    finally:
        if stage:
            shutil.rmtree(stage, ignore_errors=True)
    size = out.stat().st_size if out.exists() else 0
    print(f"{a.role} by {who}: exit {rc}, {size} bytes -> {out}")
    if rc or size == 0:
        print("  empty or failed: read the .log/.err next to the output before retrying.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
