#!/usr/bin/python

###############################################################################
 #
 # Main class for the Cheat Sheet generating program.  Will mostly focous on 
 # housecleaning to begin with.  It will then mosltly delegate to other 
 # classes to preform the brunt of the work.
 #
 # Copyright (C) 2016 June 02  Mitchell Thompson
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

import os
import sys
import logFilePrep
import header
import alpha
import menu
import generator

# Change the working directory to the main directory of 'Cheat Sheet'
#os.chdir("CheatSheet")

# Call to logFilePrep to prepare to open the new logfile
print "Calling logFilePrep.py to clean and prepare the new log file.\n"

complete = logFilePrep.prepStart()
assert (complete == True), "Log File setup failed"

# Opening the file stream for the logfile
try:
  log = open('log.txt', 'r+')

  log.write("Beginning execution.  Opened logfile.\n\n")

except IOError as err:
  print "I/O error ({0}): {1}".format(err.errno, err.strerror)
  sys.exit()

# Generate the patch panel letters and numbers
log.write("Entering Alpha to generate patch panel letters and numbers\n")

theLetters = alpha.Alpha()
panelLetter, panelNum = theLetters.start()

log.write("Leaving Alpha\n")

# Clear the terminal to begin the main application
log.write("Logfile opening sucessful.  Clearing terminal to start main exe\n")
os.system("./Utils/clear.py")

# Run the script to display the header
log.write("Displaying header.  Entering Header.py\n")

width = header.detect()
header.display(width)

log.write("Leaving header\n")

# Run the menu and get the user selection
log.write("Entering menu.  Displaying the menu\n")

menuX = menu.Menu()
menuChoice = menuX.display() 

log.write("Leaving menu\n")

# Choose what to do after the menu selection is returned
if menuChoice == '1':
  log.write("User chose 1, entering generator")
  gen = generator.Generator()
  gen.gen(panelLetter, panelNum)
  log.write("Leaving generator")

if menuChoice == '2':
  os.system("view LICENSE")
if menuChoice == '3':
  sys.exit()

# Start all over again
while menuChoice != '3':
  os.system("./Utils/clear.py")
  header.display(width)
  menuX = menu.Menu()
  menuChoice = menuX.display()

  if menuChoice == '1':
    gen = generator.Generator()
    gen.gen(panelLetter, panelNum)
  if menuChoice == '2':
    print "Temp.  Menu Choice 2"


log.close()
