# Codecademy veneer project
# Further work:
# Client available cash, affected by buying and selling.
# Client wishlists by artist, or title, and alerts, when things are listed
# Overall art database, splitting into universe of works, of which veneer listings are a subset

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
		#[Listing,,]

	def add_listing(self, new_listing):
		self.listings.append(new_listing)

	def remove_listing(self, listing):
		self.listings.remove(listing)

	def show_listings(self):
		print("Current listings on Veneer:")
		if len(self.listings)==0:
			print("No current listings")
		else:	
			for listing in self.listings:
				print(listing)
		print()

veneer = Marketplace()

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
			print("{name} doesn't own {artwork}, so can't put it up for sale.".format(name=self.name, artwork=artwork.title))
			print()
		else:
			sale_listing = Listing(artwork, price, artwork.owner)
			veneer.add_listing(sale_listing)
			print("{name} has announced that {title} by {artist} is for sale for ${price}".format(name=artwork.owner.name, title=artwork.title, artist=artwork.artist, price=price))
			print()

	def buy_artwork(self, artwork):
		print("{name} is interested in buying {artwork}".format(name=self.name, artwork=artwork.title))
		if artwork.owner==self:
			print("They already own this.")
			print()
		else:
			found=False
			for listing in veneer.listings:
				if listing.art == artwork:
					found=True
					art_listing=listing
					print("Sale announced: {buyer} has purchased {work} from {seller} for £{price}.".format(buyer=self.name, work=artwork.title, seller=artwork.owner.name, price=listing.price))
					listing.art.owner=self
					print(artwork)
					print()
					veneer.remove_listing(art_listing)
			if not found:
				print("{title} is not currently for sale. It is owned by {owner}.".format(title=artwork.title, owner=artwork.owner.name))
				print()	

edytta=Client("Edytta Halpirt", "London", False)
danon=Client("Edmund Danon", "Leeds", False)
griffin=Client("Ken Griffin", "Boca Raton", False)
moma=Client("The MOMA", "New York", True)
national=Client("The National Gallery", "London", True)
louvre=Client("The Louvre", "Paris", True)

girl_with_mandolin = Art("Picasso, Pablo", "Girl with a Mandolin (Fanny Tellier)", 1910, "oil on canvas", edytta)
boy_and_dog = Art("Basquiat, Jean-Michel", "Boy and Dog in a Johnnypump", 1982, "oil on canvas", griffin)
virgin_rocks = Art("DaVinci, Leonardo", "The Virgin of the Rocks", 1508, "oil on board", national)

veneer.show_listings()

edytta.sell_artwork(girl_with_mandolin,6000000)
national.sell_artwork(virgin_rocks, 240000000)
danon.sell_artwork(boy_and_dog, 100000000)

veneer.show_listings()

moma.buy_artwork(girl_with_mandolin)

veneer.show_listings()

griffin.sell_artwork(boy_and_dog, 100000000)

veneer.show_listings()

danon.buy_artwork(boy_and_dog)

veneer.show_listings()

moma.buy_artwork(boy_and_dog)

veneer.show_listings()

louvre.buy_artwork(virgin_rocks)

veneer.show_listings()