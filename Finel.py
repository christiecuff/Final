from time import sleep
from random import randint
import pickle
import os
import numpy
#Description: Prints text at designated speed

#Arguments:
#	text: Text to print
#	delay(Seconds): delay between characters, default:0.005 seconds
def slowPrint(text, delay=0.005):
	for i in text:
		print(i, end='', flush=True)
		sleep(delay)
	print('')

		
#Description: Print map in primitive format		

#Arguments:
#	map: 2 Dimensional Array of a map of place...Prints room names in position
#Returns:
#	None
def printMap(map):
	for level in map:
		for room in level:
			print(room + "; ", end='', flush=True)
		print("\n", end='', flush=True)
	print('\n You are in the ' + printRoom())
	print('------------------------------------------ \n')

def printRoomMap(file):
	file = open(file, 'r').read()
	slowPrint(file)

#Description: Return option selected by user from list

#Arguments: 
#	options: List of strings of the options
#	questionText: Text to be printed when selecting
#	name: Boolean whether you want object or position to be returned
#Return:
#	String value of selected option
def pickOption(options, questionText, name=True):
	for i, o in enumerate(options):
		slowPrint(str(i+1) + ": " + o + "\n")
	failed = True
	while failed:
		printed = False
		try:
			optionSelected = int(input(questionText + ": "))
		except:
			slowPrint("Invalid selection!")
			printed = True
		if optionSelected > 0 and optionSelected <= len(options):
			failed = False
			if name:
				return options[optionSelected-1]
			else:
				return optionSelected-1
		elif not printed:
			slowPrint("Invalid selection!")


class player():
	#Description: Get a dictionary of the current player information

	#Arguments:
	#	None
	#Returns:
	#	Dictionary of player: 
	#		'pos': Position of player
	#		'inv': Current inventory
	#		'size': Player maximum inventory size
	#		'solution': Player game solution
	def getDict(self):
		return {'pos':self.pos,'inv':self.inventory,'size':self.inventorySize,'solution':self.solution}

	#Description: Set player information from a dictionary

	#Arguments:
	#	dict: Dictionary to load character into
	def setPlayerFromDict(self, dict):
		self.pos = dict['pos']
		self.inventory = dict['inv']
		self.inventorySize = dict['size']
		self.solution = dict['solution']

	#Description: Move current position of player in one of 4 directions

	#Arguments:
	#	dir: Direction to move player in: up, down, left, right
	#Returns:
	#	None
	def move(self, dir):
		if dir == 'right' and player.pos[1] < 2:
			player.pos[1] += 1
		if dir == 'left' and player.pos[1] > 0:
			player.pos[1] -= 1
		if dir == 'up' and player.pos[0] < 2:
			player.pos[0] += 1
		if dir == 'down' and player.pos[0] > 0:
			player.pos[0] -= 1

	#Description: Add item(s) to inventory

	#Arguments:
	#	item: Item to add to inventory
	#	count: Amount of item to add to inventory
	def addItem(self, item, count):
		if item.lower() in Items and len(player.inventory)+count <= player.inventorySize:
			for i in range(count):
				player.inventory.append(item.lower())
			slowPrint("Item(s) added to inventory")
		elif not item.lower() in Items:
			slowPrint('Item not found, here are the items available:')
			for item in Items:
				slowPrint(item.capitalize())
		elif len(player.inventory) > player.inventorySize:
			slowPrint('Iinventory is full')

	#Description: Remove item(s) from inventory

	#Arguments:
	#	item: item to remove from inventory
	#	count: amount of items to remove
	#Returns:
	#	None
	def removeItem(self, item, count):
		if item in player.inventory:
			for i in range(count):
				player.inventory.remove(item)
			slowPrint("Item(s) removed from inventory")
		else:
			slowPrint("Item not in inventory")
		
	#Description: Prints the contents of the inventory

	#Arguments:
	#	None
	#Returns:
	#	None
	def printInventory(self):
		items = {}
		if len(player.inventory) > 0:
			slowPrint("Here is your inventory:")
			for item in player.inventory:
				if item in items:
					items[item] = items[item] + 1
				else:
					items[item] = 1
			for item in items:
				slowPrint(item.capitalize() + ": " + str(items[item]))
		else:
			slowPrint("Your inventory is empty")

	#Description: Return rooms in 4 directions around position

	#Arguments
	#	pos: Position to look at, default: current player position
	#Returns:
	#	Dictionary of 4 directional rooms: 
	#		'up': Room above position
	#		'down': Room below position
	#		'left': Room to the left of position
	#		'right': Room to the right of the position
	def nearbyRooms(self, pos=None):
		if pos == None:
			pos = self.pos
		levels = len(RoomOrder)
		currentLevelLen = len(RoomOrder[pos[0]])
		right,left,up,down = None,None,None,None
		if pos[1]+1 <= currentLevelLen-1:
			right = RoomOrder[pos[0]][pos[1]+1]
		if pos[1]-1 >= 0:
			left = RoomOrder[pos[0]][pos[1]-1]
		if pos[0]+1 <= levels-1:
			up = RoomOrder[pos[0]+1][pos[1]]
		if pos[0]-1 >= 0:
			down = RoomOrder[pos[0]-1][pos[1]]
		return {'right':right,'left':left,'up':up,'down':down}

	#Description: Return a random solution for player

	#Arguments:
	#	None
	#Returns:
	#	Dictionary of solution:
	#		'weapon': Weapon used in solution
	#		'room': Room of murder
	#		'murderer': The killer
	def getRandSolution(self):
		weapon = Weapons[randint(0, len(Weapons)-1)]
		room = Rooms[randint(0, len(Rooms)-1)]
		murderer = People[randint(0, len(People)-1)]
		return {'weapon':weapon, 'room':room, 'murderer':murderer}

	#Description: Print room of position

	#Arguments:
	#	pos: position of room to print; default: current player position
	#Returns:
	#	None
	def printRoom(self, pos=None):
		if pos == None:
			pos = self.pos
		print(RoomOrder[pos[0]][pos[1]].capitalize())
	
	#Description: Save player to file

	#Arguments:
	#	path: Path to save location
	#	player: Player object to save to file
	#Returns:
	#	None
	def save(self, path, player=None):
		if player == None:
			player = self
		with open(path, 'wb') as file:
			pickle.dump(player.getDict(), file)

	#Description: Load player from file

	#Arguments:
	#	path: Path to save location
	#Returns:
	#	Player object of save position
	def load(self, path):
		with open(path) as file:
			obj = pickle.load(file)
		return player(obj['pos'],obj['inv'],obj['size'],obj['solution'])

		
	#Description: Initialization function

	#Arguments:
	#	pos: Player Position
	#	inventory: Array of current inventory
	#	size: Maximum inventory size
	#	solution: Solution to current play through
	def __init__(self, pos, inventory, size, solution):
		self.pos = pos
		self.inventory = inventory
		self.inventorySize = size
		self.solution = solution
		if solution == None:
			self.solution = self.getRandSolution()

Weapons = ['knife','pen']
Rooms = ['study','hallway','dining','kitchen','ballroom','library','bathroom','closet','living']
RoomOrder = [['kitchen','hallway','dining'],['library','ballroom','study'],['bathroom','living','closet']]
People = ['maid', 'cook', 'wife', 'butler']
Items = ['book','bucket','mop','music','keys']
player = player([0,1], [], 15, None)

#SOLUTION
weapon = player.solution['weapon']
room = player.solution['room']
murderer = player.solution['murderer']

###########################################################################
print("\tMan's Homocide\n")
name = input(f'State your name:\n')

print('''Note: You are a detective investigating 
a crime that was commited 1 hour ago at the Henderson 
house hold. You have 7 supects.
''')
input('\t\t\t\t\tEnter to continue')

print('''Note: The victim's name was Josh Henderson. 
32 years old, a lawyer, he was found dead on the first floor in his study. 
The latest suspects: Millie Knolastname (maid), Georgia Valintine (maid), 
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
	1 - New Save
	2 - Save
	3 - Load
	4 - Suspects statements
	5 - Map
	6 - Inventory
	""")

	choice = input("Option:\n")

#exit:
	if choice == "0":
		print("Good-bye.")


#someone helped on saving and loading part
#new saving:
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
#saving:
	if choice == "2":
		if not os.path.exists(os.getcwd() + name + ".dat"):
			new = input("Create new save? [y/n] ")
			if new == 'y':
				save(os.getcwd() + name + ".dat", player)
		else:
			save(os.getcwd() + name + ".dat")
#loading:
	if choice == "3":
		location = input("Save file? ")
		if os.path.exists(os.getcwd() + location):
			player = load(os.getcwd() + location)
		else:
			print("Save not found!")
#######################################################################
#statements:
	if choice == "4":
		print('''Millie Knolastname has been a maid in the in the Henderson
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

		print('''Amina Bradford has been a maid for 2 year, her parents sold
off to work as a maid, Mr. Henderson gave her an oppatunity to continue her 
studies.

Her statement read: Amina was the closet grabing a bucket and the mop to 
cleanthe dinning room floor. While cleaning she gotten a chance to greet Mr.
Henderson, she says that he said "Good Afternoon, Ms. Bradford" then went
inside his studies. Also she happen to see Mrs. and Mr. Henderson arguing 
in the roomsomething about money and a baby.
''')
		input('\t\t\t\t\t\t\tEnter to continue')

		print('''Daisie Robies is the cook in the Henderson house hold, she 
has been a cook for the 8 years just like Millie Knolastname. Daisie said that
her and Mr. Henderson werereall good friends after his parents died.

Her statement read: Daisie was outside grabing boxes out of the truck that cames
by every month to deliver food for the Henderson's kitchen. Before she went to grab
another box, Mr. Henderson came up to her and they chatted for a while, but
to go back to work.Then as she was heading out to grab more boxes Mrs. Henderson
came up to her and a small chat about the food she was going to prepare.''')
	
		input('\t\t\t\t\t\t\tEnter to continue')

		print('''Elliot Yang is a cook that became the Henderson's staff 2 years ago.
Mrs. Henderson seem to have interest to him. They were seen talking all the time, the 
last time him and mrs. Henderson was talking he very happy about some news that Mrs.
Henderson was telling him about.

His statement reads: I was helping Daisie with the boxes, then talked with Mr.
and Mrs. Henderson about what they would like to eat for dinner.
''')
		input('\t\t\t\t\t\t\tEnter to continue')

		print('''Kelsey Henderson the women of the house, she has been married to Mr. Henderson
for 5 years. She was a socal person and very happy but did not like many people. She
was very good friends with Elliot, most people would say they are the bests of friends after he 
was hired to work there.

He statment read: I was heading to my bedroom after argguing with my husband about money 
problems we have, but before heading to our room i head to the bathroom to wash up from fight,
he is not a rough person just his words were ery hurtful. I went to talk with Eliot about it after.
''')
		input('\t\t\t\t\t\t\tEnter to continue')

		print('The butler was out of town for the week')

		input('\t\t\t\t\t\t\tEnter to continue')
#map:
	if choice == "5":
		printMap(RoomOrder)
		print('''__________________________________
| |........|.....G.....|.........|
| |.____...|...........|.........|
| ||    |..|...........|...___...|
| ||____|..|...........|..|   |..|
| |.......+|+.........+|+.|   |..|
| |........|...........|..|   |..|
| |........|...........|..|___|..|
| |........|...........|.........|
| |........|...........|.........|
| |...+....|.....@.....|....+....|
____________...=====...___________
|..|..+........|   |...|   |+....|
|..|...........|   |...|___|.....|
|.+|+..........|   |...|.........|
|..|...........|   |...|........+|
|..|...........|   |...|........_|
|@.|...........|___|...|.......| |
|..|...................|.......| |
|..|...................|....___| |
|.+|+..................|...|     |
|..|....@........+.....|..+|     |
_________________________________|
| |.....+..|.....+.....|..+......|
| |........|...........|.........|
| |........|...........|...__....|
| |........|...........|..|  |...|
| |@.......|...........|..|  |...|
| |........|..........+|+.|  |...|
| |........|...........|..|  |...|
| |........|...........|..|__|...|
| |________|...........|.........|
|          |...........|.........|
__________________________________''')
#inventory:
	if choice == "6":
		printInventory()
#items: