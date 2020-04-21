class EMFAttributes:
    select = []
    numberGroupingVar = None
    groupingAttr = []
    f_Vect = []
    selectCondition = []
    havingCondition = []
    where = ''

    def getSelect(self):
        return self.select

    def setSelect(self,select):
        self.select  = select

    def getNumberGrouping(self):
        return self.numberGroupingVar

    def setNumberGrouping(self, numberGroupingVar):
        self.numberGroupingVar = numberGroupingVar

    def getGroupingAttr(self):
        return self.groupingAttr

    def setGroupingAttr(self, groupingAttr):
        self.groupingAttr = groupingAttr

    def getF_Vect(self):
        return self.f_Vect

    def setF_Vect(self, f_Vect):
        self.f_Vect = f_Vect

    def getSelectCondition(self):
        return self.selectCondition

    def setSelectCondition(self, selectCondition):
        self.selectCondition = selectCondition

    def getHavingCondition(self):
        return self.havingCondition

    def setHavingCondition(self, havingCondition):
        self.havingCondition = havingCondition

    def getWhere(self):
        return self.where

    def setWhere(self, where):
        self.where = where

    def emfAttributes(self,select,numberGroupingVar ,groupingAttr,f_Vect ,selectCondition, havingCondition ,where ):

        self.select = select
        self.numberGroupingVar = numberGroupingVar
        self.groupingAttr = groupingAttr
        self.f_Vect = f_Vect
        self.selectCondition = selectCondition
        self.havingCondition = havingCondition
        self.where = where



