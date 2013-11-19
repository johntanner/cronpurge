#!/usr/bin/env python

import os, psutil

memory_before = psutil.virtual_memory().inactive
cpu_usage = psutil.cpu_percent(interval = 1)

if memory_before >= 200000000:

	if cpu_usage < 99:
		os.system("purge")
		memory_after = psutil.virtual_memory().inactive

		if memory_after >= 200000000:
			print "Unable to free memory."

		elif memory_after < 200000000:
			print "Total inactive memory freed: " + str((memory_before - memory_after) / 1000000) + "MB."

	else:
		print "CPU usage was " + str(cpu_usage) + "%."

else: 
	print "Enough free memory available."

