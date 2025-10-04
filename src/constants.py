from ctypes import *

# pytype values
NAME: int = 0
NUM_TRACKS: int = 1
TEMPO: int = 2
SPB: int = 3
P_LEN: int = 4
LENGTH: int = 5
FREQ: int = 6
BITS: int = 7
NUM_VALUES: int = 7
# ctype default values
HEADER_SIZE: c_uint8 = c_uint8(19)
TEMPO_DEFAULT: c_float = c_float(120.0)
SPB_DEFAULT: c_uint16 = c_uint16(60)
P_LEN_DEFAULT: c_uint16 = c_uint16(240)
NUM_TRACKS_DEFAULT: c_uint8 = c_uint8(4)
LENGTH_DEFAULT: c_float = c_float(1.0)
FREQ_DEFAULT: c_uint32 = c_uint32(44100)
BITS_DEFAULT: c_uint8 = c_uint8(24)
# arrays
SIZEOF_VALUES: list[int] = [1, 4, 2, 2, 4, 4, 1]
VAL_TYPES: tuple = (c_uint8(), c_float(), c_uint16(), c_uint16(),
                    c_float(), c_uint32(), c_uint8())
VAL_TYPES_2: tuple = (int(), float(), int(), int(),
                      float(), int(), int())
SETTINGS_FILE_SYNTAX: dict[str: str] = {"e": "Name: ",
                                        "c": "Tracks: ",
                                        ":": "BPM: ",
                                        "p": "Samples/beat: ",
                                        "t": "Pattern length: ",
                                        "g": "Length: ",
                                        "q": "Frequency: ",
                                        " ": "Bit depth: "}
# regex match strings
REM_ABS_LENGTH = "\\d+:\\d+-\\d+"
REM_REL_LENGTH = "\\d+:\\d+/\\d+"