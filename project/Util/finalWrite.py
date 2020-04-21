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
            temp += '\t\tself.'+vals[0]+' = '+vals[0]+'\n\n'
        temp+='\n'
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

    def startMain(self):

        # temp = 'class '+self.getFileName().split('/')[-1].split('.')[0]+' :'
        temp = 'def main():\n\n'
        temp += '\tconfigFile = "/Users/shubhamjain/CS562/project/db.properties"\n'
        temp +='\tconfigPar = RawConfigParser()\n'
        temp +='\tconfigPar.read(configFile)\n'
        temp +='\tconfiguration = dict(configPar.items("DatabaseSection"))\n'
        temp +="\tconn = psycopg2.connect(database = configuration['database'],user = configuration['user'], password=configuration['password'],host= configuration['host'], port = configuration['port'])\n"
        temp +="\tcur = conn.cursor()\n"
        temp +="\tprint('Database connected Successfully')\n"
        temp +="if __name__ =='__main__':\n\tmain()"


        self.returns.append(temp)
    def outputFile(self):
        self.printImports()
        self.printRelations()
        self.printMFStructure()
        self.startMain()
        return self.returns


