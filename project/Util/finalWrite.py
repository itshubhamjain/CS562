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
                temp += '\t' + vals + ' =  0\n'
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
                temp += '\t' + vals + ' =  0\n'
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

        # print(vars)
        self.setVars(vars)
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
        # print(self.getVars(), self.getAttributes().getGroupingAttr())

        for var in self.getVars():

            if var.__contains__('_0'):
                duplicate = var[:]
                if duplicate.__contains__('avg'):
                    group = var.replace('_0_avg_','')
                    _count = duplicate.replace('avg_','count_')
                    _sum  = duplicate.replace('avg_','sum_')
                    temp += '\t\t\tmf.set'+_sum+"(relation.get"+group[0].upper()+group[1:]+"()+mf.get"+_sum+"())\n"
        #             GADBAAD CHECK BAADME
                    temp += "\t\t\tmf.set"+_count+"(mf.get"+_count+"()+1)\n"
                else:
                    group = var.replace('_0_sum_','').replace('_0_max_','').replace('_0_min_','').replace('_0_count_','')
                    # duplicate = var[:]
                    if var.__contains__('_sum_'):
                        temp += '\t\t\tmf.set'+var+"(relation.get"+group[0].upper()+group[1:]+"()+mf.get"+var+"())\n"
                    elif var.__contains__('_min_'):
                        temp += '\t\t\tif mf.get'+var+'() > relation.get'+group[0].upper()+group[1:]+'():\n'
                        temp += '\t\t\t\tmf.set'+var+'(relation.get'+group[0].upper()+group[1:]+'())\n'
                    elif var.__contains__('_max_'):
                        temp += '\t\t\tif mf.get' + var + '() < relation.get' + group[0].upper() + group[1:] + '():\n'
                        temp += '\t\t\t\tmf.set' + var + '(relation.get' + group[0].upper() + group[1:] + '())\n'
                    elif var.__contains__('_count_'):
                        temp += "\t\t\tmf.set" + var + "(mf.get" + var + "()+1)\n"
            elif var in self.getStructDB().keys():
                # print("Hello World", var)
                if var not in self.getAttributes().getGroupingAttr():
                    temp+= '\t\t\tmf.set'+ var[0].upper() + var[1:]+'(relation.get'+ var[0].upper() + var[1:] +'())\n'
            elif  not var.__contains__('_0'):
                # print("Hello World", var)
                if var.__contains__('_avg'):
                    _count = var.replace('avg_', 'count_')
                    _sum = var.replace('avg_', 'sum_')
                    temp += '\t\t\tmf.set' + _sum + "(0)\n"
                    temp += '\t\t\tmf.set' + _count + "(0.000001)\n"
                elif var.__contains__('_count'):
                    temp += '\t\t\tmf.set' + var + "(0.000001)\n"
                else:
                    temp += '\t\t\tmf.set' + var + "(0)\n"

        temp +='\t\t\tmfStructure.append(mf)\n\n\n'
        # print(self.vars)
        self.returns.append(temp)

    def nextParse(self, manage):
        relation = manage.getTableName()
        temp = ""
        numberGrouping = self.getAttributes().getNumberGrouping()
        selectCond  = self.getAttributes().getSelectCondition()
        tableStruct = self.getStructDB()
        # print(selectCond)
        # print(self.vars)
        for idx in range(numberGrouping):
            temp+= ''
            temp += '\tcur.execute("select * from ' + relation
            temp += self.getAttributes().getWhere() + '")\n' if self.getAttributes().getWhere() else '")\n'
            temp += '\trows = cur.fetchall()\n'
            temp += '\tfor row in rows:\n'
            temp += '\t\trelation = Relation()\n'
            temp += '\t\trelation.setAllVal(row)\n'
            temp += '\t\tfor index, mfs in enumerate(mfStructure):\n'
            temp += '\t\t\tif '
            for condition in selectCond[idx]:
                operator = ''
                if condition.__contains__('='):
                    operator = '='
                elif condition.__contains__('<>'):
                    operator = '<>'
                elif condition.__contains__('>'):
                    operator = '>'
                elif condition.__contains__('<'):
                    operator = '<'
                leftOperand = condition.split(operator)[0].strip().split('_')[1].strip()
                rightOperand = condition.split(operator)[1].strip()
                # print(condition)
                # print(leftOperand,rightOperand)
                if operator is '<>':
                    operator = '!='
                if operator  is '=':
                    operator = '=='
                    # print("Hello")
                temp +='( relation.get'+leftOperand[0].upper() +leftOperand[1:]+'()'+operator
                # print('( relation.get'+leftOperand[0].upper() +leftOperand[1:]+'()'+operator)
                # print(rightOperand in self.vars)
                if rightOperand in self.vars:
                    # if operator in ('==','!='):
                    temp+= 'mfs.get'+rightOperand[0].upper()+rightOperand[1:]+'())'

                else:
                    if ('_'+rightOperand).__contains__('avg_'):
                        _count = ('_'+rightOperand).replace('avg_','count_')
                        _sum = ('_' + rightOperand).replace('avg_', 'sum_')
                        temp += '(mfs.get'+_sum+'() / mfs.get'+_count + '()))'
                    else:
                        # right =
                        if '_'+rightOperand in self.vars:
                            temp += 'mfs.get'+('_'+rightOperand)+'())'

                        else:
                            if '+' in rightOperand or '-' in rightOperand or '/' in rightOperand or '*' in rightOperand:

                                if '+' in rightOperand:
                                    LHS = rightOperand.split('+')[0].strip()
                                    RHS = rightOperand.split('+')[1].strip()
                                    if LHS in self.vars:
                                        LHS = 'mfs.get'+LHS[0].upper()+LHS[1:]+'()'
                                    elif RHS in self.vars:
                                        RHS = 'mfs.get' + RHS[0].upper() + RHS[1:] + '()'
                                    temp += LHS+' + '+RHS+')'
                                if '-' in rightOperand:
                                    # print(rightOperand.split('-'))
                                    LHS = rightOperand.split('-')[0].strip()

                                    RHS = rightOperand.split('-')[1].strip()

                                    if LHS in self.vars:
                                        LHS = 'mfs.get'+LHS[0].upper()+LHS[1:]+'()'
                                    elif RHS in self.vars:
                                        RHS = 'mfs.get' + RHS[0].upper() + RHS[1:] + '()'
                                    temp += LHS+' - '+RHS+')'
                                if '*' in rightOperand:
                                    LHS = rightOperand.split('*')[0].strip()
                                    RHS = rightOperand.split('*')[1].strip()
                                    if LHS in self.vars:
                                        LHS = 'mfs.get'+LHS[0].upper()+LHS[1:]+'()'
                                    elif RHS in self.vars:
                                        RHS = 'mfs.get' + RHS[0].upper() + RHS[1:] + '()'
                                    temp += LHS+' * '+RHS+')'
                                if '/' in rightOperand:
                                    LHS = rightOperand.split('/')[0].strip()
                                    RHS = rightOperand.split('/')[1].strip()
                                    if LHS in self.vars:
                                        LHS = 'mfs.get'+LHS[0].upper()+LHS[1:]+'()'
                                    elif RHS in self.vars:
                                        LRS = 'mfs.get' + RHS[0].upper() + RHS[1:] + '()'
                                    temp += LHS+' / '+RHS+')'

                            else:

                                rightOperand = rightOperand.replace("'","\"")
                                temp += rightOperand +")"
                temp += " and "
            temp = temp[:-5]
            temp +=':\n'
            FVectors = self.getAttributes().getF_Vect()
            for fvect in FVectors:
                if (str(idx+1)+'_') in fvect:
                    if 'avg' in fvect:
                        _count = '_'+str(idx+1)+'_count_'+fvect.split("_")[2]
                        _sum  = '_'+str(idx+1)+'_sum_'+fvect.split("_")[2]
                        temp += '\t\t\t\tmfs.set'+_count+'(mfs.get'+_count+'()+1)\n'
                        temp += '\t\t\t\tmfs.set'+_sum+'(mfs.get'+_sum+'() + relation.get'+fvect.split('_')[2][0].upper()+fvect.split('_')[2][1:]+'())\n'
                    elif 'count' in fvect:
                        _count = '_' + str(idx+1) + '_count_' + fvect.split("_")[2]
                        temp += '\t\t\t\tmfs.set' + _count + '(mfs.get' + _count + '() + relation.get'+fvect.split('_')[2][0].upper()+fvect.split('_')[2][1:]+'())\n'
                    elif 'sum' in fvect:
                        _sum = '_' + str(idx+1) + '_sum_' + fvect.split("_")[2]
                        temp += '\t\t\t\tmfs.set' + _sum + '(mfs.get' + _sum + '() + relation.get' + \
                                fvect.split('_')[2][0].upper() + fvect.split('_')[2][1:] + '())\n'
                    elif 'max' in fvect:
                        _max = '_'+str(idx+1)+'_max_'+fvect.split('_')[2]
                        temp += "\t\t\tif mfs.get"+_max+'() < relation.get'+fvect.split('_')[2][0].upper()+fvect.split('_')[2][1:]+'():\n'
                        temp += '\t\t\t\tmfs.set'+_max+'(relation.get'+fvect.split('_')[2][0].upper()+fvect.split('_')[2][1:]+'())\n'

                    elif 'min' in fvect:
                        _min = '_'+str(idx+1)+'_min_'+fvect.split('_')[2]
                        temp += "\t\t\tif mfs.get"+_min+'() > relation.get'+fvect.split('_')[2][0].upper()+fvect.split('_')[2][1:]+'():\n'
                        temp += '\t\t\t\tmfs.set'+_min+'(relation.get'+fvect.split('_')[2][0].upper()+fvect.split('_')[2][1:]+'())\n'

                    temp += '\t\t\t\tmfStructure[index]= mfs'
            temp += '\n\n'

        self.returns.append(temp)
        # print(self.getAttributes().getF_Vect())
    def removeConditionsMF(self):
        temp = ''
        having = self.getAttributes().getHavingCondition()
        if having:
            temp += '\tdelete = []\n'
            temp += '\tfor idx,mfs in enumerate(mfStructure):\n\t\tif not('
            for condition in having:
                operator = ''
                if condition.__contains__('='):
                    operator = '='
                elif condition.__contains__('<>'):
                    operator = '<>'
                elif condition.__contains__('>'):
                    operator = '>'
                elif condition.__contains__('<'):
                    operator = '<'
                leftOperand = condition.split(operator)[0].strip()
                rightOperand = condition.split(operator)[1].strip()
                # print(leftOperand,rightOperand)
                if 'avg' in leftOperand:
                    _sum = '_'+leftOperand.replace('avg','sum')
                    _count = '_'+leftOperand.replace('avg','count')
                    temp += '(mfs.get'+_sum+'()/mfs.get'+_count+'())'
                else:
                    if (''+leftOperand) in self.vars:
                        temp += '(mfs.get'+'_'+leftOperand+'()'

                temp += operator
                duplicate = '_'+rightOperand
                if rightOperand in self.vars:
                    duplicate = rightOperand[0].upper()+rightOperand[1:]
                    temp += '(mfs.get'+rightOperand[0].upper()+rightOperand[1:]+'()'

                if 'avg' in rightOperand:
                    _sum = '_'+rightOperand.replace('avg','sum')
                    _count = '_'+rightOperand.replace('avg','count')
                    print(_sum,_count)
                    temp += '(mfs.get'+_sum+'()'+'/ mfs.get'+_count+'())'

                if duplicate in  self.vars:
                    temp += '(mfs.get'+duplicate+'()'

                else:
                    if '+' in rightOperand or '-' in rightOperand or '/' in rightOperand or '*' in rightOperand:
                        # print(rightOperand)
                        if '+' in rightOperand:

                            LHS = rightOperand.split('+')[0].strip()
                            RHS = rightOperand.split('+')[1].strip()
                            if LHS in self.vars:
                                LHS = 'mfs.get' + LHS[0].upper() + LHS[1:] + '()'
                            elif RHS in self.vars:
                                RHS = 'mfs.get' + RHS[0].upper() + RHS[1:] + '()'
                            temp += LHS + ' + ' + RHS + ')'
                        elif '-' in rightOperand:
                            # print(rightOperand.split('-'))
                            LHS = rightOperand.split('-')[0].strip()

                            RHS = rightOperand.split('-')[1].strip()

                            if LHS in self.vars:
                                LHS = 'mfs.get' + LHS[0].upper() + LHS[1:] + '()'
                            elif RHS in self.vars:
                                RHS = 'mfs.get' + RHS[0].upper() + RHS[1:] + '()'
                            temp += LHS + ' - ' + RHS + ')'
                        elif '*' in rightOperand:
                            LHS = rightOperand.split('*')[0].strip()
                            RHS = rightOperand.split('*')[1].strip()
                            if LHS in self.vars:
                                LHS = 'mfs.get' + LHS[0].upper() + LHS[1:] + '()'
                            elif RHS in self.vars:
                                RHS = 'mfs.get' + RHS[0].upper() + RHS[1:] + '()'
                            temp += LHS + ' * ' + RHS + ')'
                        elif '/' in rightOperand:
                            LHS = rightOperand.split('/')[0].strip()
                            RHS = rightOperand.split('/')[1].strip()
                            if LHS in self.vars:
                                LHS = 'mfs.get' + LHS[0].upper() + LHS[1:] + '()'
                            elif RHS in self.vars:
                                LRS = 'mfs.get' + RHS[0].upper() + RHS[1:] + '()'
                            temp += LHS + ' / ' + RHS + ')'
                        # print(LHS,RHS)
                temp += " and "
            temp = temp[:-4]
            temp += '):\n'
            temp+= '\t\t\tdelete.append(mfs)\n'
            temp += '\tfor mfs in delete:\n'
            temp += '\t\tmfStructure.remove(mfs)\n'
            # temp += '\t\t\tidx-=1\n'





        # print(having)
        self.returns.append(temp)

        # print('========\t\t========\t\t===========\t\t===========\t\t===========')
        # for mfs in mfStructure:
        #     print('{0:8s}\t\t{1:8d}\t\t{2:11f}\t\t{3:11f}\t\t{4:11f}'.format(mfs.getCust(), mfs.getMonth(),
        #                                                                      mfs.get_1_sum_quant() / mfs.get_1_count_quant(),
        #                                                                      mfs.get_0_sum_quant() / mfs.get_0_count_quant(),
        #                                                                      mfs.get_2_sum_quant() / mfs.get_2_count_quant()))

    def resultMain(self):
        temp = ''
        selectAttr = self.getAttributes().getSelect()
        print(selectAttr)
        lengthString = 'print("'
        endString =  ',.format('
        ArrLength = []
        for idx,attributes in enumerate(selectAttr):
            length = len(attributes) if attributes not in self.getStructDB().keys() else 8
            if '_' in attributes:
                temp+= "\tprint('{0:"+str(length+1)+"s}'.format('"+attributes+"'),end = '   ')\n"
            # elif
                # lengthString += '{'+str(idx)+':'+str(length)+'s}\\t'
                # endString += '"'+attributes+'", '
            elif '+' in attributes or '-' in attributes or '*' in attributes or '/' in attributes:
                temp+= '\tprint("{0:'+str(length)+1+'d}".format("'+attributes+'"), end = "   ")\n'
            elif attributes in self.getStructDB().keys():
                temp += "\tprint('{0:" + str(length + 1) + "s}'.format('" + attributes + "'),end = '   ')\n"
            else:
                temp += "\tprint('{0:" + str(length + 1) + "s}'.format('" + attributes + "'),end = '   ')\n"
            ArrLength.append(length+1)
        # print(lengthString+'"'+endString[1:-2]+'))')
        temp += "\tprint()\n"
        for idx in range(len(selectAttr)):
            strTemp = '='
            strTemp *= ArrLength[idx]
            temp += '\tprint("'+strTemp+'",end = "   ")\n'
        temp+='\tprint()\n'
        temp += '\tfor idx, mfs in enumerate(mfStructure):\n'

        for idx,attributes in enumerate(selectAttr):

            if '+' in attributes or '-' in attributes or '*' in attributes or '/' in attributes:
                temp += '\t\tprint("{0:'+str(ArrLength[idx])+'f}".format('
                # ), end = "   ")\n
                print(attributes)
                operator = ''
                if attributes.__contains__('+'):
                    operator = '+'
                elif attributes.__contains__('-'):
                    operator = '-'
                elif attributes.__contains__('/'):
                    operator = '/'
                elif attributes.__contains__('*'):
                    operator = '*'
                leftOperand = attributes.split(operator)[0].strip()
                rightOperand = attributes.split(operator)[1].strip()

                if 'avg' in leftOperand:
                    _count = ('_' + leftOperand).replace('avg_', 'count_').strip()
                    _sum = ('_' + leftOperand).replace('avg_', 'sum_').strip()
                    temp += 'mfs.get' + _sum + '() / mfs.get' + _count + '() '
                else:
                    temp += 'mfs.get'+ '_'+leftOperand+'() '

                temp += operator

                if 'avg' in rightOperand:
                    _count = ('_' + rightOperand).replace('avg_', 'count_').strip()
                    _sum = ('_' + rightOperand).replace('avg_', 'sum_').strip()
                    temp += 'mfs.get' + _sum + '() / mfs.get' + _count + '() '
                else:
                    temp += 'mfs.get' + '_' + rightOperand + '() '

                temp += "), end = '   ')\n"
                # temp += "), end = '   ')"
            else:
                if '_' in attributes:
                    temp += '\t\tprint("{0:'+str(ArrLength[idx])+'f}".format('
                    if 'avg' in attributes:
                        _count = ('_' + attributes).replace('avg_', 'count_').strip()
                        _sum = ('_' + attributes).replace('avg_', 'sum_').strip()
                        temp += 'mfs.get' + _sum + '() / mfs.get' + _count + '()),end = "   ")\n '
                    else:
                        temp += 'mfs.get' + '_' + attributes + '()),end = "   ")\n '

                else:
                    accessIdentifier = 'd' if self.getStructDB()[attributes] is 'int' else 's'
                    temp += '\t\tprint("{0:'+str(ArrLength[idx])+accessIdentifier+'}".format(mfs.get'+attributes[0].upper()+attributes[1:]+'()),end = "   ")\n'
        temp += '\t\tprint()\n'


        self.returns.append(temp)





    def startMain(self,manage):

        # temp = 'class '+self.getFileName().split('/')[-1].split('.')[0]+' :'
        temp = 'def main():\n\n'
        self.returns.append(temp)
        self.connectivity()
        self.firstParse(manage)
        self.nextParse(manage)
        self.removeConditionsMF()
        self.resultMain()
        temp ="\nif __name__ =='__main__':\n\tmain()"
        self.returns.append(temp)


    def outputFile(self,manage):
        self.printImports()
        self.printRelations()
        self.printMFStructure()
        self.startMain(manage)
        return self.returns


