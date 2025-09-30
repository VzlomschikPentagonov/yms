from functions import *

def main() -> None:
    s: tuple = read_settings()
    h: Header = Header(*s)
    b: bytes = get_header(h)
    print(b, len(b))
    # f: BinaryIO = open(h.name + ".yusm", "w+b")
    # f.write(b)
    # f.seek(2)
    # a1: c_char_p = create_string_buffer(f.read(4), 4)
    # a2: c_void_p = cast(addressof(a1), POINTER(c_float))
    # a3: c_float = a2.contents
    # b1: c_char_p = create_string_buffer(f.read(2), 2)
    # b2: c_void_p = cast(addressof(b1), POINTER(c_uint16))
    # b3: c_uint16 = b2.contents
    # print(a3.value, b3.value)
    return None

if __name__ == "__main__":
   main()


