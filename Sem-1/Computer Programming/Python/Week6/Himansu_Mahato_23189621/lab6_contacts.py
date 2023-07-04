def view_contacts(contacts):
	for i,j in enumerate(contacts):
		print("{} {:^10}{}".format(i+1, j[0], j[1] ))
	print("",end='\n\n') # Just for new lines

def add_contacts(contacts):
	print('-'*6,' add_contact ','-'*6,end='\n\n')
	username = input("Enter contact name: ")
	userid = input("Enter contact number: ")
	print(f"{username} - {userid} has been added into the contact.",end="\n\n")
	return contacts.append((username,userid))

def delete_contacts(contacts):
	print("-"*6," delete_contact ","-"*6)
	view_contacts(contacts)
	userid = int(input("Enter the ID of the contact to delete: "))
	for i,j in enumerate(contacts):
		if (i+1) == userid:
			print(f"Deleting: Record {userid} {j[0]} {j[1]}",end="\n\n")
			del contacts[i]
	return contacts

def main(contacts=[("Stish","123"),("Rita","321")]):
	choice = input("""Select an Operation
v view contacts
a add contacts
d delete contacts
q quit

Enter choice(v/a/d/q- to quit): """).lower()
	if choice == 'v':
		print('-'*6,' view_contacts ','-'*6,end='\n\n')
		view_contacts(contacts)
	elif choice == 'a':
		contacts = add_contacts(contacts)
	elif choice == 'd':
		contacts = delete_contacts(contacts)
	elif choice == 'q':
		print("-"*6," goodbye ","-"*6)
		exit()
	else:
		print("-"*6," invalid_choice ","-"*6)

if __name__ == "__main__":
	while True:
	 	main()

