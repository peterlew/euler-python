
class Calendar():

	def __init__(self):
		#Initial condition: Monday, Jan 1, 1900
		self.day = 1 #Sunday will be 0
		self.date = 1 #"Day of the month"
		self.month = 1 
		self.year = 1900

	def next(self):
		self.day += 1
		self.day %= 7
		self.date += 1
		if self.date > 31:
			self.month += 1
			self.date = 1
		if self.date > 30 and self.month in [9, 4, 6, 11]:
			self.month += 1
			self.date = 1
		if self.date > 29 and self.month == 2:
			self.month += 1
			self.date = 1
		if self.date > 28 and self.month == 2:
			if self.year % 4 != 0 or self.year % 100 == 0:
				if self.year % 400 != 0:
					self.month += 1
					self.date = 1
		if self.month > 12:
			self.year += 1
			self.month = 1

	def show(self):
		return(self.day, self.month, self.date, self.year)


c = Calendar()
(d, m, n, y) = c.show()
counter = 0
while y < 2001:
	if d == 0 and n == 1 and y > 1900:
		counter += 1
	c.next()
	(d, m, n, y) = c.show()
print(counter)
				
				
				
