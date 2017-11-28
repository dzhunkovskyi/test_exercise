def handle_number(number1, number2, number3):
	list_of_numbers = [i for i in range(number1, number2+1) if i%number3 == 0]
	return len(list_of_numbers)

#Some comment new
