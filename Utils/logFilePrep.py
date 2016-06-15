#!/usr/bin/python

###############################################################################
 #
 # Class to prepare to open the log file
 #
 # Author/copyright:  Mitchell Thompson
 # Date: 2016 May 07
 # 
##

import sys
import os
import time

complete = False

def prepStart():
  # Change working directory to main directory of 'Income'
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
 




