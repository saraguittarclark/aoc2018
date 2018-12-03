
def get_final_freq(numbers):
	n = 0
	for x in numbers:
		n = n + x
	return n

def get_first_duplicate(numbers):
	n = 0
	new_set = set()
	while True: 
		# print(n, len(new_set))
		for x in numbers:
			n = n + x
			if n in new_set:
				return n
			new_set.add(n)
		
# statement
def main():
	f = open('input.txt', 'r')
	lines = f.readlines()
	f.close()

	numbers = [int(s) for s in lines]

	final_freq = get_final_freq(numbers)
	print(final_freq) 

	first_duplicate = get_first_duplicate(numbers)
	print(first_duplicate)

if __name__ == "__main__":
	main()

