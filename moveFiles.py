#!/usr/bin/env python

# Python script that will move all non-directory files in a directory and
# place them in a new directory associated with the current date and time
# @author Gareth Ng

import os, shutil
import time, datetime

# get today's date as a datetime type
# and later a string representation YYYY-MM-DD
todaystr = datetime.date.today().isoformat()  

prompt, directoryFoundFlag, numFilesFound, files = ('> ', False, 0, 0) 
print "Enter directory which files need to be moved"
inputDir = raw_input(prompt)
lookIn = "./" + inputDir

if os.path.exists(lookIn) is True:
	print "%s is a valid directory, moving all files accordingly" %(lookIn)

	destination = lookIn + "/" + todaystr
	os.mkdir(destination)
	print "Moving all files to a new folder %s" %(destination)
	print "--------------------------------"

	for files in os.listdir(lookIn):
		if(os.path.isdir(files) or os.path.isfile("movesFiles.py")):
			print "%s is a directory, will not be moved" %(files)
		else:
			try: 
				filePath = lookIn + "/" + files
				shutil.move(filePath,destination)
				numFilesFound = numFilesFound + 1
				print "%d) %s has been moved from current dir to %s" %(numFilesFound, files, destination)		
			except (IOError):
				print "%s cannot be moved" %(files)

	print "--------------------------------"
	print "%d files moved" %(numFilesFound)
else:
	print "%s directory does not exist, closing script" %(lookIn)

print "Exiting script... Thank you!"
