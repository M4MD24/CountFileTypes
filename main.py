from pathlib import Path


def validate_folder(folder_path):
    if not folder_path.exists():
        print("Folder does not exist.")
        return
    if not folder_path.is_dir():
        print("The specified path is not a folder.")
        return


def show_folder_path(folder_path):
    print(f"Root folder: {folder_path.absolute()}")


def show_total_sub_folders(all_items):
    sub_folders = [item for item in all_items if item.is_dir()]
    print(f"Total subfolders: {len(sub_folders)}")


def show_total_files(files):
    print(f"Total files: {len(files)}")


def analyze_folder(path):
    folder_path = Path(path)

    validate_folder(folder_path)

    all_items = list(folder_path.rglob('*'))

    print("\n" + "=" * 40)
    show_folder_path(folder_path)
    show_total_sub_folders(all_items)
    show_total_files(all_items)


if __name__ == "__main__":
    user_path = input("Enter folder path: ").strip()
    analyze_folder(user_path)
