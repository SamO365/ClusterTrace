import pytest
from clustertrace.image_handler import validate_img_path

def test_validate_img_path_valid_file(tmp_path):
    image = tmp_path / "test_image.img"
    image.write_bytes(b"test")

    result = validate_img_path(image)

    assert result == image

def test_validate_img_path_invalid_file(tmp_path):
    image = tmp_path / "invalid.img"

    with pytest.raises(FileNotFoundError):
        validate_img_path(image)

def test_validate_img_path_unsupported_extension(tmp_path):
    image = tmp_path / "unsupported.txt"
    image.write_bytes(b"test")

    with pytest.raises(ValueError):
        validate_img_path(image)

def test_validate_img_path_not_file(tmp_path):
    folder = tmp_path / "test_folder"
    folder.mkdir()

    with pytest.raises(ValueError):
            validate_img_path(folder)