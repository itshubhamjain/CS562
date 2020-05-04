class Relation:
	cust = ''
	def getCust(self):
		return self.cust
	def setCust(self,cust):
		self.cust = cust
	prod = ''
	def getProd(self):
		return self.prod
	def setProd(self,prod):
		self.prod = prod
	day =  0
	def getDay(self):
		return self.day
	def setDay(self,day):
		self.day = day
	month =  0
	def getMonth(self):
		return self.month
	def setMonth(self,month):
		self.month = month
	year =  0
	def getYear(self):
		return self.year
	def setYear(self,year):
		self.year = year
	state = ''
	def getState(self):
		return self.state
	def setState(self,state):
		self.state = state
	quant =  0
	def getQuant(self):
		return self.quant
	def setQuant(self,quant):
		self.quant = quant
	def setAllVal(self, tuple):
		self.cust,self.prod,self.day,self.month,self.year,self.state,self.quant= tuple

