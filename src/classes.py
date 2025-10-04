from constants import *

class Header:
    def __init__(self, name: str = "UnnamedProject",
                 num_tracks: c_uint8 | int = NUM_TRACKS_DEFAULT,
                 tempo: c_float | float = TEMPO_DEFAULT,
                 spb: c_uint16 | int = SPB_DEFAULT,
                 p_len: c_uint16 | int = P_LEN_DEFAULT,
                 length: c_float | float = LENGTH_DEFAULT,
                 freq: c_uint32 | int = FREQ_DEFAULT,
                 bits: c_uint8 | int = BITS_DEFAULT):
        self.name = name
        self.num_tracks = num_tracks
        self.tempo = tempo
        self.spb = spb
        self.p_len = p_len
        self.length = length
        self.freq = freq
        self.bits = bits

class Sample:
    def __init__(self, note: c_uint8 | int = 69,
                 start: c_uint16 | int = 0,
                 length: c_uint16 | int = 0):
        self.note = note
        self.start = start
        self.length = length