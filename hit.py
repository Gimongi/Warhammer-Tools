list1D = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list2D = [
	[4, 4, 5, 5, 5, 5, 5, 5, 5, 5],
	[3, 4, 4, 4, 5, 5, 5, 5, 5, 5],
	[3, 3, 4, 4, 4, 4, 5, 5, 5, 5],
	[3, 3, 3, 4, 4, 4, 4, 4, 5, 5],
	[3, 3, 3, 3, 4, 4, 4, 4, 4, 4],
	[3, 3, 3, 3, 3, 4, 4, 4, 4, 4],
	[3, 3, 3, 3, 3, 3, 4, 4, 4, 4],
	[3, 3, 3, 3, 3, 3, 3, 4, 4, 4],
	[3, 3, 3, 3, 3, 3, 3, 3, 4, 4],
	[3, 3, 3 ,3 ,3, 3, 3, 3, 3, 4]
];


def Hit():
	
	youwep = raw_input("What is your weapon skill? ")

	theywep = raw_input("What is their weapon skill? ")


	if int(youwep) in list1D or int(theywep) in list1D:
		print str(list2D[int(youwep) - 1 ][int(theywep) - 1 ]) + "+ to hit."

	else:
		print "Invalid Data"
		Hit()

while True:
	try:
		Hit()

	except:
		print "Invalid Data, try again."
		pass