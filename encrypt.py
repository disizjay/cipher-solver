#!/usr/bin/python

import random
import string

abc = "abcdefghijklmnopqrstuvwxyz"

key = list(abc)
random.shuffle(key)
key = "".join(key)

text = open('plaintext_read.txt').read().lower()

trans = string.maketrans(abc, key)

f = open("encrypted.txt", "a")
f.write(text.translate(trans))
f.close()

#print text.translate(trans)
