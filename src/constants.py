from ctypes import c_uint8, c_uint16, c_uint32, c_float

HEADER_SIZE: c_uint8 = c_uint8(19)
NAME: int = 0
TEMPO: int = 2
LENGTH: int = 5
FREQ: int = 6
SPB: int = 3
P_LEN: int = 4
NUM_TRACKS: int = 1
BITS: int = 7
TEMPO_DEFAULT: c_float = c_float(120.0)
SPB_DEFAULT: c_uint16 = c_uint16(60)
P_LEN_DEFAULT: c_uint16 = c_uint16(240)
NUM_TRACKS_DEFAULT: c_uint8 = c_uint8(4)
LENGTH_DEFAULT: float = c_float(1.0)
FREQ_DEFAULT: c_uint32 = c_uint32(44100)
BITS_DEFAULT: c_uint8 = c_uint8(24)
SETTINGS_FILE_SYNTAX: dict[str: str] = {"e": "Name: ",
                                        "c": "Tracks: ",
                                        ":": "BPM: ",
                                        "p": "Samples/beat: ",
                                        "t": "Pattern length: ",
                                        "g": "Length: ",
                                        "q": "Frequency: ",
                                        " ": "Bit depth: "}
