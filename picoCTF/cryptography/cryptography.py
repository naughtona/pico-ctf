from string import ascii_lowercase
import re

MORSE = {
    'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.',
    'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.',
    'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 'U':'..-',
    'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..', 
    '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....', 
    '6':'-....', '7':'--...', '8':'---..', '9':'----.', '0': '-----'
}


def decode_caeser(encoded_str, offset):
    alphabet = ascii_lowercase

    try: # encoded_str is like: "1 2 3 4 5"
        numbers = list(map(int,encoded_str.split()))
    except ValueError: # encoded_str is like: "qwerty"
        numbers = [alphabet.index(l) for l in encoded_str if l in alphabet]

    return "".join([alphabet[(n+offset)%26] for n in numbers])


def encode_caeser(plaintext, offset, numeric=False):
    alphabet = ascii_lowercase
    if numeric:
        return " ".join([str(alphabet.index(l) + offset) for l in plaintext.lower()])
    else:
        return "".join([alphabet[(alphabet.index(l) + offset)%26] for l in plaintext.lower()])


def create_table(filename):
    fh = open(filename, "r")
    plains = fh.readline().split()
    fh.readline() # throwaway format line
    rows = [row.replace('|','').split() for row in fh.readlines() if row.split() != []]
    fh.close()

    pad = [row[0] for row in rows]
    vals = [row[1:] for row in rows]
    table = {(x,y): vals[i][j] for j,y in enumerate(pad) for i,x in enumerate(plains)}
    return table


def decode_from_table(code, key, table):
    get_plain = lambda table, code, key: next(k[1] for k,v in table.items() if k[0] == key and v == code)

    return "".join([get_plain(table,c,k) for c,k in zip(code,key)])


def encode_from_table(plaintext, key, table):
    return "".join([table[(k,p)] for (k,p) in zip(key.upper(),plaintext.upper())])


def decode_morse(code):
    rgx = re.compile(r'\.|\-|\s')
    processed_code = "".join(rgx.findall(code)).split()
    try:
        return "".join([next(k for k,v in MORSE.items() if v==c) for c in processed_code]).lower()
    except:
        return "Error: code includes foreign morse. Try again."


def encode_morse(plaintext):
    return " ".join([MORSE[l] for l in plaintext.upper()])