from classes import *
from os import mkdir, chdir

def get_header(header: Header) -> bytes:
    header_data: tuple[c_uint8, c_uint8, c_uint32, c_uint16,
                      c_uint16, c_uint32, c_uint8] = (HEADER_SIZE,
                      header.num_tracks, header.tempo, header.spb,
                      header.p_len, header.freq, header.bits)
    bytestr : bytes = b""
    for var in header_data:
        bytestr += bytes(var)
    return bytestr
