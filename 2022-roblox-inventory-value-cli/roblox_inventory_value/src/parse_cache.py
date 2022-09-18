from os.path import exists

import pickle

def get_filename(userID):
	return "../inventory_cache/{0}.txt".format(userID)

def load(userID):
	file = get_filename(userID)

	if exists(file):
		with open(get_filename(userID), "rb") as file:
			cache = pickle.load(file)

	return cache

def write(userID):
	file = get_filename(userID)
	
	if exists(file):
		with open(get_filename(userID), "wb") as file:
			pickle.dump(file)
