import os
from datetime import datetime

def build_letter(cfg: dict, output_path: str):
    template_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "final", "template.html")
    with open(template_path, "r", encoding="utf-8") as f:
        html = f.read()

    ann = cfg.get("anniversary", "2023-01-01")
    try:
        ann_fmt = datetime.fromisoformat(ann).strftime("%d/%m/%Y")
    except Exception:
        ann_fmt = ann

    replacements = {
        "{{BOYFRIEND_NAME}}": cfg.get("boyfriend_name", "Amor"),
        "{{NICKNAME}}": cfg.get("nickname", "mi amor"),
        "{{ANNIVERSARY}}": ann_fmt,
        "{{PLACE_1}}": cfg.get("place_1", ""),
        "{{PLACE_2}}": cfg.get("place_2", ""),
        "{{SONG}}": cfg.get("song", ""),
        "{{TITLE}}": cfg.get("final_message_title", "Te amo"),
        "{{BODY}}": cfg.get("final_message_body", ""),
        "{{MEM1}}": (cfg.get("memories") or [""])[0] if (cfg.get("memories")) else "",
        "{{MEM2}}": (cfg.get("memories") or ["",""])[1] if len(cfg.get("memories") or []) > 1 else "",
        "{{MEM3}}": (cfg.get("memories") or ["","",""])[2] if len(cfg.get("memories") or []) > 2 else ""
    }

    for k, v in replacements.items():
        html = html.replace(k, str(v))

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)
