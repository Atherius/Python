import pyodbc
import pandas as pd                             

connection_string = (
    "Driver={SQL Server};"
    "Server=LAPTOP-HKILR459;"  
    "Database=AdventureWorks2022;" 
    "Trusted_Connection=yes;"    
)
connection = pyodbc.connect(connection_string)
cursor = connection.cursor()

cursor.execute("USE Supply_Chain")
#cursor.execute("INSERT INTO BIZM.regions (rname, conti_name, modified_date, mod_user) VALUES ('North America', 'America', GETDATE(), 'Harrdy')")
#connection.commit()
cursor.execute("exec sp_help 'BIZM.regions'")
while True:
    rows = cursor.fetchall()
    if not rows:
        break
    columns = [column[0] for column in cursor.description]
    df = pd.DataFrame.from_records(rows, columns=columns)
    print(df)
    if not cursor.nextset():
        break

cursor.close()
connection.close()
