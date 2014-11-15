###############################################################################
# Grand Theft Audio Radio Shuffler
#
# By Matthew Mettler
#
# In Grand Theft Auto III for PC, there is a custom radio feature, that lets 
# you play any MP3's you want in-game on the car radio. However, I noticed that
# it doesn't shuffle the songs; it chooses a random start point, and plays from 
# that point forward. The order depends on the filenames of the MP3's in the 
# folder, so this program reads those names, makes sure they have my custom
# numbering system (seen with ---), and then renames and shuffles them with new
# numbers, so that the order of songs is fresh each time I run this script.
###############################################################################

import os
from glob import glob
import random
radio_path = 'C:\Games\GTAIII\mp3\*.mp3'

def add_numbers():
	songs = glob(radio_path)
	count = sum(1 for x in songs if ("---") in x)
	#print(count)
	for item in songs:
		if not "---" in item:
			count += 1
			new_title = "{0}\\{1}---{2}".format('\\'.join(item.split("\\")[:-1]), str(count), item.split("\\")[-1])
			print("Renaming " + item)
			os.rename(item, new_title)

def shuffle():
	#assumes all songs are properly named
	songs = glob(radio_path)
	print(songs)
	numbers = range(1,len(songs)+1)
	random.shuffle(numbers)
	print(numbers)
	for item in range(len(songs)):
		print(item)
		new_title = "{0}\\{1}---{2}".format('\\'.join(songs[item].split("\\")[:-1]), numbers[item], songs[item].split("---")[-1])
		print("Renaming to " + new_title)
		os.rename(songs[item], new_title)

def main():
	add_numbers()
	shuffle()

if __name__ == "__main__":
    main()
