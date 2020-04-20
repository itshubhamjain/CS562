class FileInput:
    filePath = ''


    def readFile(self):
        while True:
            path = '/Users/shubhamjain/CS562/project/'
            path += input('Input the File Name with its path\n')
            try:
                file = open(path, "r")
                if file:
                    break
            except (Exception, FileExistsError) as error:
                print("Error while fetching data from file", error)
        return file

fileInput = FileInput()
fileInput.readFile()

