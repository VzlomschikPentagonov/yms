from re import match

#constants

VAL_TYPES_2: tuple = (int(), float(), int(), int(),
                      float(), int(), int())

#functions2

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
        if match("\\d.+:\\d.*-\\d.*", s):
            
    print(pattern_data)
    return []

  #classes
class Sample:
    def __init__(self, note: c_uint8 = 69,
                 start: c_uint16 = 0,
                 length: c_uint16 = 0):
        self.note = note
        self.start = start
        self.length = length
  #_Field: ctype | pytype = CONST_VAL
  #Example: tempo: c_float | float = TEMPO_DEFAULT
