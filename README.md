# CheatSheet #
Generates cheat sheets for patch panels on job sites with 100+ cables.  Places
those cheat sheets into their own directory for the user to easily be able to 
print.


# Getting Started #

Unix-like systems:
Clone the repo and then get started.  Their shouldn't be anything else nessary
to set up.  

Windows:
Clone the repo.  Only a few changes need to be made to ensure sucessful runtime

1. Remove the fnclt import in header.py and change the detect() return value
   to 80.  Commit out the rest of the function.  

2. Change every instance of 'os.system('./Utils/clear.py') to 
   'os.system('python ./Utils/clear.py').  This should occur 3 times.
   Twice in the main and once in the Header.

3. 


# Prerequisities #

Python 2.7
 

# Installing #

You don't need to do anything but clone the repo.


# Running the tests #

Tests soon.


# Deployment #

No info needed


# Contributing #

Please read CONTRIBUTING.md for details on our code of conduct, and the process for submitting pull requests to us.


# Versioning #

We use SemVer for versioning.

Current Version: 0.1.0

# Authors #

Mitchell Thompson - Initial work

See also the list of contributors who participated in this project.


# License #

This project is licensed under the GNU Public License - see the LICENSE.md
file for details


# Acknowledgments #

Hat tip to PurpleBooth for the README Template


