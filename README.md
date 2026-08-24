# CountFileTypes

A lightweight Python command-line tool for analyzing a directory and counting its files by extension.

## Features

- Recursively scan a directory.
- Count files and subdirectories.
- Count unique file extensions.
- Show the distribution of file types.
- Sort file extensions by file count.
- Handle files without an extension.
- Use only Python's standard library.

## Requirements

- Python 3.8 or later

## Usage

Run the program:

```bash
python main.py
```

Enter the path of the directory you want to analyze when prompted.

Example:

```text
Enter folder path: C:\Users\User\Downloads
```

## Example

```text
========================================
Root folder: C:\Users\User\Downloads
Total subfolders: 12
Total files: 247
Total file extensions: 8
----------------------------------------
File extension distribution:
.pdf : 82 file(s)
.jpg : 54 file(s)
.png : 41 file(s)
.txt : 25 file(s)
.mp4 : 18 file(s)
.zip : 15 file(s)
.docx : 10 file(s)
(no extension) : 2 file(s)
========================================
```

## How It Works

CountFileTypes recursively scans the selected directory using Python's `pathlib` and analyzes the resulting files.

File extensions are normalized to lowercase so that extensions such as `.JPG` and `.jpg` are counted as the same type.

Files without an extension are grouped separately as `(no extension)`.