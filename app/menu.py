#!/usr/bin/python

###############################################################################
 #
 # Class to display the menu to start the Generator
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
class Menu():

  def display(self):

    print "Choose an option: "
    print "1.  Generate for a new project"
    print "2.  View License"
    print "3.  Clean program files"
    print "4.  Exit\n"

    choice = raw_input("Selection: ")

    return choice
