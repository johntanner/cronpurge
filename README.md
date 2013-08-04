cronpurge
=========

Mac OS Memory Management Script

TO USE:

Simply add a line such as the one below to your crontab using the "crontab -e" command. Make sure the script is in a system-executable location, such as root (/) or user home (~/), with appropriate permissions (using chmod).

*/10 * * * * python /purge_script.py > ~/Desktop/log.txt

The above line will move Inactive memory from RAM to Free memory using OS X "purge" command. This is perfectly safe, and I have been using it myself for the past year or so.

DEPENDENCIES:
Xcode 4.x (other versions may work)
