import pyodbc
import MySQLdb
import pandas as pd

pyodbc.drivers()
mydb = MySQLdb.connect(host='3306', user='root', passwd='2807', db='batata')

with open('cars.csv') as csv_file:
    csv_file = csv.reader(csv_file, delimiter=',')
    for row in csv_file:
        value = (row[0], row[1], row[2])
        all_value.append(value)

query = "INSERT INTO batata (Potato) VALUES (?)"
mycursor = mydb.connect()
mycursor.executemany(query, all_value)
mydb.commit()
