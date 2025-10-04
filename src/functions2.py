from classes import *
from typing import BinaryIO, TextIO
from re import match

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

def read_pattern(name: str) -> list[Sample]:
    pattern_file: TextIO = open(name + ".pat")
    pattern_data: list[str] = pattern_file.readlines()
    sample_list: list[Sample] = []
    for line in range(len(pattern_data)):
        pattern_data[line] = pattern_data[line].replace(" ", "")
        print(pattern_data[line])
        if match("\\d+:\\d+-\\d+", pattern_data[line]):
            sample_list.append(Sample(0, 0, 0))
        elif match("\\d+:\\d+/\\d+", pattern_data[line]):
            sample_list.append(Sample(0, 0, 0))
    print(pattern_data)
    return sample_list