import sys
from pathlib import Path

try:
    from colorama import Fore, Style, init
except ImportError:
    # Fallback keeps the script working even if colorama is not installed yet.
    class _ForeFallback:
        BLUE = ""
        GREEN = ""
        RED = ""

    class _StyleFallback:
        RESET_ALL = ""

    Fore = _ForeFallback()
    Style = _StyleFallback()

    def init(*_args, **_kwargs) -> None:
        """Fallback initialization when colorama is unavailable."""


def get_directory_icon() -> str:
    """Return a folder icon only if the terminal encoding supports it."""
    if not text_supported("📂 "):
        return ""

    return "📂 "


def text_supported(text: str) -> bool:
    """Check whether text can be printed with the current terminal encoding."""
    encoding = sys.stdout.encoding or "utf-8"

    try:
        text.encode(encoding)
        return True
    except (LookupError, UnicodeEncodeError):
        return False


def get_tree_symbols() -> tuple[str, str, str, str]:
    """Return tree drawing symbols supported by the current terminal."""
    if text_supported("│├└"):
        return "│   ", "├── ", "└── ", "    "

    return "|   ", "|-- ", "`-- ", "    "


def get_display_name(path: Path) -> str:
    """Return a readable name for a path, including '.' and root paths."""
    return path.name or str(path.resolve())


def format_directory_name(directory: Path) -> str:
    """Return a formatted directory name with an icon."""
    return f"{get_directory_icon()}{get_display_name(directory)}"


def print_directory_tree(directory: Path, prefix: str = "") -> None:
    """Recursively print the directory tree with colored output."""
    vertical, branch_symbol, last_branch_symbol, indent = get_tree_symbols()

    try:
        items = sorted(
            directory.iterdir(),
            key=lambda item: (item.is_file(), item.name.lower()),
        )
    except PermissionError:
        print(f"{prefix}{Fore.RED}[Permission denied]{Style.RESET_ALL}")
        return

    for index, item in enumerate(items):
        is_last = index == len(items) - 1
        branch = last_branch_symbol if is_last else branch_symbol

        if item.is_dir():
            print(
                f"{prefix}{branch}{Fore.BLUE}"
                f"{format_directory_name(item)}"
                f"{Style.RESET_ALL}"
            )
            next_prefix = prefix + (indent if is_last else vertical)
            print_directory_tree(item, next_prefix)
        else:
            print(f"{prefix}{branch}{Fore.GREEN}{item.name}{Style.RESET_ALL}")


def main() -> None:
    """Parse CLI arguments and print the directory structure."""
    init(autoreset=True)

    if len(sys.argv) != 2:
        print("Usage: python task3.py /path/to/directory")
        return

    directory = Path(sys.argv[1])

    if not directory.exists():
        print(f"Error: path '{directory}' does not exist.")
        return

    if not directory.is_dir():
        print(f"Error: path '{directory}' is not a directory.")
        return

    print(f"{Fore.BLUE}{format_directory_name(directory)}{Style.RESET_ALL}")
    print_directory_tree(directory)


if __name__ == "__main__":
    main()
