from classes import *
from re import match
from typing import BinaryIO, TextIO

def read_header(name: str) -> list:
    c_file: BinaryIO = open(name + ".yusm", "r+b")
    settings: list = []
    c_file.seek(1)
    for i in range(NUM_VALUES):
        buf: c_char_p = create_string_buffer(
                        c_file.read(SIZEOF_VALUES[i]), SIZEOF_VALUES[i])
        ptr: c_void_p = cast(addressof(buf), POINTER(type(VAL_TYPES[i])))
        value: type(VAL_TYPES[i]) = ptr.contents
        settings.append(value.value)
    return settings

def isdigit(char: str) -> bool:
    if 48 <= ord(char) <= 57:
        return True
    else:
        return False

def tokenize(line: str) -> list[int]:
    tokens: list[int] = []
    str_token: str = ""
    digit_flag: bool = False
    line += chr(255)
    for char in line:
        match isdigit(char):
            case True:
                str_token += char
                digit_flag = True
            case False:
                if digit_flag:
                    tokens.append(int(str_token))
                    str_token = ""
                digit_flag = False
    return tokens

def read_pattern(name: str) -> list[Sample]:
    pattern_file: TextIO = open(name + ".pat")
    pattern_data: list[str] = pattern_file.readlines()
    sample_list: list[Sample] = []
    _sample: list = [0, 0, 0]
    for line in range(len(pattern_data)):
        pattern_data[line] = pattern_data[line].replace(" ", "")
        if match(REM_ABS_LENGTH, pattern_data[line]):
            _sample = tokenize(pattern_data[line])
            _sample[2] -= _sample[1]
        elif match(REM_REL_LENGTH, pattern_data[line]):
            _sample = tokenize(pattern_data[line])
        sample_list.append(Sample(*_sample))
    return sample_list