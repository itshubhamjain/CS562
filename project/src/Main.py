

from project.src.manage import Manage
from project.src.FileInput import FileInput
def main():
    manage = Manage()
    print(manage.tableStruct)
    fileInput =FileInput()
    attributes = fileInput.InputFile()
    file = fileInput.output(attributes,manage)
    print(file)

# select = []
#     numberGroupingVar = None
#     groupingAttr = []
#     f_Vect = []
#     selectCondition = []
#     havingCondition = []
#     where = ''


if __name__ =='__main__':
    main()