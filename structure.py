import os

def show_structure(root="."):
    for dirpath, dirnames, filenames in os.walk(root):
        # Уровень вложенности для отступов
        level = dirpath.replace(root, "").count(os.sep)
        indent = "  " * level
        print(f"{indent}[{os.path.basename(dirpath)}]")
        subindent = "  " * (level + 1)
        for file in filenames:
            print(f"{subindent}{file}")

show_structure()