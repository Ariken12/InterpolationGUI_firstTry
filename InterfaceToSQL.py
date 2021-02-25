import pyodbc
import mysql.connector

class MSConnector:
    def __init__(self, server, port, database, user, password):
        self.connect_request = 'DRIVER={SQL Server};' + \
                               'SERVER={ip};' + \
                               'PORT={port};' + \
                               'DATABASE={db};' + \
                               'UID={usr};' + \
                               'PWD={pwd}'.format(
                                   ip=server, 
                                   port=port, 
                                   db=database, 
                                   usr=user, 
                                   pwd=password
                                   )
        self = pyodbc.connect(self.connect_request)
        self.cursor = self.cursor()

    def insert(self, table, **kwargs):
        request = 'INSERT INTO {table} ({fields}) VALUES ({values})'
        fields = ''
        values = ''
        for i in kwargs:
            fields += i + ', '
            values += kwargs[i]
        request = request.format(table=table, fields=fields, values=values)

class MyConnector:
    def __init__(self, server, port, database, user, password):
        self.core = mysql.connector.connect(host=server, database=database, user=user, password=password)
        if self.core.is_connected():
            print('Connected to MySQL database')
        self.cursor = self.core.cursor()
    
    def insert(self, table, **kwargs):
        request = 'INSERT INTO {table} ({fields}) VALUES ({values})'
        fields = ''
        values = ''
        for i in kwargs:
            fields += i + ', '
            values += str(kwargs[i]) + ', '
        request = request.format(table=table, fields=fields[:-2:], values=values[:-2:])
        print(request)
        self.cursor.execute(request)
        self.core.commit()