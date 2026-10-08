from pathlib import Path

folder_path = Path("path/to/your/folder")

# '*' matches all files recursively
file_names = [f.name for f in folder_path.rglob("*") if f.is_file()]

print(file_names)
