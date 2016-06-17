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
class Generator():

  def gen(self, alphabet, panelNum):

    os.system("./Utils/clear.py")
    width = header.detect()
    header.display(width)

    os.chdir("Cheat_Sheets")
    self.letterList = alphabet
    
    projectName = raw_input("Enter the project name: ")
    cableNum = raw_input("Enter the number of cables used on the project: ")
    cableNumber = int(cableNum)
    projectName =  projectName.replace(" ","")
    projectName.strip() 
 
    os.mkdir(projectName)
    os.chdir(projectName)
    numOfPanels = cableNumber / 48
    numOfPanels += 2
    ActualPanels = numOfPanels - 2

    print "Generating...."
    
    for x in range(0, numOfPanels): 
      currentPanel = self.letterList[x]
      panelNumber = panelNum[x]
      panelStr = projectName + '_Panel_' + currentPanel + '.txt'
     

      try:
        fd = os.open(panelStr, os.O_RDWR|os.O_CREAT )
        out = os.fdopen(fd, 'r+')

      except IOError as err:
        print "I/O error ({0}): {1}".format(err.errno, err.strerror)
        sys.exit()

      out.write(currentPanel + ":")
      out.write("\n\n")
    
      firstNum = 1
      secondNum = 25
      
      for n in range(0,24):
        out.write('{:5}'.format(str(firstNum)) + '---' +                                '{:>5}'.format(str(panelNumber + firstNum)) + '{:>22}'.format('|') +            '{:22}'.format('|') + '{:5}'.format(str(secondNum)) + '---'  +                  '{:>5}'.format(str(panelNumber + secondNum)) + "\n")

        firstNum += 1
        secondNum += 1

    print "Done!"
    out.close()
    os.chdir(os.pardir)
    os.chdir(os.pardir)
