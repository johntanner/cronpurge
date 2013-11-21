cronpurge -- Mac OS Memory Management Script
============================================

USAGE INSTRUCTIONS:

Simply add a line such as the one below to your crontab using the "crontab -e" command. Make sure the script has appropriate execute permissions.

The line below will move Inactive memory from RAM to Free memory using OS X "purge" command every ten minutes on 0:00, 0:10, 0:20,...,23:n0.

*/10 * * * * python /purge_script.py > ~/Desktop/log.txt

Basically, the script move unusable Inactive Memory to the usable pool of Free Memory.
This script can help result in a significant speedup by avoiding page outs.

REQUIRES:

Xcode v4.x Command Line Tools or greater (earlier versions are untested).

Python v2.x or greater (earlier versions are untested).

psutil v1.1.x or greater (earlier versions are untested).
