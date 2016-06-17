#!/usr/bin/python

###############################################################################
 #
 # Class to create the patch panel letters and assign a value to them.
 #
 # Copyright (C) 2016 June 15  Mitchell Thompson
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
class Alpha:

  def start(self):
    
    # Here we will generate all the variables for the possible patch pannel
    # letters.  We will also assign a value to seperate variables.
    
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O']
    alphabet += ['P','Q','R','S','T','U','V','W','X','Y','Z']
    
    for x in range(0, 25000):
        alphabet += ['Panel' + str(x)]
   
    panelNum = range(0, 25000, 48)

    return alphabet, panelNum

