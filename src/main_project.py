from func_project import *
from func_header import read_settings
from typing import BinaryIO

def main() -> None:
    s: tuple = read_settings()
    create_project(s[0], s[1].value)
    return None

if __name__ == "__main__":
   main()