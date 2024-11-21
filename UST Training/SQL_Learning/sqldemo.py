import sqlite3
import pandas as pd
connection= sqlite3.connect(r"C:\Users\Administrator\Desktop\PythonTraining\UST Training\SQL_Learning\Chinook_Sqlite.sqlite")
curr=connection.cursor()

print(curr)


#curr.execute("SELECT name FROM sqlite_master WHERE type='table';")

#tables=curr.fetchall()
#for table in tables:
 #   print(table)

curr.execute("select * from 'Album' limit 10" )
data=curr.fetchall()
for row in data:
    print(row)

desc=curr.description
cols=[col[0] for col in desc]
print(cols)

#CRUD --> Create,Read,Update,Delete

#new_customer=(60,'Rajiv','RR','ABC','rajiv.rr@gmail.com','IND')

#curr.execute("""INSERT INTO Customer(CustomerId,FirstName,LastName,Company,Email,Country)VALUES(?,?,?,?,?,?)""",new_customer)
#connection.commit()
#print("New customer added")

#customer_id=60
#new_email="rajiv.rr@ust.com"
#curr.execute("""update Customer set Email=?,Company=? where CustomerId=?""",(new_email,'UST',customer_id))
#connection.commit()
#print("Customer updated")

#Delete
curr.execute("""delete from Customer where CustomerId=60""")
connection.commit()
print("Deleted Successfully")

#Read the customer that you just wrote to database
curr.execute("select * from Customer where CustomerId=60")
data=curr.fetchall()
for row in data:
    print(row)

desc=curr.description
cols=[col[0] for col in desc]
print(cols)

#query="""select * from Customer limit 100"""
#df_customers=pd.read_sql_query(query,connection)
#print(df_customers)
#connection.close()

#Determine the total sales for each country in the invoice table
query="""select BillingCountry,SUM(Total) as Total_Sales from Invoice group by BillingCountry
"""
df_customers=pd.read_sql_query(query,connection)
print(df_customers)
connection.close()