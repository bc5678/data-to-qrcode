import sys
import string
import random

def generate(size):
	f = open('random.txt', 'w')
	for i in range(size):
		f.write(random.choice(string.ascii_letters))

	f.close()

#generate(int(sys.argv[1]))
