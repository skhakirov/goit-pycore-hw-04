import sys
from pathlib import Path
from colorama import init, Fore

init()


def print_tree(path, prefix=""):
    entries = sorted(path.iterdir(), key=lambda e: (e.is_file(), e.name))
    for i, entry in enumerate(entries):
        is_last = i == len(entries) - 1
        connector = "\u2514\u2500\u2500 " if is_last else "\u251c\u2500\u2500 "
        if entry.is_dir():
            print(f"{prefix}{connector}{Fore.BLUE}{entry.name}/{Fore.RESET}")
            extension = "    " if is_last else "\u2502   "
            print_tree(entry, prefix + extension)
        else:
            print(f"{prefix}{connector}{Fore.GREEN}{entry.name}{Fore.RESET}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Використання: python task3.py /шлях/до/директорії")
        sys.exit(1)

    dir_path = Path(sys.argv[1])

    if not dir_path.exists():
        print(f"Шлях '{dir_path}' не існує.")
        sys.exit(1)

    if not dir_path.is_dir():
        print(f"'{dir_path}' не є директорією.")
        sys.exit(1)

    print(f"{Fore.BLUE}{dir_path.name}/{Fore.RESET}")
    print_tree(dir_path)
