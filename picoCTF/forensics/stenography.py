from PIL import Image
from ..general.general import to_ascii

def lsb(filename, n_bits=1):
    if n_bits < 1:
        raise ValueError("Error: Must be at least 1 least siginificant bit/digit.")

    image = Image.open(filename)
    pixels = image.load()

    extracted = "".join(["".join([bits[-n_bits] for bits in map(bin,pixels[x,0][:-1])]) for x in range(image.width)])

    return "".join([to_ascii(extracted[i:i+8],2) for i in range(0,len(extracted),8)])

    
