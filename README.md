cronpurge
=========

Mac OS Memory Management Script

USAGE INSTRUCTIONS:

Simply add a line such as the one below to your crontab using the "crontab -e" command. Make sure the script is in a system-executable location, such as root (/) or user home (~/), with appropriate permissions (using chmod).

*/10 * * * * python /purge_script.py > ~/Desktop/log.txt

The above line will move Inactive memory from RAM to Free memory using OS X "purge" command every ten minutes on 0:00, 0:10, 0:20 ... 0:n0. What the script basically does is move unusable Inactive Memory to usable Free Memory. If you are not a heavy user of the system cache, this can result in significant speedup by avoiding "thrashing" [ http://en.wikipedia.org/wiki/Thrashing_(computer_science) ] or swap usage altogether.

REQUIRES:

Xcode 4.x Command Line Tools or greater (earlier versions may work).
Python 2.x or greater (earlier versions may work).
