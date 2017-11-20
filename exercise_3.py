def handle_list_of_tuples(list_of_tuples):
	new_list = sorted(list_of_tuples, key = lambda x : (x[0], -int(x[1]), -int(x[2]), -int(x[3])))
	return new_list
