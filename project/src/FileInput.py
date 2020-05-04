from project.Util.EMFAttributes import EMFAttributes
from project.Util.finalWrite import finalWrite
import re

class FileInput:
    filePath = ''
    EMF = True

    def readFile(self):
        while True:
            # print()
            self.EMF = False if not 'Y' in input("Enter Yes if EMF || Enter No for MF\n").strip().upper()  else True


            path = '/Users/shubhamjain/CS562/project/test/test'
            # path += input('Input the File Name with its path\n')
            try:
                file = open(path, "r")
                if file:
                    break
            except (Exception, FileExistsError) as error:
                print("Error while fetching data from file", error)
        return file

    def InputFile(self):
        print("Input File")
        attr = EMFAttributes()
        file = self.readFile()
        selectAttributes = []
        if file.readline().lower().__contains__('select'):
            selectAttributes =''
            selectAttributes += file.readline()
            selectAttributes = selectAttributes.strip().replace('  ',' ').split(',')

            for idx,selectAtt in enumerate(selectAttributes):
                selectAttributes[idx] = selectAtt.replace(',', '').replace(' ', '')
                if not selectAttributes[idx].isalpha():
                    selectAttributes[idx]  =  selectAtt.replace(',','').replace(' ','')
                    if not selectAttributes[idx].__contains__('_'):
                        print("You got trouble in select Attribute", selectAtt)

        n = 0
        if file.readline().lower().__contains__('variable'):
            n = int(file.readline().replace(' ',''))
        groupAttributes = []
        if file.readline().lower().__contains__('attributes'):
            groupAttributes = ''
            groupAttributes += file.readline()
            groupAttributes = groupAttributes.strip().replace(',', ' ').replace('  ', ' ').split(' ')
            for idx, groupAtt in enumerate(groupAttributes):
                if not groupAtt.isalpha():
                    groupAttributes[idx] = groupAtt.replace(',', '').replace(' ', '')
                    if not groupAttributes[idx].__contains__('_'):
                        print("You got trouble in group Attribute", groupAtt)
            # print(groupAttributes)
        f_vect = []
        if file.readline().lower().__contains__('vect'):
            f_vect = ''
            f_vect += file.readline()
            f_vect = f_vect.strip().replace(',', ' ').replace('  ', ' ').split(' ')
            for idx, vect in enumerate(f_vect):
                if not vect.isalpha():
                    f_vect[idx] = vect.replace(',', '').replace(' ', '')
                    if not f_vect[idx].__contains__('_'):
                        print("You got trouble in f-vect Attribute", vect)
        select = []
        selectJoint = []
        if not self.EMF:
            count = 0
            if file.readline().lower().__contains__('select'):
                while True:

                    conditions = []
                    tempJoint = []
                    temp = file.readline()[:-1]
                    if temp.lower().__contains__('having'):
                        break
                    groupingAddVariable = ''
                    for groups in groupAttributes:
                        groupingAddVariable += str(count + 1) + '_' + groups + ' = ' + groups + ' and '
                    # print(groupingAddVariable)
                    temp  = groupingAddVariable + temp
                    for i in range(len(temp) - 2):
                        if temp[i:i + 3] == 'and':
                            tempJoint.append('and')
                        if temp[i:i + 2] == 'or':
                            tempJoint.append('or')

                    temp = re.split('and|or', temp)
                    for cons in temp:
                        conditions.append(cons.strip())
                    # print(conditions)
                    select.append(conditions)
                    count+=1
                    selectJoint.append(tempJoint)
                    print(conditions,tempJoint)
        else:
            if file.readline().lower().__contains__('select'):
                while True:
                    conditions = []
                    tempJoint = []
                    temp = file.readline()[:-1]
                    if temp.lower().__contains__('having'):
                        break
                    for i in range(len(temp)-2):
                        if temp[i:i+3] =='and':
                            tempJoint.append('and')
                        if temp[i:i+2] == 'or':
                            tempJoint.append('or')

                    temp = re.split('and|or', temp)
                    for cons in temp:
                        conditions.append(cons.strip())
                    # print(conditions)
                    select.append(conditions)
                    selectJoint.append(tempJoint)

        having = []
        havingJoint = []
        if temp.lower().__contains__('having'):

            temp = file.readline()
            if not temp.lower().__contains__('where'):
                having = ''
                having += temp
                having  = re.split('and|or',having)
                for i in range(len(temp)-2):
                    if temp[i:i+3] =='and':
                        havingJoint.append('and')
                    if temp[i:i+2] == 'or':
                        havingJoint.append('or')
                having = [val.strip() for val in having]
        # print(havingJoint)
        where = ''
        if temp.lower().__contains__('where'):
            where = file.readline().strip()

        attr.emfAttributes(selectAttributes, n, groupAttributes, f_vect, select, having, where)
        attr.setHavingJoint(havingJoint)
        attr.setSelectJoint(selectJoint)
        # print(attr.f_Vect)

        return attr

    def output(self, attributes, manage):

        fileMain = open('/Users/shubhamjain/CS562/project/output/output.py', 'w+')
        fileMF = open('/Users/shubhamjain/CS562/project/output/mfstructure.py', 'w+')
        fileRel = open('/Users/shubhamjain/CS562/project/output/relation.py', 'w+')
        final_write = finalWrite()
        final_write.setFileName(fileMain.name)
        package = 'project.output'
        imports = ['from configparser import RawConfigParser','import psycopg2','from project.output.relation import Relation','from project.output.mfstructure import MF_Structure']
        final_write.setImports(imports)
        final_write.setStructDB(manage.getStructDB())
        final_write.setAttributes(attributes)
        # final_write.
        final_write.printRelations()
        final_write.printMFStructure()
        final_write.outputFile(manage)

        for write in final_write.returnMFStruct:
            fileMF.write(write)
        for write in final_write.returnTable:
            fileRel.write(write)
        for write in final_write.returns:
            fileMain.write(write)
        # print()
        return fileMain.name



#
# fileInput = FileInput()
# fileInput.InputFile()

