from constants import *

class Header:
    def __init__(self, name: str = "UnnamedProject",
                 num_tracks: c_uint8 = NUM_TRACKS_DEFAULT,
                 tempo: c_float = TEMPO_DEFAULT,
                 spb: c_uint16 = SPB_DEFAULT,
                 p_len: c_uint16 = P_LEN_DEFAULT,
                 length: c_float = LENGTH_DEFAULT,
                 freq: c_uint32 = FREQ_DEFAULT,
                 bits: c_uint8 = BITS_DEFAULT):
        self.name = name
        self.num_tracks = num_tracks
        self.tempo = tempo
        self.spb = spb
        self.p_len = p_len
        self.length = length
        self.freq = freq
        self.bits = bits