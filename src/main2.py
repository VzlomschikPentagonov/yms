from functions2 import *

def mainkraft() -> None:
    s: list = read_header("test")
    h: Header = Header("test", *s)
    print(h.name,
        h.tempo,
        h.length,
        h.freq,
        h.spb,
        h.p_len,
        h.num_tracks,
        h.bits)
    return None

if __name__ == "__main__":
   mainkraft()