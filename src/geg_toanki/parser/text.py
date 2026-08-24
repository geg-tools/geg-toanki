from pathlib import Path

def parse_text(file_path: str) -> str:
    return Path(file_path).read_text(encoding="utf-8")