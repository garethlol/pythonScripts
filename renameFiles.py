#!/usr/bin/env python

# This python script changes fileNames that start with
# a certain string to be renamed without them
# @author Gareth Ng

import os

print "Enter fileName to be changed/removed from all files in current directory"
prompt, filesFoundFlag, numFilesFound, filename = ('> ', False, 0, 0)
nameToRemove = raw_input(prompt)

for filename in os.listdir("."):
	if filename.startswith(nameToRemove):
		try:
			os.rename(filename, filename[len(nameToRemove):])
			filesFoundFlag, numFilesFound = (True, numFilesFound + 1)
		except (WindowsError,OSError):
			print "Error renaming %s to %s" % (filename, filename[len(nameToRemove):])
			print "%s skipped" % (filename)

if filesFoundFlag is True:
	print "%d files found, all file(s) changed without %s" % (numFilesFound, nameToRemove)
else:
	print "No files found that started with %s" % nameToRemove

print "Exiting script... Thank you!"