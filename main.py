from pathlib import Path


def validate_folder(folder_path):
    if not folder_path.exists():
        print("Folder does not exist.")
        return
    if not folder_path.is_dir():
        print("The specified path is not a folder.")
        return


def analyze_folder(path):
    folder_path = Path(path)

    validate_folder(folder_path)


if __name__ == "__main__":
    user_path = input("Enter folder path: ").strip()
    analyze_folder(user_path)
