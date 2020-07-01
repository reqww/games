import sys
sys.path.insert(0, '/main')

import pytest
import cards as cd

Card = cd.Card

@pytest.mark.xfail(raises=ValueError)
def test_card_create1():
	card = Card(1, 1, 1, 1)

@pytest.mark.xfail(raises=ValueError)
def test_card_create2():
	card = Card(1, "OVAL", "OVAL", "OVAL")
	
@pytest.mark.xfail(raises=ValueError)
def test_card_create3():
	card = Card(1, "OVAL", "STRIPPED", "OVAL")

@pytest.mark.xfail(raises=ValueError)
def test_card_create4():
	card = Card(1, "OVAL", "STRIPPED", "RED")

x = [
	Card(1, 'SQUIGGLE', 'STRIPPED', 'PURPLE'),
	Card(2, 'OVAL', 'OPEN', 'RED'),
	Card(1, 'OVAL', 'SOLID', 'PURPLE')
]

y = [
	Card(1, 'SQUIGGLE', 'STRIPPED', 'GREEN'),
	Card(2, 'SQUIGGLE', 'SOLID', 'RED'),
	Card(2, 'DIAMOND', 'SOLID', 'GREEN')
]

z = [
	Card(3, 'DIAMOND', 'SOLID', 'RED'),
	Card(3, 'SQUIGGLE', 'STRIPPED', 'PURPLE'),
	Card(1, 'SQUIGGLE', 'SOLID', 'RED')
]

cd.check_set(z)

def test_set1():
	assert cd.check_set(x) == False

def test_set2():
	assert cd.check_set(y) == False


def test_set3():
	assert cd.check_set(z) == False

