import pyodbc

class DBProcessing(object):
    """This is class create SQL-commands conversion to Xml and save them into file"""
    server = 'localhost'
    database = 'SampleDB2'
    username = 'sa'
    password = 'your_password'
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER='+server+';PORT=1443;DATABASE='+database+';')
    cursor = cnxn.cursor()

    def InsertQ():
        print ('Inserting a new row into table')
        #Insert Query
        tsql = "INSERT INTO Employees (Name, Location) VALUES (?,?);"
        with cursor.execute(tsql,'Jake','United States'):
            print ('Successfuly Inserted!')

    #Update Query
    def UpdateQ():
        print ('Updating Location for Nikita')
        tsql = "UPDATE Employees SET Location = ? WHERE Name = ?"
        with cursor.execute(tsql,'Sweden','Nikita'):
            print ('Successfuly Updated!')


    #Delete Query
    def DeleteQ():
        print ('Deleting user Jared')
        tsql = "DELETE FROM Employees WHERE Name = ?"
        with cursor.execute(tsql,'Jared'):
            print ('Successfuly Deleted!')


    #Select Query
    def SelectQ():
        print ('Reading data from table')
        tsql = "SELECT Name, Location FROM Employees;"
        with cursor.execute(tsql):
            row = cursor.fetchone()
            while row:
                print (str(row[0]) + " " + str(row[1]))
                row = cursor.fetchone()

