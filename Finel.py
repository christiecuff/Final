from time import sleep
from random import randint

import pickle
import os
class player():
	def __init__(self, pos, inventory):
		self.pos = pos
		self.inventory = inventory
	def getDict(self):
		return {'pos':self.pos,'inv':self.inventory}
	def setPlayerFromDict(self, dict):
		self.pos = dict['pos']
		self.inventory = dict['inv']


