def read_header(name: str) -> list:
    c_file: BinaryIO = open(name + ".yusm", "r+b")
    settings: list = []
    c_file.seek(1)
    for i in range(NUM_VALUES):
        buf: c_char_p = create_string_buffer(
                        c_file.read(SIZEOF_VALUES[i]), SIZEOF_VALUES[i])
        ptr: c_void_p = cast(addressof(buf), POINTER(type(VAL_TYPES[i])))
        value: type(VAL_TYPES[i]) = ptr.contents
        settings.append(value)
        print(settings)
    return settings

def mainkraft() -> None:
    s: list = read_header("test")
    # s: tuple = read_settings()
    h: Header = Header("test", *s)
    # b: bytes = get_header(h)
    # print(b, len(b))
    # f: BinaryIO = open(h.name + ".yusm", "w+b")
    # f.write(b)
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
