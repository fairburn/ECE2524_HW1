# ECE2524 | Homework 2, Problem 2 | Brandon Fairburn

# import sys to allow argument handling
import sys
argv = sys.argv
argc = len(argv)
filename = argv[1]

# make sure user gave proper command line input
if argc != 2:
	print "usage: python blacksburg.py FILENAME\nShow account information for Blacksburg residents."
	quit()
	
print "ACCOUNT INFORMATION FOR BLACKSBURG RESIDENTS"
with open(filename, 'r') as f:
	for line in f:
		string = line.split()
		
		# easier to read variables
		firstname = string[0]
		lastname = string[1]
		amount_owed = string[2]
		city = string[3]
		phone = string[4]
		
		# only show member information if city of residence is Blacksburg
		if city == "Blacksburg":
			print "%s, %s, %s, %s" %(phone, lastname, firstname, amount_owed)