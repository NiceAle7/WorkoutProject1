import os
def cipher(file, file2):
    if os.path.exists(file):
        with open(f'{file}', 'r') as file1:
            contents = file1.read().strip()
            cipher = contents[::-1]
        with open(f'{file2}', 'w') as new_file:
            new_file.write(cipher)


def main():
    user_files = input("Enter a file to cipher and a new file: ").split()
    cipher(user_files[0], user_files[1])

if __name__ == "__main__":
    main()