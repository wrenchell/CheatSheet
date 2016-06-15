#!/usr/bin/python

###############################################################################
 #
 # Script to detect the width of the terminal and print the header
 #
 # Copyright (C) 2016 June 14  Mitchell Thompson
 #
 # This program is free software: you can redistribute it and/or modify
 # it under the terms of the GNU General Public License as published by
 # the Free Software Foundation, either version 3 of the License, or
 # (at your option) any later version.
 #
 # This program is distributed in the hope that it will be useful,
 # but WITHOUT ANY WARRANTY; without even the implied warranty of
 # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 # GNU General Public License for more details.
 #
 # You should have received a copy of the GNU General Public License
 # along with this program.  If not, see <http://www.gnu.org/licenses/>.
 #
 ##

import sys
import fcntl
import termios
import struct


def detect():
  lines, cols = struct.unpack('hh', fcntl.ioctl(sys.stdout, termios.TIOCGWINSZ, '1234'))
  temp = '%d' % (cols)
  width = int(temp)
  return width
  
 
def display(size):
  os.system("cd ..")
  header = ""

  for x in range(0, size):
    header += ("#")

  header += ("\n #\n # Cheat Sheet Generator ver 0.0.1a\n #\n##\n")  
  print header



