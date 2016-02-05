#!/usr/bin/env python
import os.path 
# Define a filename.
filename = "example1.py"
if not os.path.isfile(filename):
	print "File doesn't exist as far as we can tell."
else:	
	# Open the file as f.
	# The function readlines() reads the file.             
	with open(filename) as f:
	    content = f.read().splitlines()
 
# Show the file contents line by line.
# We added the comma to print single newlines and not double newlines.
# This is because the lines contain the newline character '\n'. 
for line in content:
    print line,

print "\n"
fillername2 = "newfile.txt"
myfile=open(fillername2,'w')
myfile.write("\nWriting to the file first\n")
myfile.close()
print "The file closed"


