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
	def setAllVal(self, tuple):
		self.cust,self.prod,self.day,self.month,self.year,self.state,self.quant= tuple

class MF_Structure:
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

	_1_count_quant =  0
	def get_1_count_quant(self):
		return self._1_count_quant
	def set_1_count_quant(self,_1_count_quant):
		self._1_count_quant = _1_count_quant

	_1_sum_quant =  0
	def get_1_sum_quant(self):
		return self._1_sum_quant
	def set_1_sum_quant(self,_1_sum_quant):
		self._1_sum_quant = _1_sum_quant

	_2_count_quant =  0
	def get_2_count_quant(self):
		return self._2_count_quant
	def set_2_count_quant(self,_2_count_quant):
		self._2_count_quant = _2_count_quant

	_2_sum_quant =  0
	def get_2_sum_quant(self):
		return self._2_sum_quant
	def set_2_sum_quant(self,_2_sum_quant):
		self._2_sum_quant = _2_sum_quant


def main():

	configFile = "/Users/shubhamjain/CS562/project/db.properties"
	configPar = RawConfigParser()
	configPar.read(configFile)
	configuration = dict(configPar.items("DatabaseSection"))
	conn = psycopg2.connect(database = configuration['database'],user = configuration['user'], password=configuration['password'],host= configuration['host'], port = configuration['port'])
	cur = conn.cursor()
	print('Database connected Successfully')
	mfStructure = []
	cur.execute("select * from sales")
	rows = cur.fetchall()
	for row in rows:
		relation  = Relation()
		relation.setAllVal(row)
		addToMF = True
		for eachMF in mfStructure:
			if eachMF.getCust()==relation.getCust() and eachMF.getProd()==relation.getProd() :
				addToMF = False
				break
		if addToMF:
			addToMF = False
			mf = MF_Structure()
			mf.setCust(relation.getCust())
			mf.setProd(relation.getProd())
			mf.set_1_count_quant(0.000001)
			mf.set_1_sum_quant(0)
			mf.set_2_count_quant(0.000001)
			mf.set_2_sum_quant(0)
			mfStructure.append(mf)


	cur.execute("select * from sales")
	rows = cur.fetchall()
	for row in rows:
		relation = Relation()
		relation.setAllVal(row)
		for index, mfs in enumerate(mfStructure):
			if ( relation.getCust()==mfs.getCust()) and ( relation.getProd()==mfs.getProd()):
				mfs.set_1_count_quant(mfs.get_1_count_quant()+1)
				mfs.set_1_sum_quant(mfs.get_1_sum_quant() + relation.getQuant())
				mfStructure[index]= mfs

	cur.execute("select * from sales")
	rows = cur.fetchall()
	for row in rows:
		relation = Relation()
		relation.setAllVal(row)
		for index, mfs in enumerate(mfStructure):
			if ( relation.getCust()!=mfs.getCust()) and ( relation.getProd()==mfs.getProd()):
				mfs.set_2_count_quant(mfs.get_2_count_quant()+1)
				mfs.set_2_sum_quant(mfs.get_2_sum_quant() + relation.getQuant())
				mfStructure[index]= mfs

	print('{0:9s}'.format('cust'),end = '   ')
	print('{0:9s}'.format('prod'),end = '   ')
	print('{0:12s}'.format('1_avg_quant'),end = '   ')
	print('{0:12s}'.format('2_avg_quant'),end = '   ')
	print()
	print("=========",end = "   ")
	print("=========",end = "   ")
	print("============",end = "   ")
	print("============",end = "   ")
	print()
	for idx, mfs in enumerate(mfStructure):
		print("{0:9s}".format(mfs.getCust()),end = "   ")
		print("{0:9s}".format(mfs.getProd()),end = "   ")
		print("{0:12f}".format(mfs.get_1_sum_quant() / mfs.get_1_count_quant()),end = "   ")
		print("{0:12f}".format(mfs.get_2_sum_quant() / mfs.get_2_count_quant()),end = "   ")
		print()

if __name__ =='__main__':
	main()