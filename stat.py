# ECE2524 | Homework 2, Problem 3 | Brandon Fairburn

# import sys to allow argument handling
import sys
argv = sys.argv
argc = len(argv)
filename = argv[1]

# make sure user gave proper command line input
if argc != 2:
	print "usage: python stat.py FILENAME\nShow account statistics."
	quit()
	
total = 0.0 # total money 
count = 0 # keep track of how many people owe you money
max = float("-inf") # make it easy to set the first max and min
min = float("inf")
with open(filename, 'r') as f:
	for line in f:
		string = line.split()
		
		# manage variables
		lastname = string[1]
		amount = float(string[2])
		
		# test for max and min
		if amount > max:
			max = amount
			maxname = lastname
		
		if amount < min:
			min = amount
			minname = lastname
		
		# add amount to total
		total += amount
		
		count += 1
		
average = total / count # calculate average amount owed
print "ACCOUNT SUMMARY"
print "Total amount owed =", total
print "Average amount owed =", average
print "Maximum amount owed =", max, "by", maxname
print "Minimum amount owed =", min, "by", minname