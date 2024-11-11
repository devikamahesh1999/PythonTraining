import sqlite3
connection= sqlite3.connect(r"C:\Users\Administrator\Desktop\PythonTraining\UST Training\SQL_Learning\Chinook_Sqlite.sqlite")
curr=connection.cursor

print(curr)