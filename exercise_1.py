def handle_number(number1, number2, number3):
	list_of_numbers = [i for i in range(number1, number2+1) if i%number3 == 0]
	print(list_of_numbers)
	return len(list_of_numbers)

print(handle_number(0, 10, 2))