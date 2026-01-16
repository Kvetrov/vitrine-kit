#!/usr/bin/env python3
"""vitrine-kit: render a static showcase site from a JSON description."""
import json, pathlib, shutil, sys

VERSION = "1.1.0"
ROOT = pathlib.Path(__file__).parent


def head_extra(cfg):
    head = ""
    if cfg.get("analytics_id"):
        aid = cfg["analytics_id"]
        head += (f'<script async src="https://www.googletagmanager.com/gtag/js?id={aid}"></script>\n'
                 "<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}"
                 f"gtag('js',new Date());gtag('config','{aid}');</script>\n")
    return head


def render(cfg, out):
    layout = (ROOT / "layouts" / f"{cfg['layout']}.html").read_text(encoding="utf-8")
    out.mkdir(parents=True, exist_ok=True)
    (out / "assets").mkdir(exist_ok=True)
    css = (ROOT / "assets" / "vk-core.css").read_text(encoding="utf-8")
    css = (ROOT / "themes" / f"{cfg['theme']}.css").read_text(encoding="utf-8") + "\n" + css
    (out / "assets" / "vk-core.css").write_text(css, encoding="utf-8")
    shutil.copy(ROOT / "assets" / "vk-ui.js", out / "assets" / "vk-ui.js")
    for page in cfg["pages"]:
        html = layout.replace("{{head}}", head_extra(cfg))
        for key, value in {**cfg["site"], **page}.items():
            html = html.replace("{{" + key + "}}", str(value))
        (out / page["file"]).write_text(html, encoding="utf-8")


if __name__ == "__main__":
    cfg = json.loads(pathlib.Path(sys.argv[1]).read_text(encoding="utf-8"))
    render(cfg, pathlib.Path(sys.argv[2]))
    print("ok")
