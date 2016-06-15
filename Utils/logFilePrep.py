#!/usr/bin/python

###############################################################################
 #
 # Script to prepare to open the log file
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

import sys
import os
import time

complete = False

def prepStart():
  # Change working directory to main directory of 'Cheat Sheet'
  os.system("cd ..")

  # Move the previous log file to the log archive and create a fresh one.
  sys.stderr.write("Moving old log file and creating a new one\n")

  currentTime = time.strftime("%Y_%j_%H:%M:%S")
  oldLogFile = "oldLogs/log" + currentTime + ".txt"
  sys.stderr.write(oldLogFile)

  logFileCommand = "cp log.txt " + oldLogFile
  os.system(logFileCommand)

  sys.stderr.write("\nOld log file copied to the archive. Removing from" + \
                   " current Dir\n")

  try:
    os.system("rm log.txt")
    os.system("touch log.txt")
  
    sys.stderr.write("New log file created.  All log out will now appear" + \
                     " in log.txt\n")
    
    complete = True
  except Exception as e:
  
    os.system("touch log.txt")

    sys.stderr.write("Removal of old log file failed, a new one should" + \
                     " have been created.  Double check everything.\n")

    complete = True

  return complete
 




