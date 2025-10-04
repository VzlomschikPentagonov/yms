from functions import *
from typing import BinaryIO

def main() -> None:
    s: tuple = read_settings()
    h: Header = Header(*s)
    b: bytes = get_header(h)
    print(b, len(b))
    f: BinaryIO = open(h.name + ".yusm", "w+b")
    f.write(b)
    return None

if __name__ == "__main__":
   main()