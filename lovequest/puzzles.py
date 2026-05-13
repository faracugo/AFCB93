import base64

def puzzle_base64(user_answer: str) -> bool:
    raw = "TEFfUFJJTUVSQV9QSVM6X0JVTkNBX0VTX0VOVEVOREVS"
    decoded = base64.b64decode(raw).decode("utf-8", errors="ignore").lower()
    # decoded: "LA_PRIMERA_PIS:_BUNCA_ES_ENTENDER" (lo ajustas si quieres)
    return user_answer.replace(" ", "") in decoded.replace("_", "")

def puzzle_caesar(text: str, shift: int, encrypt: bool = True) -> str:
    s = shift % 26
    if not encrypt:
        s = (-s) % 26

    out = []
    for ch in text:
        if "A" <= ch <= "Z":
            out.append(chr((ord(ch) - 65 + s) % 26 + 65))
        elif "a" <= ch <= "z":
            out.append(chr((ord(ch) - 97 + s) % 26 + 97))
        else:
            out.append(ch)
    return "".join(out)

def puzzle_repo_hunt(user_key: str, expected: str) -> bool:
    return user_key.strip().lower() == expected.strip().lower()
