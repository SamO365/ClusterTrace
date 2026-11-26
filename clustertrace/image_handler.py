#image validation, checks if paths are correct and follow rules
from pathlib import Path

ALLOWED_EXTENSIONS = set(['.img', '.dd', '.raw', '.001', '.txt'])

def validate_img_path(image_path):
    path = Path(image_path)

    #if the file doesnt exist, raise alarm
    if not path.exists():
        raise FileNotFoundError(f"Image does not exist: {path}")

    #if the file path isnt a file, raise alarm
    if not path.is_file():
        raise ValueError(f"Path isn't a file: {path}")

    #if the suffix isnt allowed, raise alarm
    if path.suffix.lower() not in ALLOWED_EXTENSIONS:
        raise ValueError(f"Unsupported file extension: {path.suffix}")

    return path