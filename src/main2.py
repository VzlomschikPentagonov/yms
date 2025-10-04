from functions2 import *

def mainkraft() -> None:
    s: list = read_header("test")
    h: Header = Header("test", *s)
    print(h.name,
          h.num_tracks,
          h.tempo,
          h.spb,
        h.p_len,
        h.length,
        h.freq,
        h.bits)
    p: list[Sample] = read_pattern("../pattern")
    for i in p:
        print(i.note, i.start, i.length)
    return None

if __name__ == "__main__":
   mainkraft()