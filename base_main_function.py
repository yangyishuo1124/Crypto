

def str_ascii(string):
    string_ascii = ''
    for i in range(len(string)):
        string_ascii += str(ord(string[i]))
        if i == len(string) - 1:
            break
        string_ascii += ' '
    return string_ascii


def ascii_bin(string_ascii: str):
    string_ascii_bin = ''
    aaa = string_ascii.split(' ')
    # string_ascii = string_ascii.split(' ')
    for i in range(len(aaa)):
        string_ascii_bin += str(bin(int(aaa[i]))[2:])
        if i == len(aaa) - 1:
            break
        string_ascii_bin += ' '
    return string_ascii_bin


def bin_hex(string_ascii_bin_hex: str):
    string_ascii_bin = ''
    aaa = string_ascii_bin_hex.split(' ')
    for i in range(len(aaa)):
        string_ascii_bin += str(hex(int(aaa[i]))[2:])
        if i == len(aaa) - 1:
            break
        string_ascii_bin += ' '
    return string_ascii_bin


def bin_dec(string_ascii_bin:str):
    string_ascii = ''
    a = string_ascii_bin.split(' ')
    for i in range(len(a)):
        string_ascii += str(int(a[i], 2))
        if i == len(a)-1:
            break
        string_ascii += ' '
    return string_ascii


def ascii_str(string_ascii:str):
    string = '' 
    a=string_ascii.split(' ')
    for i in range(len(a)):
        string += chr(int(a[i]))
    return string


def hex_bin(a: str):
    aa = ''
    aaa = str(a,encoding='utf8').split(' ')
    for i in range(len(aaa)):
        aa += str(int(aaa[i], 16))
        if i == len(aaa)-1:
            break
        aa += ' '
    return aa
