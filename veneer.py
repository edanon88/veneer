# Codecademy veneer project

class Art:
	# artist=str, title=str, medium=str, year=int, owner=Client
	def __init__(self, artist, title, medium, year, owner):
		self.artist=artist
		self.title=title
		self.medium=medium
		self.year=year
		self.owner=owner

	def __repr__(self):
		return('{artist}. "{title}". {year}, {medium}. {owner}, {location}'.format(artist=self.artist, title=self.title, year=self.year, medium=self.medium, owner=self.owner.name, location=self.owner.location))


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

class Listing:
	# art=Art, price=int, seller=Client
	def __init__(self, art, price, seller):
		self.art=art
		self.price=price
		self.seller=seller

	def __repr__(self):
		return(self.art.title+" - $"+str(self.price))


class Client:
	#name=str, location=str, is_museum=bool
	def __init__(self, name, location, is_museum):
		self.name=name
		self.location=location
		self.is_museum=is_museum

	#artwork=Art, price=int
	def sell_artwork(self, artwork, price):
		if artwork.owner != self:
			print("You don't own this!")
		else:
			sale_listing = Listing(artwork, price, artwork.owner)
			veneer.add_listing(sale_listing)


veneer = Marketplace()	
veneer.show_listings()

edytta=Client("Edytta Halpirt", "London", False)
moma=Client("The MOMA", "New York", True)

girl_with_mandolin = Art("Picasso, Pablo", "Girl with a Mandolin (Fanny Tellier)", 1910, "oil on canvas", edytta)
print(girl_with_mandolin)	

edytta.sell_artwork(girl_with_mandolin,6000000)
veneer.show_listings()