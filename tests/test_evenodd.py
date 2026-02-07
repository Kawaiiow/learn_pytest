from evenodd import is_even_odd

def test_even_number():
	assert is_even_odd(4) == "Even"

def test_odd_number():
	assert is_even_odd(3) == "Odd"

def test_zero():
	assert is_even_odd(0) == "Even"

def test_negative():
	assert is_even_odd(-2) == "Even"

def test_hidden1():
	assert is_even_odd(16) == "Even"
