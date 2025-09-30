from ctypes import c_uint8, c_uint16, c_uint32, c_float

HEADER_SIZE: c_uint8 = c_uint8(19)
TEMPO_DEFAULT: c_float = c_float(120.0)
SPB_DEFAULT: c_uint16 = c_uint16(60)
P_LEN_DEFAULT: c_uint16 = c_uint16(240)
NUM_TRACKS_DEFAULT: c_uint8 = c_uint8(4)
LENGTH_DEFAULT: float = c_float(1.0)
FREQ_DEFAULT: c_uint32 = c_uint32(44100)
BITS_DEFAULT: c_uint8 = c_uint8(24)
