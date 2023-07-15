import pyodbc 

server = 'SHYAMASUS\SQLEXPRESS' 
database = 'patient' 
username = 'myusername' 
password = 'mypassword' 
cnxn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes;)
cursor = cnxn.cursor()