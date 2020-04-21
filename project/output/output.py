from configparser import RawConfigParser
import psycopg2

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


class MF_Structure:
	prod = ''
	def getProd(self):
		return self.prod
	def setProd(self,prod):
		self.prod = prod
	month =  0
	def getMonth(self):
		return self.month
	def setMonth(self,month):
		self.month = month

	_1_count_quant =  None
	def get_1_count_quant(self):
		return self._1_count_quant
	def set_1_count_quant(self,_1_count_quant):
		self._1_count_quant = _1_count_quant

	_1_sum_quant =  None
	def get_1_sum_quant(self):
		return self._1_sum_quant
	def set_1_sum_quant(self,_1_sum_quant):
		self._1_sum_quant = _1_sum_quant

	_2_count_quant =  None
	def get_2_count_quant(self):
		return self._2_count_quant
	def set_2_count_quant(self,_2_count_quant):
		self._2_count_quant = _2_count_quant

	_2_sum_quant =  None
	def get_2_sum_quant(self):
		return self._2_sum_quant
	def set_2_sum_quant(self,_2_sum_quant):
		self._2_sum_quant = _2_sum_quant

	_3_count_quant =  None
	def get_3_count_quant(self):
		return self._3_count_quant
	def set_3_count_quant(self,_3_count_quant):
		self._3_count_quant = _3_count_quant


def main():

	configFile = "/Users/shubhamjain/CS562/project/db.properties"
	configPar = RawConfigParser()
	configPar.read(configFile)
	configuration = dict(configPar.items("DatabaseSection"))
	conn = psycopg2.connect(database = configuration['database'],user = configuration['user'], password=configuration['password'],host= configuration['host'], port = configuration['port'])
	cur = conn.cursor()
	print('Database connected Successfully')
if __name__ =='__main__':
	main()