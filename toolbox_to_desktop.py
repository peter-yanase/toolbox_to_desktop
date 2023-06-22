import re
from pathlib import Path
import sys

assert (sys.version_info >= (3, 5))

CONTAINER: str = "fedora-toolbox-38"  # Rename to appropriate
SOURCE: Path = Path("/usr")
TARGET: Path = Path.home() / ".local"
PATHS: list[Path] = [(SOURCE / "share/icons/"), (SOURCE / "share/applications/")]


def create_desktop() -> None:
    search_term: str = input("Search: ").lower()
    paths_found: list[Path] = sum([list(path.rglob(f'*{search_term}*')) for path in PATHS], [])
    if not paths_found:
        sys.exit("Nothing found.")
    for path_found in paths_found:
        target_parents: Path = Path(*(list(TARGET.parts) + list((path_found.parent).parts)[2:]))
        target_path: Path = target_parents / path_found.name
        if not target_parents.exists():
            target_parents.mkdir(parents=True)
        if target_path.suffix == ".desktop":
            text: str = path_found.read_text()
            new_text: str = re.sub("Exec=", f"Exec=toolbox run -c {CONTAINER} ", text)
            target_path.write_text(new_text)
        else:
            data: bytes = path_found.read_bytes()
            target_path.write_bytes(data)
    print("Finished")


if __name__ == "__main__":
    create_desktop()
