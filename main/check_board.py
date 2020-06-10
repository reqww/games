def validate_board(x):
	fl = False
	if check_lens(x) and check_numbers(x):
		c1 = 0
		c2 = 0
		for arr in x:
			for el in arr:
				if el == 1:
					c1 += 1
				elif el == 2:
					c2 += 1
		if c1 == c2 or c1 == c2 + 1:
			fl = True

	return fl

def check_lens(x):
	fl = True
	if len(x) != 3:
		fl = False
	else:
		for arr in x:
			if len(arr) != 3:
				fl = False
				break
	return fl

def check_numbers(x):
	fl = True
	i, j = 0, 0
	while fl and i < 3:
		while fl and j < 3:
			if x[i][j] != 0 and x[i][j] != 1 and x[i][j] != 2:
				fl = False
			else:
				j += 1
		i += 1
	return fl

x = [
	[2, 1, 0],
	[0, 1, 2],
	[2, 1, 1],
]

print(validate_board(x))
