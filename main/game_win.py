def game_finished(x):
	if check_rows(x)[0] or check_columns(x)[0] or check_diagonals(x)[0]:
		k = find_winner(check_rows(x)[1], check_columns(x)[1], check_diagonals(x)[1])
	elif draw(x):
		k = -1
	else:
		k = 0
	return k

def find_winner(a, b, c):
	k = a
	if b != 0:
		k = b
	elif c != 0:
		k = c
	return k

def check(x):
	fl = True
	k = 0
	i = 0
	ans = []
	while fl and i < 2:
		if x[i] != x[i+1]:
			fl = False
		else:
			i += 1
	if not fl:
		ans.append(fl)
		ans.append(0)
	else:
		ans.append(fl)
		ans.append(x[i])

	return ans

def check_rows(x):
	i = 0
	while (i < 3) and (not check(x[i])[0]):
		arr = check(x[i])
		i += 1
	if i != 3:
		arr = check(x[i])
	return arr

def check_columns(x):
	j = 0
	while j < 3 and not check([x[0][j], x[1][j], x[2][j]])[0]:
		arr = check([x[0][j], x[1][j], x[2][j]])
		j += 1
	if j != 3:
		arr = check([x[0][j], x[1][j], x[2][j]])
	return arr

def check_diagonals(x):
	arr = [False, 0]
	if check([x[0][0], x[1][1], x[2][2]])[0]:
		arr = check([x[0][0], x[1][1], x[2][2]])
	elif check([x[0][2], x[1][1], x[2][0]])[0]:
		arr = check([x[0][2], x[1][1], x[2][0]])
	return arr

def draw(x):
	arr = []
	fl = False
	for i in range(3):
		arr.append(0 in x[i])
	if not (True in arr):
		fl = True
	return fl

x = [
	[1, 1, 2],
	[2, 2, 0],
	[2, 1, 0],
]

print(game_finished(x))