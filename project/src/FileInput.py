from project.Util.EMFAttributes import EMFAttributes
from project.Util.finalWrite import finalWrite

class FileInput:
    filePath = ''


    def readFile(self):
        while True:
            path = '/Users/shubhamjain/CS562/project/example'
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

        if file.readline().lower().__contains__('select'):
            while True:
                conditions = []
                temp = file.readline()[:-1]
                if temp.lower().__contains__('having'):
                    break
                temp = temp.split('and')
                for cons in temp:
                    conditions.append(cons.strip())
                # print(conditions)
                select.append(conditions)
        # print(select)
        having = []
        if temp.lower().__contains__('having'):

            temp = file.readline()
            if not temp.lower().__contains__('where'):
                having = ''
                having += temp
                having = having.split('and')
                having = [val.strip() for val in having]
        # print(having)
        where = ''
        if temp.lower().__contains__('where'):
            where = file.readline().strip()

        attr.emfAttributes(selectAttributes, n, groupAttributes, f_vect, select, having, where)
        # print(attr.f_Vect)

        return attr

    def output(self, attributes, manage):

        file = open('/Users/shubhamjain/CS562/project/output/output.py', 'w+')
        final_write = finalWrite()
        final_write.setFileName(file.name)
        imports = ['from configparser import RawConfigParser','import psycopg2']
        final_write.setImports(imports)
        final_write.setStructDB(manage.getStructDB())
        final_write.setAttributes(attributes)
        final_write.outputFile(manage)
        for write in final_write.returns:
            file.write(write)
        # print()
        return file.name



#
# fileInput = FileInput()
# fileInput.InputFile()

