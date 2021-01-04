#!/bin/bash
filename="$1"

strings -n 9 "$filename" | grep -o "picoCTF{.*}" 

# ~/andy/documents/misc/picoctf/forensics >>> chmod +x forensics.sh
# ~/andy/documents/misc/picoctf/forensics >>> ./forensics.sh garden.jpg
# picoCTF{more_than_m33ts_the_3y3eBdBd2cc}

# or with hexedit:
# ~/andy/documents/misc/picoctf/forensics >>> hexedit garden.jpg
# then, in the editor, press TAB and ctrl-s to search forward through the
# ascii strings. Search "Here is a flag" or "picoCTF{".