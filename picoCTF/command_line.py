import argparse
import subprocess

from .cryptography.cryptography import decode_caeser, encode_caeser, \
                                create_table, decode_from_table, \
                                encode_from_table, decode_morse, encode_morse
from .general.general import decimal_to_binary, hex_to_decimal, to_ascii
from .forensics.stenography import lsb


def print_encoded_caeser_msg(plaintexts, offset, numeric=False):
    for text in plaintexts:
        code = encode_caeser(text, offset, numeric)
        print(code)


def print_decoded_caeser_msgs(codes, offset):
    for code_str in codes:
        msg = decode_caeser(code_str, offset)
        print(msg)


def print_encoded_table_msgs(plaintexts, filename, key):
    table = create_table(filename)
    for text in plaintexts:
        code = encode_from_table(text, key, table)
        print(code)


def print_decoded_table_msgs(codes, filename, key):
    table = create_table(filename)
    for code in codes:
        msg = decode_from_table(code, key, table)
        print(msg)        


def print_encoded_morse_msgs(plaintexts):
    for text in plaintexts:
        code = encode_morse(text)
        print(code)


def print_decoded_morse_msgs(codes):
    for code in codes:
        msg = decode_morse(code)
        print(msg)


def print_decimal_to_binary(decimals):
    for dec in decimals:
        binary = decimal_to_binary(dec)
        print(binary)


def print_hidden_msg(filenames):
    for f in filenames:
        subprocess.call(f"./picoCTF/forensics/forensics.sh {f}",shell=True)

    
def print_hex_to_decimal(hexadecimals):
    for h in hexadecimals:
        dec = hex_to_decimal(h)
        print(dec)


def print_to_ascii(originals, base, base64=False):
    for o in originals:
        asci = to_ascii(o,base,base64)
        print(asci)


def print_lsb_msg(filename, n_bits_str):
    try:
        n_bits = int(n_bits_str)
        msg = lsb(filename, n_bits)
        print(msg)
    except:
        print("Error: Second argument to [--lsb] must be an integer.")


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-d",
                        "--decode",
                        nargs='+',
                        type=str,
                        help="Decodes an encoded message (default: caeser cipher).")
    parser.add_argument("-e",
                        "--encode",
                        nargs='+',
                        type=str,
                        help="Encodes a plaintext message (default: caeser cipher).")
    parser.add_argument("-o",
                        "--offset",
                        type=int,
                        default=0,
                        help="Specifies the offset for encoding or decoding messages.")
    parser.add_argument("-db",
                        "--dec-to-binary",
                        nargs='+',
                        type=int,
                        help="Convert decimal number to its binary number.")
    parser.add_argument("-f",
                        "--find",
                        nargs=1,
                        type=str,
                        help="Finds the flag in a jpeg using 'strings' and 'grep'.")
    parser.add_argument("-hd",
                        "--hex-to-decimal",
                        nargs='+',
                        type=str,
                        help="Convert hexadecimal number to its decimal number.")
    parser.add_argument("-a",
                        "--ascii",
                        nargs='+',
                        type=str,
                        help="Convert binary/octal/hexadecimal/etc. number to its ascii character.")
    parser.add_argument("-b",
                        "--base",
                        type=int,
                        default=2,
                        help="Specifies the base to go with -a [--ascii] conversion.")
    parser.add_argument("--base64",
                        help="Specifies the encoding/decoding method is base64.",
                        action='store_true')
    parser.add_argument("-t",
                        "--table",
                        nargs=2,
                        type=str,
                        help="Specifies a table and key from which a messsage can be decoded/encoded.")
    parser.add_argument("-m",
                        "--morse",
                        help="Specifies the encoding/decoding method is morse.",
                        action='store_true')
    parser.add_argument("--lsb",
                        nargs=2,
                        type=str,
                        help="Specifies an image from which a hidden message can be found, and the number of bits to use in the least significant bit (lsb) algorithm.")
    parser.add_argument("-n",
                        "--numeric",
                        help="Encodes caeser cipher in numbers.",
                        action='store_true')

    args = parser.parse_args()

    if args.encode:
        if args.table:
            print_encoded_table_msgs(args.encode, *args.table)
        elif args.morse:
            print_encoded_morse_msgs(args.encode)
        else:
            print_encoded_caeser_msg(args.encode, args.offset, args.numeric)
            
    if args.decode:
        if args.table:
            print_decoded_table_msgs(args.decode, *args.table)
        elif args.morse:
            print_decoded_morse_msgs(args.decode)
        else:
            print_decoded_caeser_msgs(args.decode, args.offset)
    
    if args.dec_to_binary:
        print_decimal_to_binary(args.dec_to_binary)
    
    if args.find:
        print_hidden_msg(args.find)
    
    if args.hex_to_decimal:
        print_hex_to_decimal(args.hex_to_decimal)
    
    if args.ascii:
        print_to_ascii(args.ascii, args.base, args.base64)

    if args.lsb:
        print_lsb_msg(*args.lsb)
