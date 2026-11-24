"""Token-grid illustrations for slides 6-7 (Self-Flow Fig. 3 re-drawn): one clean image from Fig. 1(b),
noise mixed in pixel space per 6x6 token. Run from the repository root."""
import io
import numpy as np
import pymupdf as fitz
from PIL import Image, ImageDraw

d = fitz.open("work/self-flow-full/source/paper.pdf")
pix = d[0].get_pixmap(dpi=600, clip=fitz.Rect(304.0, 171.2, 376.6, 243.7))   # Self-Flow parrot, Fig. 1(b)
S, G = 840, 6
P = S // G
im = Image.open(io.BytesIO(pix.tobytes("png"))).convert("RGB").resize((S, S), Image.LANCZOS)
x0 = np.asarray(im).astype(np.float32) / 127.5 - 1
rng = np.random.default_rng(7)
eps = rng.standard_normal(x0.shape).astype(np.float32)
t, s = 0.3, 0.8
idx = rng.choice(G * G, 9, replace=False)                 # R_M = 0.25 -> 9 of 36
M = np.zeros(G * G, bool); M[idx] = True; M = M.reshape(G, G)
ti = rng.uniform(0.05, 0.95, (G, G))                      # diffusion-forcing style: one t per token
WARM = (232, 160, 46)


def render(tau, marked, name):
    tau_px = np.kron(tau, np.ones((P, P)))[..., None]
    x = (1 - tau_px) * x0 + tau_px * eps
    img = Image.fromarray(((np.clip(x, -1, 1) + 1) * 127.5).astype(np.uint8))
    dr = ImageDraw.Draw(img)
    for k in range(1, G):
        dr.line([(k * P, 0), (k * P, S)], fill=(255, 255, 255), width=3)
        dr.line([(0, k * P), (S, k * P)], fill=(255, 255, 255), width=3)
    for r, c in zip(*np.nonzero(marked)):
        dr.rectangle([c * P + 3, r * P + 3, (c + 1) * P - 4, (r + 1) * P - 4], outline=WARM, width=8)
    img.save(f"work/self-flow-full/deck/assets/fig/{name}.jpg", quality=90)


none = np.zeros((G, G), bool)
render(np.full((G, G), t), none, "tok_vanilla")
render(np.where(M, 1.0, t), M, "tok_fullmask")
render(ti, none, "tok_dforcing")
render(np.where(M, s, t), M, "tok_dual")

print("mask tokens:", int(M.sum()))
