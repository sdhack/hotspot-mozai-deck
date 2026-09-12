# -*- coding: utf-8 -*-
"""gpt-image-2 (image2) 单页成图脚本 · hotspot-mozai-deck 统一风格流水线

任何 agent 用本脚本 + 模版 Prompt 文件即可复现与既有成品一致的墨仔图文风格。

用法：
  python gen_gpt2_page.py --prompt prompt.txt --out 01-封面.jpg --mode dual --seed 81
  python gen_gpt2_page.py --prompt prompt.txt --out 02-内页.jpg --mode dual --seed 71
  python gen_gpt2_page.py --prompt prompt.txt --out 03-页面.jpg --mode canvas --canvas last-ok.jpg --seed 9

Key 解析顺序：环境变量 GPT2_API_KEY → assets/gpt2-api-key.txt（本地文件，不入库）。
--mode dual   双参考：风格参考图 + 墨仔人物卡（默认，封面与场景内页用这个）
--mode canvas 单画布整页替换：无风格参考时，传一张自有成品页当纸张画布
"""
import argparse, base64, io, os, sys, time
import numpy as np
import requests
from PIL import Image, ImageEnhance

API = "https://api.790053500.com/v1/images/edits"
MODEL = "gpt-image-2"
SIZE = "1024x1365"
SKILL_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS = os.path.join(SKILL_DIR, "assets")

DUAL_HEADER = (
    "The FIRST attached image is a style reference: learn ONLY its art style, texture and lettering feel. "
    "The SECOND attached image is the character appearance truth (appearance only, never copy its sheet "
    "layout or poses). Replace everything with the BRAND NEW page described below — keep no text, layout, "
    "page number or scene from either image.\n\n"
)
CANVAS_HEADER = (
    "Replace the entire page with a BRAND NEW page described below. The attached image serves only as the "
    "paper/style canvas — do not keep any of its text, layout, page number or scene.\n\n"
)


def resolve_key():
    key = os.environ.get("GPT2_API_KEY", "").strip()
    if key:
        return key
    key_file = os.path.join(ASSETS, "gpt2-api-key.txt")
    if os.path.exists(key_file):
        key = open(key_file, encoding="utf-8").read().strip()
        if key:
            return key
    sys.exit("missing key: set env GPT2_API_KEY or create assets/gpt2-api-key.txt")


def request_image(prompt, mode, style_ref, canvas, mozai_ref, seed):
    data = {"model": MODEL, "prompt": prompt, "size": SIZE, "n": "1"}
    if seed is not None:
        data["seed"] = str(seed)
    if mode == "dual":
        files = [("image", ("ref_style.jpg", open(style_ref, "rb"), "image/jpeg")),
                 ("image", ("mozai.jpg", open(mozai_ref, "rb"), "image/jpeg"))]
    else:
        files = [("image", ("canvas.jpg", open(canvas, "rb"), "image/jpeg"))]
    for attempt in range(4):
        try:
            r = requests.post(API, headers={"Authorization": "Bearer " + resolve_key()},
                              data=data, files=files, timeout=560)
            if r.status_code in (403, 429, 502):
                print(f"attempt {attempt+1}: status {r.status_code}, backoff 20s")
                time.sleep(20)
                continue
            r.raise_for_status()
            item = r.json()["data"][0]
            if item.get("b64_json"):
                return base64.b64decode(item["b64_json"])
            url = item.get("url") or ""
            if url.startswith("http"):
                return requests.get(url, timeout=300).content
            if url.startswith("data:"):
                return base64.b64decode(url.split(",", 1)[1])
            raise SystemExit("unknown response: " + repr(item)[:300])
        except requests.RequestException as e:
            print(f"attempt {attempt+1}: {e}")
            time.sleep(15)
    raise SystemExit("all attempts failed")


def postprocess(raw, out, seed=None):
    im = Image.open(io.BytesIO(raw)).convert("RGB")
    print("raw size:", im.size, "ratio:", round(im.size[0] / im.size[1], 4))
    im = ImageEnhance.Contrast(im).enhance(1.04)
    im = ImageEnhance.Color(im).enhance(0.72)
    a = np.asarray(im).astype(np.float64)
    TARGET = np.array([254.0, 251.5, 246.5])
    for _ in range(3):
        lum = a.mean(axis=2)
        sel = a[lum > np.percentile(lum, 60)]
        a = np.clip(a * (TARGET / np.clip(sel.mean(0), 1, 255)), 0, 255)
    import random
    rng = np.random.default_rng(seed if seed is not None else random.randrange(10 ** 6))
    noise = rng.random((14, 19))
    warm = np.asarray(Image.fromarray((noise * 255).astype(np.uint8)).resize(
        (a.shape[1], a.shape[0]), Image.BICUBIC)).astype(np.float64) / 255.0 - 0.5
    a[..., 0] = np.clip(a[..., 0] * (1 + 0.006 * warm), 0, 255)
    a[..., 1] = np.clip(a[..., 1] * (1 + 0.0035 * warm), 0, 255)
    a[..., 2] = np.clip(a[..., 2] * (1 - 0.002 * warm), 0, 255)
    im = Image.fromarray(a.astype(np.uint8))
    im.save(out, "JPEG", quality=92)
    assert open(out, "rb").read(3) == b"\xff\xd8\xff", "JPEG header mismatch"
    print("saved:", out, Image.open(out).size, "header ok")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--prompt", required=True, help="prompt txt file (UTF-8)")
    ap.add_argument("--out", required=True, help="output .jpg path (versioned, never overwrite last ok)")
    ap.add_argument("--mode", choices=["dual", "canvas"], default="dual")
    ap.add_argument("--style-ref", default=os.path.join(ASSETS, "style-ref-cream-journal.jpg"))
    ap.add_argument("--mozai-ref", default=os.path.join(ASSETS, "mozai-ip-sheet-4k.jpg"))
    ap.add_argument("--canvas", help="own finished page used as paper canvas (mode=canvas)")
    ap.add_argument("--seed", type=int, default=None)
    args = ap.parse_args()

    if os.path.exists(args.out):
        sys.exit(f"refusing to overwrite existing file: {args.out} (use a new versioned name)")
    prompt = open(args.prompt, encoding="utf-8").read()
    if args.mode == "dual":
        prompt = DUAL_HEADER + prompt
    else:
        if not args.canvas:
            sys.exit("--canvas is required in canvas mode")
        prompt = CANVAS_HEADER + prompt
    raw = request_image(prompt, args.mode, args.style_ref, args.canvas, args.mozai_ref, args.seed)
    postprocess(raw, args.out, args.seed)


if __name__ == "__main__":
    main()
