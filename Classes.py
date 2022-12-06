import csv
import random

def log(str):
	print('(log)'+str(str))

class Cycle:
	def __init__ (self, season):
		if season.season == 'winter':
			self.dcycle = 12
			self.ncycle = 24 - self.dcycle
		elif season.season == 'spring':
			self.dcycle = 15
			self.dcycle = 24 - self.dcycle
		elif season.season == 'summer':
			self.dcycle = 18
			self.ncycle = 24 - self.dcycle
		elif season.season == 'autumn':
			self.dcycle = 13
			self.ncycle = 24 - self.dcycle

class Location:
	def __init__(self, location):
		self.location = location
		if location == 'forest':
			self.speed = 4
		elif location=='town':
			self.speed = 7
		elif location=='plains':
			self.speed = 6
		elif location == 'mountains':
			self.speed = 0
		else:
			self.speed == 'Null'

#СДЕЛАТЬ ПОТОМ СПИД В ПРОЦЕНТАХ В ЛОКАЦИЯХ СУКА И БЛЯТЬ НАХУЙ В СЕЗОНЫ 
class Season:
	def __init__(self, season):
		self.season = season
		if season == 'winter':
			self.speed = 0
		elif season=='spring':
			self.speed = 2
		elif season=='summer':
			self.speed = 3
		elif season=='autumn':
			self.speed = 1
		else:
			self.speed == 'Null'

class Halt:
	def __init__(self, season, location):
		self.time = 0
		if season == 'winter':
			self.time += 6
		elif season == 'summer':
			self.time += 4
		elif season == 'spring':
			self.time += 5
		elif season == 'autumn':
			self.time += 4

		if location == 'forest':
			self.time += 1
		elif location =='town':
			self.time -= 5
		elif location == 'plains':
			self.time -= 2
		elif location == 'mountains':
			self.time += 10

class MasNesInv:
	def __init__(self, food):
		self.ctent = int(Puteshestvenniki.ctravelers / 2) + (Puteshestvenniki.ctravelers % 2)
		self.tentmass = self.ctent * 1.5
		self.finalmass = food + self.tentmass
		
class Puteshestvenniki:
	def __init__(self, ctravelers):
		self.ctravelers = ctravelers
		self.speed = (ctravelers/2)
class ChTravelers:
	def __init__(self, charact):
		self.chtra = []
		

		