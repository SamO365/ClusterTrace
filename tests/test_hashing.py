import hashlib
from clustertrace.hashing import calculate_sha256

def test_hashing(tmp_path):
    test_file = tmp_path / "test_file.txt"
    test_file.write_bytes(b"test")

    expected = hashlib.sha256(b"test").hexdigest()
    result = calculate_sha256(test_file)
    assert result == expected