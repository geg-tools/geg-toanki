from pathlib import Path


def detect_file_type(file_path: str) -> str:
    file_extension = Path(file_path).suffix.lower()
    return file_extension
