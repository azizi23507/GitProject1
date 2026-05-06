



from mysql.connector import Error
from tabulate import tabulate
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="shabir123",
    # database = "test"
)
my_cursor = mydb.cursor()
my_cursor.execute("USE world")
my_cursor.execute("SELECT * FROM country")
items = my_cursor.fetchall()

first_row = [col[0] for col in my_cursor.description]
print(tabulate(items, headers=first_row, tablefmt="psql"))
print(my_cursor.description)