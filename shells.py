# ECE2524 | Homework 2, Problem 1 | Brandon Fairburn

with open('/etc/passwd', 'r') as f:
	for line in f:
		string = line.split(':') # split strings on line by ':' separators
		if string[1] != '*': # hide inactive accounts
			print "%s\t%s" %(string[0], string[6]), # give the output