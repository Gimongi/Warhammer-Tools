list1D = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list2D = [
	[4, 5, 6, 6, 6, 6, 6, 6, 6, 6],
	[3, 4, 5, 6, 6, 6, 6, 6, 6, 6],
	[2, 3, 4, 5, 6, 6, 6, 6, 6, 6],
	[2, 2, 3, 4, 5, 6, 6, 6, 6, 6],
	[2, 2, 2, 3, 4, 5, 6, 6, 6, 6],
	[2, 2, 2, 2, 3, 4, 5, 6, 6, 6],
	[2, 2, 2, 2, 2, 3, 4, 5, 6, 6],
	[2, 2, 2, 2, 2, 2, 3, 4, 5, 6],
	[2, 2, 2, 2, 2, 2, 2, 3, 4, 5],
	[2, 2, 2, 2, 2, 2, 2, 2, 3, 4]
];


def wound():

	stren = raw_input("What is your strength? ")

	tough = raw_input("What is their toughness? ")


	if int(stren) in list1D and int(tough) in list1D:
		print str(list2D[int(stren) - 1][int(tough) - 1]) + "+ to hit."

	else:
		print "Invalid Data"
		wound()

while True:
	try:
		wound()

	except:
		print "Invalid Data, try again."
		pass