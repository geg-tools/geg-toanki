import re


def clean_json_string(json_str: str) -> str:
    # Substitui barras invertidas não escapadas por barras invertidas duplas
    return re.sub(r"(?<!\\)\\(?!\\)", r"\\\\", json_str)
