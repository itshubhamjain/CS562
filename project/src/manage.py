from configparser import RawConfigParser
import psycopg2

class Manage:
    properties = []
    configuration = '/Users/shubhamjain/CS562/project/db.properties'
    tableName = ''
    tableStruct = {}
    config = {}
    connections = []

    # Constructor
    def __init__(self):
        configPar = RawConfigParser()
        configPar.read(self.configuration)
        self.config = dict(configPar.items('DatabaseSection'))
        self.tableName = 'sales'
        self.tableStruct = self.getStructDB(self.tableName,config)

    def getConnections(self):
        return self.connections.pop(0)
    def closeConnection(self,conn):
        if conn:
            conn.close()
            
    #Retrive the database schema
    def getStructDB(self,tableName, config):
        struct = {}
        try:
            conn = psycopg2.connect(database = config['database'],user = config['user'], password=config['password'],host= config['host'], port = config['port'])
            cur = self.conn.cursor()
            cur.execute("select column_name,data_type" + " from information_schema.columns"+ " where table_name='"+ tableName+"'")
            print('Retrieving information Schema of table'+tableName)
            rows = cur.fetchall()
            for row in rows:
                struct[row[0]] = 'str' if row[1] is 'character varying' or 'character' else 'int'
            self.connections.append(conn)
            cur.close()
            del rows
        except (Exception, psycopg2.Error) as error :
            print ("Error while fetching data from PostgreSQL", error)

        return struct

