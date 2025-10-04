from classes import *
from typing import TextIO
# from os import mkdir, chdir

def read_settings() -> tuple:
    settings_file: TextIO = open("../settings.txt")
    settings_read: list[str] = settings_file.readlines() # read settings file
    settings_new: list[str] = []
    for line in settings_read: # iterate through settings list
        settings_new.append(line.lstrip(SETTINGS_FILE_SYNTAX[line[3]])[:-1])
    return (settings_new[NAME],
            c_uint8(int(settings_new[NUM_TRACKS])),
            c_float(float(settings_new[TEMPO])),
            c_uint16(int(settings_new[SPB])),
            c_uint16(int(settings_new[P_LEN])),
            c_float(float(settings_new[LENGTH])),
            c_uint32(int(settings_new[FREQ])),
            c_uint8(int(settings_new[BITS])))

def get_header(header: Header) -> bytes:
    header_data: tuple[c_uint8, c_uint8, c_uint32, c_uint16,
                      c_uint16, c_uint32, c_uint32, c_uint8] = (HEADER_SIZE,
                      header.num_tracks, header.tempo, header.spb,
                      header.p_len, header.length, header.freq, header.bits)
    bytestr: bytes = b""
    for var in header_data:
        bytestr += bytes(var)
    return bytestr