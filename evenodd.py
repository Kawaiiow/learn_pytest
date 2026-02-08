"""Even odd module"""

def is_even_odd(n : int) -> str:
	"""Function to print is the number is even or odd"""
	return "Even" if not (n % 2) else "Odd"

if __name__ == "__main__":
	num = int(input("Enter a Number: "))
	print(is_even_odd(num))
