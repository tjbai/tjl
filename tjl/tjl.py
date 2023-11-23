import sys
from pathlib import Path


def run_file(path: Path) -> None:
    pass

def run_prompt() -> None:
    raise NotImplementedError()

def main():
    if len(sys.argv) > 2:
        print('Usage: tjl {script}.tj')
        exit(1)
    elif len(sys.argv) == 2:
        run_file(sys.argv[1])
    else:
        run_prompt()
