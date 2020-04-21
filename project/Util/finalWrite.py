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




