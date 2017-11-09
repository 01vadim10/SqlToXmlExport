import pyodbc
import os

class DBProcessing(object):
    """This is class create SQL-commands conversion to Xml and save them into file"""
    username = 'vadimZ'
    password = '1991'

    def connect(self, params):
        if params.username is None :
            cnxn = pyodbc.connect('DRIVER={SQL Server Native Client 11.0};SERVER='+params.server+';DATABASE='+params.database+';UID='+username+';PWD='+ password)
        else:
            cnxn = pyodbc.connect('DRIVER={SQL Server Native Client 11.0};SERVER='+params.server+';DATABASE='+params.database+';UID='+params.username+';PWD='+ params.password)
        cursor = cnxn.cursor()
        #file = os.open('StoXScript', 'w+')
        if cursor:
            # Query
            tsql = "Select TABLE_NAME FROM INFORMATION_SCHEMA.TABLES Where TABLE_TYPE = 'BASE TABLE'"
            tsql2 = str.format("Select TABLE_NAME FROM {0}.INFORMATION_SCHEMA.TABLES Where TABLE_TYPE = 'BASE TABLE' Order By TABLE_NAME ASC;", params.database)
            with cursor.execute(tsql):
                rows = cursor.fetchall()
                if len(rows) > 0:
                    with open('StoXScript', 'w') as f:
                        i = 0
                        for row in rows:
                            i += 1
                            st = str.format("(SELECT * FROM dbo.{0} FOR XML PATH('{0}'), TYPE) AS 'Elements{1}',", row[0], i)
                            print (st, file=f)
