print("\tMan's Homocide\n")
name = input(f'State your name:\n')

print('''Note: You are a detective investigating 
a crime that was commited 1 hour ago at the Henderson 
house hold. You have 7 supects.
''')
input('\t\t\t\t\tEnter to continue')

print('''Note: The victim's name was Josh Henderson. 
32 years old, a lawyer, he was found dead on the first floor in his study. 
The latest suspects: Millie Parker (maid), Georgia Valintine (maid), 
Amina Bradford (maid), Daisie Robies (cook), Elliot Yang (cook), 
Kelsey Henderson (wife) and Alfred Conley (butler)
''')
input('\t\t\t\t\t\tEnter to continue')

#Menu:
    choice = None  
while choice != "0":
	print \
	("""
	       Man's Homocide
	0 - Quit
	1 - Save
	2 - Load
	3 - Suspects statements
	4 - Map
	5 - Inventory
	""")

	choice = input("Option:\n")

#exit:
	if choice == "0":
		print("Good-bye.")


#getting help on saving and loading part
#saving:
    if choice == "1":
       if os.path.exists(os.getcwd() + name + ".dat"):
			overwrite = input("Save file exists, overwrite? [y/n]")
			if overwrite == "y":
				save(os.getcwd() + name + ".dat", player)
			elif overwrite == "n":
				newName == ""
				while not newName == name + ".dat":
					newName = input("Save name? ")
				save(os.getcwd() + newName, player)
		else:
			save(os.getcwd() + name + ".dat", player)
#loading:
    if choice == "2":
        location = input("Save file? ")
		if os.path.exists(os.getcwd() + location):
			player = load(os.getcwd() + location)
		else:
			print("Save not found!")
