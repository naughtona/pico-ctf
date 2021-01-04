# A picoCTF helper tool
A Python package that aims to help picoCTF contestants in their quest to find all the flags.

## What is picoCTF?
picoCTF is a Capture The Flag (CTF) cybersecurity hacking competition for middle and high school students, created by security experts at Carnegie Mellon University.

Partipants tackle a set of challenges from six domains of cybersecurity:
- General skills
- Cryptography
- Web exploitation
- Forensics
- Reverse Engineering
- Binary Exploitation

## Example use
The below example demonstrates how you use this tool to decode some caeser cipher.
```bash
~ code="13 25 5 24 1 13 16 12 5"
~ python3 -m picoCTF --decode "$code" --offset -1
myexample
```

## Getting started
After cloning, run:
```bash
python3 -m picoCTF <commands>
```

The following options are available:
```bash
--help    # shows options
--decode ".... . .-.. .-.. ---" --morse    # decodes morse code
--decode qwerty --offset 1    # decodes "qwerty", assumed to be caeser cipher and offset/shifted by 1
--decode qwerty --table picoctf/cryptography/table.txt solvecrypto    # decodes "qwerty" given table.txt and key "solvecrypto" 
--encode hello --morse    # encodes morse code
--encode hello --offset -1    # encodes "hello", assumed to be caeser cipher and offset/shifted by -1
--encode hello --table picoctf/cryptography/table.txt solvecrypto    # encodes "hello" given table.txt and key "solvecrypto"
--encode myexample --offset 1 --numeric    # encodes "myexample" in numbers, assumed to be caeser cipher and offset/shifted by 1
--dec-to-binary 10    # converts decimal 10 to its binary number
--hex-to-decimal 0x1F    # converts hexadecimal 0x70 to its decimal number
--ascii 1010010 --base 2    # converts binary number to ascii characters
--ascii TWFu --base 64 --base64    # converts "TWFu" from base64 encoding to ascii characters
--find picoctf/forensics/garden.jpg    # finds any flags in the form picoCTF{....} from garden.jpg using strings and grep (unix commands)
--lsb picoctf/forensics/buildings.png 1    # finds any messages hidden within buildings.png using least significant bit
```

# License
[MIT](https://choosealicense.com/licenses/mit/)