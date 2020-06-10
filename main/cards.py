from random import randint

NUMBERS = [1, 2, 3]
SYMBOLS = ["DIAMOND", "SQUIGGLE", "OVAL"]
SHADINGS = ["STRIPPED", "SOLID", "OPEN"]
COLORS = ["RED", "GREEN", "PURPLE"]

class Card:
	def __init__(self, number, symbol, shading, color):

		if any([
			number not in NUMBERS,
			symbol not in SYMBOLS,
			shading not in SHADINGS,
			color not in COLORS
		]):
			raise ValueError("Неправильные параметры карты")

		self.number = number
		self.symbol = symbol
		self.shading = shading
		self.color = color

	def __str__(self):
		return (f"[{self.number}, '{self.symbol}', '{self.shading}', '{self.color}']")

def make_cards():
	cards = [
		Card(NUMBERS[randint(0,2)],
			SYMBOLS[randint(0,2)],
			SHADINGS[randint(0,2)],
			COLORS[randint(0,2)],
		) 
	for _ in range(3)]

	return cards

cards = make_cards()

def check_set(cards):
	a = set(card.number for card in cards)
	b = set(card.symbol for card in cards)
	c = set(card.shading for card in cards)
	d = set(card.color for card in cards)
	return check(a,b,c,d)

def check(a,b,c,d):
	arr = [a, b, c, d]
	k_3 = 0
	k_1 = 0
	for my_set in arr:
		if len(my_set) == 1:
			k_1 += 1
		elif len(my_set) == 3:
			k_3 += 1
	if k_3 == 1 and k_1 == 3:
		return True
	else:
		return False
		


