#!/usr/bin/env python

# Python script that will move all non-directory files in a directory and
# place them in a new directory associated with the current date and time
# @author Gareth Ng

import time, datetime, os
import time
import shutil


today = datetime.date.today()  # get today's date as a datetime type

todaystr = today.isoformat()   # get string representation: YYYY-MM-DD
                               # from a datetime type.


print "Todays date is %s" %(todaystr)
print "Moving all files"

directoryFoundFlag, numFilesFound, files = (False, 0, 0)
os.mkdir(todaystr)

destination = "./" + todaystr


for files in os.listdir("."):
	if(os.path.isdir(files) or os.path.isfile("movesFiles.py")):
		print "%s is a directory, will not be moved" %(files)
	else:
		shutil.move(files,destination)
		print "%s has been moved from current dir to %s" %(files, destination)

print "End file transfer"
