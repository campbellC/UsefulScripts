UsefulScripts
===============
A few scripts to speed up productivity.
Do not use these scripts unless you understand them, I make no claims to their safety! I also have not packaged these up and they do have dependencies.

Each script's code should explain itself with comments. However, here's each scripts overview:




todoGenerator
-------------
The purpose of this script is to search through a text file and find lines that end in "TODO: stuff to do" and record the stuff to do in a seperate file that records the line number where this TODO occurs. It also works on directories and has options for recursing through them etc.

directoryTree.py:
-------------------
This program is designed to build a graph of the directory structures of a given folder. If no argument is provided it takes the current directory as it's default.

timeSpent.py:
--------------
This program uses the history database created by Google Chome to tell you what websites you've been visiting in the past number of hours (default is 24). Currently it requires chrome to be closed to use it.

webBlock:
--------------------
This script takes in website names and adds them to the /etc/hosts/ file, redirecting them to 127.0.0.1. In this way it blocks access to the websites from the machine. I have no idea if this works on anything other than OS X.

thiefSnapper.py:
--------------------
This script when run will take a picture through the webcam and write it to disk, currently set to be in dropbox. Using sleepwalker and launchctl you can set this to happen automatically and perhaps get images of anyone using your laptop.

cropBook.sh:
--------------------
In conjunction with splitter.py and joiner.py, and relying on briss (http://briss.sourceforge.net/) this script allows you to crop pdf books for use on an ereader. As far as I know briss does not work well with "book" style latex files, where pages alternate their adjustment, this script works around this by splitting the pdfs in half, cropping, and then remerging them.
