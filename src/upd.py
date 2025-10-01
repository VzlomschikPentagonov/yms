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
  
  #classes
  
  #_Field: ctype | pytype = CONST_VAL
  #Example: tempo: c_float | float = TEMPO_DEFAULT
