import json
import os
import sys
from datetime import datetime
from .puzzles import puzzle_base64, puzzle_caesar, puzzle_repo_hunt
from .letter import build_letter

ROOT = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(ROOT, "config.json")
FINAL_DIR = os.path.join(os.path.dirname(ROOT), "final")
OUTPUT_HTML = os.path.join(os.path.dirname(ROOT), "final", "index.html")

def _load_config():
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def _clear():
    os.system("cls" if os.name == "nt" else "clear")

def _pause(msg="Enter para continuar..."):
    input(f"\n{msg}")

def _heart():
    return r"""
     _  _   _  _
    ( \/ ) ( \/ )
     \  /   \  /
      \/  .  \/
       \     /
        \   /
         \_/
    """

def run():
    cfg = _load_config()
    name = cfg.get("Andrés", "Vida")

    _clear()
    print(_heart())
    print(f"Hola, {name}.")
    print("Bienvenido a LoveQuest: un repo con un secreto.\n")
    print("Regla: aquí avanzas como dev… leyendo, deduciendo y recordando 💛")
    _pause()

    # Nivel 1 — Base64
    _clear()
    print("NIVEL 1/3 — Señal encriptada")
    print("Decodifica esto (pista: Base64):\n")
    code = "TEFfUFJJTUVSQV9QSVM6X0JVTkNBX0VTX0VOVEVOREVS"
    print(code)
    ans = input("\n¿Qué dice? > ").strip().lower()
    if not puzzle_base64(ans):
        print("\nMmm… casi. Tip: busca un decodificador Base64 😉")
        sys.exit(1)

    # Nivel 2 — César (con clave por fecha)
    _clear()
    print("NIVEL 2/3 — Cifrado clásico")
    ann = cfg.get("anniversary", "2026-01-04")
    shift = int(datetime.fromisoformat(ann).day) % 26
    encrypted = puzzle_caesar("NUESTRA PALABRA SECRETA ES", shift, encrypt=True)
    print(f"Fecha especial detectada: {ann}")
    print("Usa el día del mes como desplazamiento (día % 26).")
    print("\nTexto cifrado:")
    print(encrypted)
    ans2 = input("\n¿Texto descifrado? (tal cual) > ").strip().upper()
    if ans2 != "NUESTRA PALABRA SECRETA ES":
        print("\nCasi… recuerda: es un César shift con el día del aniversario.")
        sys.exit(1)

    # Nivel 3 — Caza en el repo (palabra interna)
    _clear()
    print("NIVEL 3/3 — Caza del tesoro en el repo")
    print("Encuentra la palabra clave en el repositorio.")
    print("Pista: está en un archivo que NO parece romántico.\n")
    key = input("Palabra clave > ").strip()
    if not puzzle_repo_hunt(key, cfg.get("secret_word", "")):
        print("\nNope. Tip: revisa archivos tipo NOTES.md / CHANGELOG.md / comments.")
        sys.exit(1)

    # Final — Generar carta HTML
    _clear()
    print("✅ Desbloqueado: el final.")
    os.makedirs(FINAL_DIR, exist_ok=True)
    build_letter(cfg, OUTPUT_HTML)
    print(f"\nTe dejé una carta aquí:\n{OUTPUT_HTML}")
    print("\n(Ábrela en tu navegador. Y sí: está hecha para ti.)")
    print(_heart())
