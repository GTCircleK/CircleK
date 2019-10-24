import os
from sys import argv

while True:
	folder = input('Enter folder name: ')
	directory = 'D:\CircleK\images\Pictures' + "\\" + folder
	output = "'" + folder + "': ["

	for filename in os.listdir(directory):
		if filename.lower().endswith('.jpg') or filename.lower().endswith('.jpeg'):			
			print (filename)
			output += "'" + filename + "',"
			
	print (output)