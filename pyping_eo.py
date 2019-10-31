#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  pyping_eo_v0.1.py
#  
#  Copyright 2016 Erik Ostrom <eostrom@sti>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import sys, getopt, time
from os import system
from random import randint
def main(argv):
	global green
	global yellow
	global red
	global white
	green = "\033[1;32m"
	yellow = "\033[1;33m"
	red = "\033[1;31m"
	white = "\033[0;37m"
	print("Pinging ", end="")
	#print(argv[-1])
	if len(argv) > 1:
		for i in argv[1:-1]:
			print(i+", ", end="")
	print(argv[-1])
	print("Starting loop...")
	while True:
		for i in argv[1:]:
			eo_ping(i)
		sleep_time = 1
		print("Pings complete. Sleeping for "+str(sleep_time)+" seconds...")
		time.sleep(sleep_time)
		print("Starting over...")
		time.sleep(1)
	return 0


#ping a given host. if host appears down, ping again.
#print results
def eo_ping(host):
	result = system("ping -c 1 -w 1 " + host + " > /dev/null 2>&1")
	if result != 0:
		printcolor("WARN", yellow)
		print("["+thetime()+"] "+ "The last ping of "+ str(host) +" failed. Trying again...")
		result = system("ping -c 1 -w 5 " + host + " > /dev/null 2>&1")
	if result == 0:
		printcolor("OK", green)
		print("["+thetime()+"] "+ str(host) +" appears to be UP.")
		return result
	if result != 0:
		printcolor("ERROR", red)
		print("["+thetime()+"] "+ str(host) +" appears to be DOWN.")
		return result

#print [string] in a certain color, doesnt print \n
def printcolor(string, color):
	print("["+color+string+white+"] ",end="")

def thetime():
	return time.strftime("%m/%d/%y %H:%M.%S")

if __name__ == '__main__':
    sys.exit(main(sys.argv))
