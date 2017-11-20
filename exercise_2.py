def handle_string(value):
	count_letters = 0
	count_digits = 0
	for element in (value):
		if element.isalpha():
			count_letters+=1
		if element.isdigit():
			count_digits+=1
	return count_letters, count_digits

a, b = handle_string("Hello world! 123!")
print(a, b)
