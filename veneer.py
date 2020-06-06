# Codecademy veneer project

class Art:
	# artist=str, title=str, medium=str, year=int
	def __init__(self, artist, title, medium, year):
		self.artist=artist
		self.title=title
		self.medium=medium
		self.year=year

	def __repr__(self):
		return('{artist}. "{title}". {year}, {medium}.'.format(artist=self.artist, title=self.title, year=self.year, medium=self.medium))


class Marketplace:
	def __init__(self):
		self.listings=[]

	def add_listing(self, new_listing):
		self.listings.append(new_listing)

	def remove_listing(self, listing):
		self.listings.remove(listing)

	def show_listings(self):
		if len(self.listings)==0:
			print("No current listings")
		else:	
			for listing in self.listings:
				print(listing)

class Client:
	#name=str, location=str, is_museum=bool
	def __init__(self, name, location, is_museum):
		self.name=name
		self.location=location
		self.is_museum=is_museum


girl_with_mandolin = Art("Picasso, Pablo", "Girl with a Mandolin (Fanny Tellier)", 1910, "oil on canvas")
print(girl_with_mandolin)	

veneer = Marketplace()	
veneer.show_listings()

edytta=Client("Edytta Halpirt", "London", False)
moma=Client("The MOMA", "New York", True)