class finalWrite:
    tableStruct = {}
    fileName  = ''
    attributes = None
    imports = []
    returns = []
    vars = []
    package = ''

    def getPackage(self):
        return self.package

    def setPackage(self, package):
        self.package = package

    def getAttributes(self):
        return self.attributes

    def setAttributes(self, attributes):
        self.attributes = attributes

    def getStructDB(self):
        return self.tableStruct

    def setStructDB(self, tableStruct):
        self.tableStruct = tableStruct

    def getReturns(self):
        return  self.returns

    def setReturns(self, returns):
        self.returns = returns

    def getFileName(self):
        return self.fileName

    def setFileName(self, name):
        self.fileName = name

    def getImports(self):
        return self.imports

    def setImports(self, imports):
        self.imports = imports

    def getVars(self):
        return self.vars

    def setVars(self, vars):
        self.vars = vars

    def printImports(self):
        temp = ''
        for val in self.getImports():
            temp+=val+'\n'
        self.returns.append(temp+'\n')

    def printRelations(self):
        temp = ''
        temp += 'class Relation:\n'
        # self.returns.append(temp)
        # print(self.tableStruct)
        for vals in self.tableStruct.items():
            # print(vals[1]=='str')
            temp += '\t'+vals[0]+' =  0\n' if vals[1].__contains__('int') else '\t'+vals[0]+" = ''\n"
            # self.returns.append(temp)
            # temp+='\t'+vals[0]+'\n'
            temp += '\tdef get'+vals[0][0].upper()+vals[0][1:]+'(self):\n'
            # self.returns.append(temp)
            temp += '\t\treturn self.'+vals[0]+'\n'
            # self.returns.append(temp)
            temp += '\tdef set'+vals[0][0].upper()+vals[0][1:]+'(self,'+vals[0]+'):\n'
            # self.returns.append(temp)
            temp += '\t\tself.'+vals[0]+' = '+vals[0]+'\n'
        temp+=''
        temp+='\tdef setAllVal(self, tuple):\n\t\t'
        # temp+='):\n\t\t'
        for vals in self.tableStruct.keys():
            temp+='self.'+vals+','
        temp= temp[:-1]
        temp += '= tuple\n\n'
        self.returns.append(temp)

    def printMFStructure(self):
        temp = ''
        temp+= 'class MF_Structure:\n'
        # print(self.getAttributes().groupingAttr)
        vars = []
        for vals in self.tableStruct.items():

            if vals[0] in self.getAttributes().getGroupingAttr():
                vars.append(vals[0])
            # print(vals[1]=='str')
                temp += '\t'+vals[0]+' =  0\n' if vals[1].__contains__('int') else '\t'+vals[0]+" = ''\n"
                # self.returns.append(temp)
                # temp+='\t'+vals[0]+'\n'
                temp += '\tdef get'+vals[0][0].upper()+vals[0][1:]+'(self):\n'
                # self.returns.append(temp)
                temp += '\t\treturn self.'+vals[0]+'\n'
                # self.returns.append(temp)
                temp += '\tdef set'+vals[0][0].upper()+vals[0][1:]+'(self,'+vals[0]+'):\n'
                # self.returns.append(temp)
                temp += '\t\tself.'+vals[0]+' = '+vals[0]+'\n'
        temp+='\n'
        for idx,vals in enumerate(self.getAttributes().getF_Vect()):
            vals = '_'+vals

            if vals.__contains__('avg'):
                vals  = vals.replace('avg','count')
                temp += '\t' + vals + ' =  None\n'
                # self.returns.append(temp)
                # temp+='\t'+vals[0]+'\n'
                temp += '\tdef get' + vals[0].upper() + vals[1:] + '(self):\n'
                # self.returns.append(temp)
                temp += '\t\treturn self.' + vals + '\n'
                # self.returns.append(temp)
                temp += '\tdef set' + vals[0].upper() + vals[1:] + '(self,' + vals + '):\n'
                # self.returns.append(temp)
                temp += '\t\tself.' + vals + ' = ' + vals + '\n\n'
                vars.append(vals)

                vals = vals.replace('count', 'sum')
                temp += '\t' + vals + ' =  None\n'
                # self.returns.append(temp)
                # temp+='\t'+vals[0]+'\n'
                temp += '\tdef get' + vals[0].upper() + vals[1:] + '(self):\n'
                # self.returns.append(temp)
                temp += '\t\treturn self.' + vals + '\n'
                # self.returns.append(temp)
                temp += '\tdef set' + vals[0].upper() + vals[1:] + '(self,' + vals + '):\n'
                # self.returns.append(temp)
                temp += '\t\tself.' + vals + ' = ' + vals + '\n\n'
                vars.append(vals)

            else:
                temp += '\t' + vals + ' =  None\n'
                # self.returns.append(temp)
                # temp+='\t'+vals[0]+'\n'
                temp += '\tdef get' + vals[0].upper() + vals[1:] + '(self):\n'
                # self.returns.append(temp)
                temp += '\t\treturn self.' + vals + '\n'
                # self.returns.append(temp)
                temp += '\tdef set' + vals[0].upper() + vals[1:] + '(self,' + vals + '):\n'
                # self.returns.append(temp)
                temp += '\t\tself.' + vals + ' = ' + vals + '\n\n'
                vars.append(vals)
        temp += '\n'
        for idx, vals in enumerate(self.getAttributes().getSelect()):
            if vals not in vars and not vals.__contains__('_'):
                vars.append(vals)
                temp += '\t' + vals + ' =  None\n'
                # self.returns.append(temp)
                # temp+='\t'+vals[0]+'\n'
                temp += '\tdef get' + vals[0].upper() + vals[1:] + '(self):\n'
                # self.returns.append(temp)
                temp += '\t\treturn self.' + vals + '\n'
                # self.returns.append(temp)
                temp += '\tdef set' + vals[0].upper() + vals[1:] + '(self,' + vals + '):\n'
                # self.returns.append(temp)
                temp += '\t\tself.' + vals + ' = ' + vals + '\n\n'
                vars.append(vals)

        print(vars)
        self.returns.append(temp)

    def connectivity(self):
        temp = ''
        temp += '\tconfigFile = "/Users/shubhamjain/CS562/project/db.properties"\n'
        temp += '\tconfigPar = RawConfigParser()\n'
        temp += '\tconfigPar.read(configFile)\n'
        temp += '\tconfiguration = dict(configPar.items("DatabaseSection"))\n'
        temp += "\tconn = psycopg2.connect(database = configuration['database'],user = configuration['user'], password=configuration['password'],host= configuration['host'], port = configuration['port'])\n"
        temp += "\tcur = conn.cursor()\n"
        temp += "\tprint('Database connected Successfully')\n"
        self.returns.append(temp)

    def firstParse(self,manage):
        relation = manage.getTableName()
        temp = ''
        temp += '\tmfStructure = []\n'
        temp += '\tcur.execute("select * from ' + relation
        temp += self.getAttributes().getWhere() + '")\n' if self.getAttributes().getWhere() else '")\n'
        temp += '\trows = cur.fetchall()\n'
        temp += '\tfor row in rows:\n'
        temp += '\t\trelation  = Relation()\n'
        temp += '\t\trelation.setAllVal(row)\n'
        temp += '\t\taddToMF = True\n'
        temp += '\t\tfor eachMF in mfStructure:\n'
        groupingAtt = self.getAttributes().getGroupingAttr()
        if groupingAtt:
            temp += '\t\t\tif '
        for groups in groupingAtt:
            temp += 'eachMF.get' + groups[0].upper() + groups[1:] + '()==relation.get' + groups[0].upper() + groups[1:] + '() and '
        if temp[-4:] == 'and ':
            temp = temp[:-4] + ':\n'
            temp += '\t\t\t\taddToMF = False\n\t\t\t\tbreak\n'
        temp += '\t\tif addToMF:\n'
        temp += '\t\t\taddToMF = False\n'
        temp += '\t\t\tmf = MF_Structure()\n'

        for group in groupingAtt:
            temp+='\t\t\tmf.set'+group[0].upper()+group[1:]+'(relation.get'+group[0].upper()+group[1:]+'())\n'

        temp +='\t\t\tmfStructure.append(mf)'
        self.returns.append(temp)


    def startMain(self,manage):

        # temp = 'class '+self.getFileName().split('/')[-1].split('.')[0]+' :'
        temp = 'def main():\n\n'
        self.returns.append(temp)
        self.connectivity()
        self.firstParse(manage)
        temp ="\nif __name__ =='__main__':\n\tmain()"
        self.returns.append(temp)


    def outputFile(self,manage):
        self.printImports()
        self.printRelations()
        self.printMFStructure()
        self.startMain(manage)
        return self.returns


