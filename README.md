# A picoCTF helper tool
A Python package that aims to help picoCTF contestants in their quest to find all the flags.

## What is picoCTF?
[picoCTF](https://picoctf.org/) is a [Capture The Flag (CTF)](https://en.wikipedia.org/wiki/Capture_the_flag#Computer_security) cybersecurity hacking competition for middle and high school students, created by security experts at Carnegie Mellon University.

Partipants tackle a set of challenges from six domains of cybersecurity:
- General skills
- Cryptography
- Web exploitation
- Forensics
- Reverse Engineering
- Binary Exploitation

## Example use
Below are just four examples of how you might use this tool.
1. **Morse Code**: Decode a message
```bash
~ python3 -m picoCTF --decode ".... . .-.. .-.. ---" --morse
>>> hello
```
2. **Caeser cipher**: Decode a message
```bash
~ code="6 3 10 10 13"
~ python3 -m picoCTF --decode "$code" --offset 1
>>> hello
```
3. **Stenography**: Find a message hidden in the least significant bits of an image
```bash
~ python3 -m picoCTF --lsb picoCTF/forensics/buildings.png 1
>>> picoCTF{h1d1ng_1n_th3_b1t5}
```
4. **String search**: Find a message buried amongst unintelligible or obscure image/text files
```bash
~ python3 -m picoCTF --find picoCTF/forensics/garden.jpg
>>> picoCTF{more_than_m33ts_the_3y3eBdBd2cc}
```


## Getting started
After cloning, run:
```bash
cd pico-ctf
```

Now that you are in the root directory, you can use the helper tool as follows:
```bash
python3 -m picoCTF <options>
```

The following `options` are available:
```bash
--help						# shows options
--decode <morse code string> --morse		# decodes <morse code string>
--decode <string> --offset <int>		# decodes <string> using caeser cipher and offset <int>
--decode <string> --table <filepath> <key>	# decodes <string> using table at <filepath> and <key>
--encode <string> --morse    			# encodes morse code
--encode <string> --offset <int> 		# encodes <string> using caeser cipher and offset <int>
--encode <string> --table <filepath> <key>	# encodes <string> using table at <filepath> and <key>
--encode <string> --offset 1 --numeric 		# numerically encodes <string> using caeser cipher and 
						# offset <int>
--dec-to-binary <decimal int>			# converts <decimal int> to its binary number
--hex-to-decimal <hexadecimal>			# converts <hexadecimal> to its decimal number
--ascii <binary number> --base <int>    	# converts <binary number> to ascii chars in base <int>
--ascii <base64 sequence> --base <int> --base64 # converts <base64 sequence> to ascii chars in base <int>
--find <filepath>		  		# finds flags in the form picoCTF{...} from <filepath>
						# using strings and grep (unix commands)
--lsb <image filepath> <int> 			# finds messages hidden within <image filepath> using 
						# least significant bit algorithm with number of bits
						# as <int>
```

# License
[MIT](https://choosealicense.com/licenses/mit/)