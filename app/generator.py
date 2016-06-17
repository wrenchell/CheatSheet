#!/usr/bin/python

###############################################################################
 #
 # Class to actually generate the cheat sheets
 #
 # Copyright (C) 2016 June 16  Mitchell Thompson
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
import header
import error
class Generator():
  def gen(self, alphabet, panelNum):
    # Clear the terminal screen and display the header
    os.system("./Utils/clear.py")
    width = header.detect()
    header.display(width)

    # Get the list of letters for the patch panel
    self.letterList = alphabet
    
    # Prompt the user for the project name
    projectName = raw_input("Enter the project name: ")
    
    # Check to make sure that the project doesn't already exists
    os.chdir("app")
    
    e = open(".currentProjects.txt", 'rb')
    existing = e.read().splitlines()
    print existing 
    falseNum = 0
    new = 'false' 
    while new == 'false':
      for x in existing:
        if projectName == x:
          os.chdir(os.pardir)
          os.system("./Utils/clear.py")
          os.chdir("app")
          width = header.detect()
          header.display(width) 

          falseNum += 1

      if falseNum < 1:
        new = 'true'

      if new == 'false':
        os.chdir(os.pardir)
        os.system("./Utils/clear.py")
        os.chdir("app")
        width = header.detect()
        header.display(width)

        print projectName
        print "\nYou've entered the name of an existing project. Try again."
        projectName = raw_input("\nEnter the project name: ")
        falseNum = 0


    os.chdir(os.pardir)

    # Check the name the user submitted for symbols that would cause issues
    projectName =  projectName.replace(" ","")
    projectName.strip()
    nameCheck = error.testStr(projectName)
    
    if nameCheck == 'false':
      while nameCheck == 'false':
        os.system("./Utils/clear.py")
        width = header.detect()
        header.display(width)

        print "That name won't work.  No special characters.\n"

        projectName = raw_input("Enter the project name: ")
        projectName =  projectName.replace(" ","")
        projectName.strip()
        nameCheck = error.testInt(projectName)
        
    # Prompt the user for the number of cables used and check it for any non 
    # numerical character
    cableNum = raw_input("Enter the number of cables used on the project: ")
    cableCheck = error.testInt(cableNum)

    if cableCheck == 'false':
      while cableCheck == 'false':
        os.system("./Utils/clear.py")
        width = header.detect()
        header.display(width)
         
        print "You've entered an incorrect number.  Please try again."
        cableNum = raw_input("Enter the number of cables used on the project: ")
        cableCheck = error.testStr(projectName)

    
    # Change the cableNumber to an int. 
    cableNumber = int(cableNum)

    os.chdir("Cheat_Sheets") 
    os.mkdir(projectName)
    numOfPanels = cableNumber / 48
    numOfPanels += 2
    ActualPanels = numOfPanels - 2

    os.chdir(os.pardir)
    os.chdir("app")
    
    # Write the project name to the current projects list
    try:
      exist = open('.currentProjects.txt', 'a+')
    except IOError as err:
      print "I/O error ({0}): {1}".format(err.errno, err.strerror)
      sys.exit()
   
    exist.write(projectName)
    exist.write("\n")
    exist.close()

    os.chdir(os.pardir)
    os.chdir("Cheat_Sheets")
    os.chdir(projectName)
    print "\n\nGenerating...."
    
    # Here is where we actually generate the cheat sheets. Basically every 
    # patch panel is esotericly assigned a number.  That number is then used
    # to determin what cable should be assigned to 1 - 49 on that patch 
    # panel.  A = 0, B = 48, etc...
    for x in range(0, numOfPanels): 
      currentPanel = self.letterList[x]
      panelNumber = panelNum[x]
      panelStr = projectName + '_Panel_' + currentPanel + '.txt'
     
      # We need to open the directory for the project and then open the new
      # files for each patch panel.
      try:
        fd = os.open(panelStr, os.O_RDWR|os.O_CREAT )
        out = os.fdopen(fd, 'r+')

      except IOError as err:
        print "I/O error ({0}): {1}".format(err.errno, err.strerror)
        sys.exit()

      out.write(currentPanel + ":")
      out.write("\n\n")
    
     # Since we only want to write one output line, these represent each line 
     # of the cheat sheet.  1 - 24(two numbers on each line) to equal 48.
      firstNum = 1
      secondNum = 25
      
      # This is the heart of the algorythm.  Mostly string formatting, but if
      # you search, there is some math being done.  Loops once for every line
      # in the cheat sheet (0 - 24, or 25 times). Writes a line to file
      for n in range(0,24):
        out.write('{:5}'.format(str(firstNum)) + '---' +                                         '{:>5}'.format(str(panelNumber + firstNum)) +                                  '{:>22}'.format('|') + '{:22}'.format('|') +                                   '{:5}'.format(str(secondNum)) + '---' +                                        '{:>5}'.format(str(panelNumber + secondNum)) + "\n")

        firstNum += 1 
        secondNum += 1

    print "\n\nDone! Cheat Sheets were sucessfully generated!\n\n"
    raw_input("Press ENTER to continue...")
    # Close the output file and return to the owd
    out.close()
    os.chdir(os.pardir)
    os.chdir(os.pardir)
