print("ClusterTrace is starting\n")


from clustertrace.image_handler import validate_img_path
from clustertrace.hashing import calculate_sha256

def main():
    img_path = input("Enter forensic image path: ")
    validated_path = validate_img_path(img_path)

    print("File validation successful")
    print("SHA-256:", calculate_sha256(validated_path))


if __name__ == "__main__":
    main()