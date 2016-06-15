#!/usr/bin/python

# Clear the screen and return the cursor to the top left of the terminal

import sys

def clear() :
	"""Clear screen, return cursor to top left"""
	sys.stdout.write('\033[2J')
	sys.stdout.write('\033[H')
	sys.stdout.flush()

clear()
