class Product(object):
	def __init__(self, price, count, tax):
		self.price = price 
		self.count = count
		self.tax = tax
	def price_with_tax(self):
		total = self.price*self.count*self.tax

		if self.price > 500:
			return 0.9*total
		else:
			return total


robot = Product(price = 900, count = 2, tax = 1.25 )
book = Product(price = 100, count = 1, tax = 1.06)

products = [Product(price = 900, count = 2, tax = 1.25 ), Product(price = 100, count = 1, tax = 1.06)]


total_price = 0

for product in products:
	total_price+=product.price_with_tax()
print total_price






def metodnamn(message):
	print message

metodnamn("Terre Terre")

def metod2():
	metodnamn("heyy")	
metod2()






