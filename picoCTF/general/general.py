from base64 import b85decode, b64decode, b32decode, b16decode


def decimal_to_binary(decimal):
    # bin(decimal)[2:]
    # or...

    rem = decimal % 2
    div = decimal // 2
    binary = str(rem)

    while div > 0:
        rem = div % 2
        binary = str(rem) + binary
        div //= 2
    
    return binary


def hex_to_decimal(hexadecimal):
    # return int(hexadecimal, 16)
    # or...

    hex_dict = {str(key): i for i, key in enumerate(list(range(10)) + list('ABCDEF'))}
    decimal = 0

    for i, hex_dig in enumerate(hexadecimal[::-1]): # move right to left
        try:
            dec = hex_dict[hex_dig] * 16 ** i
            decimal += dec
        except KeyError:
            break
    
    return decimal


def to_ascii(original, base=2, base64=False):
    if base64:
        try:
            if base==16:
                return b16decode(original).decode('utf-8')
            elif base==32:
                return b32decode(original).decode('utf-8')
            elif base==64:
                return b64decode(original).decode('utf-8')
            elif base==85:
                return b64decode(original).decode('utf-8')
            else:
                return "Specify [-b BASE] where BASE is 16, 32, 64, or 85."
        except Exception as e:
            return "Error: " + str(e)

    else:
        try:
            ordinal = int(original, base)
            return chr(ordinal)
        except OverflowError:
            return "Error: Could not convert due to signed integer exceeding maximum. Reduce input."
        except ValueError:
            return "Error: Could not convert due to base. Either change base or change input."

