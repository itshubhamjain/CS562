from configparser import RawConfigParser
import psycopg2

class Manage:
    properties = []
    configFile = '/Users/shubhamjain/CS562/project/db.properties'
    tableName = ''
    tableStruct = {}
    configuration = {}
    connections = []

    # Constructor
    def __init__(self):
        configPar = RawConfigParser()
        configPar.read(self.configFile)
        self.configuration = dict(configPar.items('DatabaseSection'))
        self.tableName = 'sales'
        self._setStructDB(self.tableName, self.configuration)
        self.tableStruct = self.getStructDB()
        conn = psycopg2.connect(database = self.configuration['database'],user = self.configuration['user'], password=self.configuration['password'],host= self.configuration['host'], port = self.configuration['port'])
        self.connections.append(conn)

    def getStructDB(self):
        return self.tableStruct

    #Retrive the database schema
    def _setStructDB(self,tableName, configuration):
        struct = {}
        try:
            conn = psycopg2.connect(database = configuration['database'],user = configuration['user'], password=configuration['password'],host= configuration['host'], port = configuration['port'])
            cur = conn.cursor()
            cur.execute("select column_name,data_type" + " from information_schema.columns"+ " where table_name='"+ tableName+"'")
            print('Retrieving information Schema of table'+tableName)
            rows = cur.fetchall()
            for row in rows:
                struct[row[0]] = 'str' if row[1] is 'character varying' or 'character' else 'int'
        except (Exception, psycopg2.Error) as error :
            print ("Error while fetching data from PostgreSQL", error)
        finally:
            cur.close()
            conn.close()
            del rows
            print("PostgreSQL connection is closed")
            self.tableStruct = struct

    def setStructDB(self,tableStruct):
        self.tableStruct = tableStruct

    def getConnection(self):
        return self.connections.pop(0)

    def closeConnection(self,conn):
        if conn:
            conn.close()

    def getTableName(self):
        return self.tableName

    def setTableName(self, tableName):
        self.tableName = tableName

    def getConfiguration(self):
        return self.configuration

    def getAllConnections(self):
        return self.connections

    def setAllConnections(self, connections):
        self.connections = connections

    def getConfigName(self):
        return self.configFile

    def setConfigName(self,configFile):
        self.configFile = configFile
