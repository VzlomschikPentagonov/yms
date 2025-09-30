from ctypes import c_uint8, c_uint16, c_uint32, c_float

class Header:
    def __init__(self,
                 name: str = "UnnamedProject",
                 tempo: c_float = 120.0,
                 spb: c_uint16 = 60,
                 p_len: c_uint16 = 240,
                 freq: c_uint32 = 44100,
                 bits: c_uint8 = 24):
        self.name = name
        self.tempo = tempo
        self.spb = spb
        self.p_len = p_len
        self.freq = freq
        self.bits = bits
