#!/bin/python3

import os
#1. Display the OS version on Linux.
os.system("uname -a ")
print()
#2. Display the private IP address, 
print ("Your Private IP address is: ")
os.system("ifconfig | sed -n 2p | awk '{print $2}'")
print()
#public IP address, and 
print ("Your Public IP address is: ")
os.system("curl -s ifconfig.me ")
print()
#the default gateway.
print ("Your Default gateway address is: ")
os.system("route -n | sed -n 3p | awk '{print $2}'")
print()

#3. Display the hard disk size; free and used space
print ("Your hard disk size; free and used space: ")
os.system("df -H")
print()

#4. Display the top five (5) directories and their size
#Note: You can do a quick google search on this.
os.system("cd / && du -sh * 2>/dev/null | sort -rh | head -5")
print()

#5. Display the CPU usage; refresh every 10 seconds.
os.system("sar -u 10 5")

#note -u is an option to refresh the CPU usage every 10 seconds. And 5 is for the count.
#Usage: sar [ options ] [ <interval> [ <count> ] ]



