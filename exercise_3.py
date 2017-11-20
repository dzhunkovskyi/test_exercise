list_of_tuples = [
    ("Tom", "19", "167", "54"), 
    ("Jony", "24", "180", "69"),
    ("Json", "21", "185", "75"), 
    ("John", "27", "190", "87"), 
    ("Jony", "24", "191", "98"), 
    ]

def handle_list_of_tuples(list_of_tuples):
	new_list = sorted(list_of_tuples, key = lambda x : (x[0], -int(x[1]), -int(x[2]), -int(x[3])))
	return new_list

print(handle_list_of_tuples(list_of_tuples))