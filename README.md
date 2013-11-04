cronpurge -- Mac OS Memory Management Script
============================================

USAGE INSTRUCTIONS:

Simply add a line such as the one below to your crontab using the "crontab -e" command. Make sure the script is in a system-executable location, such as root (/) or user home (~/), with appropriate permissions (using chmod).

*/10 * * * * python /purge_script.py > ~/Desktop/log.txt

The above line will move Inactive memory from RAM to Free memory using OS X "purge" command every ten minutes on 0:00, 0:10, 0:20,...,0:n0.

Basically, the script move unusable Inactive Memory to usable Free Memory. If you are a Mac user who tends to jump around to many different applications, this script can result in significant speedup by avoiding memory thrashing or swap usage.

REQUIRES:

Xcode v4.x Command Line Tools or greater (earlier versions are untested).
Python v2.x or greater (earlier versions are untested).
