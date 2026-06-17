import zipfile

def compress_file():
    filename = input("Enter file name to compress: ")
    zipname = input("Enter ZIP file name: ")

    with zipfile.ZipFile(zipname, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(filename)

    print("File compressed successfully!")

def decompress_file():
    zipname = input("Enter ZIP file name: ")
    extract_path = input("Enter extraction folder: ")

    with zipfile.ZipFile(zipname, 'r') as zipf:
        zipf.extractall(extract_path)

    print("File decompressed successfully!")

while True:
    print("\n1. Compress File")
    print("2. Decompress File")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        compress_file()

    elif choice == '2':
        decompress_file()

    elif choice == '3':
        print("Exiting...")
        break

    else:
        print("Invalid Choice!")
