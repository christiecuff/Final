class player():
	def __init__(self, pos, inventory, size, solution):
		self.pos = pos
		self.inventory = inventory
		self.inventorySize = size
		self.solution = solution

	def getDict(self):
		return {'pos':self.pos,'inv':self.inventory,'size':self.inventorySize,'solution':self.solution}
	
	def setPlayerFromDict(self, dict):
		self.pos = dict['pos']
		self.inventory = dict['inv']
		self.inventorySize = dict['size']
		self.solution = dict['solution']


Weapons = ['knife','pen']
Rooms = ['study','hallway','dining','kitchen','ballroom','library','bathroom','closet','living']
RoomOrder = [['kitchen','hallway','dining'],['library','ballroom','study'],['bathroom','living','closet']]
People = ['maid', 'cook', 'wife', 'butler']
Items = ['book','bucket','mop','music','keys']

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
#statements:
	if choice == "3":
		print('''Millie Parker has been a maid in the in the Henderson
house hold for 8 years. She took care of Josh henderson after his parents 
died in a car crash 2 years before he enharited the Henderson house.

Her statement reads: she was in the libary putting some book away that 
Mrs. Henderson gave her and after that she cleaned the libary. Then when to 
the kitchen talking to Elliot about the food he has preparded for Mr. Henderson
''')
		input('\t\t\t\t\t\tEnter to continue')

		print('''---------------------------------------------------------------------
''')

		print('''Georgis Valintine is new in the Henderson house hold. She 
started 2 months ago, still geting use to things around the house.

Her statement reads: Georgia was cleaning he master bedroom of Mrs. and Mr.
Henderson, when cleaning out she realized the safe was left open nothing was 
in there except for bunch of papers scartered eery where on the floor
''')
		input('\t\t\t\t\t\tEnter to continue')
		
		print('''---------------------------------------------------------------------
''')

		print('''Amina Bradford has been''')

#map:
	if choice == "4":
#inventory:
	if choice == "5":
		def printInventory():
			items = {}
			if len(player.inventory) > 0:
				print("Here is your inventory:")
					if item in items:
				for item in player.inventory:
						items[item] = items[item] + 1
					else:
						items[item] = 1
				for item in items:
					print(item.capitalize() + ": " + str(items[item]))
			else:
				print("Your inventory is empty")

#items:
def addItem(item, count):
	if item.lower() in Items and len(player.inventory)+count <= player.inventorySize:
		for i in range(count):
			player.inventory.append(item.lower())
		print("Item(s) added to inventory")
	elif not item.lower() in Items:
		print('Item not found, here are the items available:')
		for item in Items:
			print(item.capitalize())
	elif len(player.inventory) > player.inventorySize:
		print('Iinventory is full')

def removeItem(item, count):
	if item in player.inventory:
		for i in range(count):
			player.inventory.remove(item)
		print("Item(s) removed from inventory")
	else:
		print("Item not in inventory")