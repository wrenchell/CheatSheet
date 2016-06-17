#!/usr/bin/python

###############################################################################
 #
 # Bulletproofing script for user input.
 #
 # Copyright (C) 2016 June 17  Mitchell Thompson
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
import os


def testInt(x):
  error = 0
  chars = list(x)
  
  for i in chars:
    if (i > '9' or i < '0'):
      return 'false'

  return 'true'

def testStr(s):
  theChars = list(s)
  print theChars
  
  for ters in theChars:
    if (ters < '0' or (ters > '9' and ters < 'A') or ters > 'z' or ters == '@'):
      return 'false'
    
  return 'true'
   
