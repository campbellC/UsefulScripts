UsefulScripts
===============
A few scripts to speed up productivity.
Do not use these scripts unless you understand them, I make no claims to their safety! I also have not packaged these up and they do have dependencies.

Each script's code should explain itself with comments. However, here's each scripts overview:




TODOGEN.pl
-------------
The purpose of this script is to search through a text file and find lines that end in "TODO: stuff to do" and record the stuff to do in a seperate file that records the line number where this TODO occurs.

directoryTree.py:
-------------------
This program is designed to build a graph of the directory structures of a given folder. If no argument is provided it takes the current directory as it's default.

timeSpent.py:
--------------
This program uses the history database created by Google Chome to tell you what websites you've been visiting in the past number of hours (default is 24). Currently it requires chrome to be closed to use it.

webBlock.pl:
--------------------
This script takes in website names and adds them to the /etc/hosts/ file, redirecting them to 127.0.0.1. In this way it blocks access to the websites from the machine. I have no idea if this works on anything other than OS X.
