import pyodbc
import pandas as pd

pyodbc.drivers()

conn = pyodbc.connect(
    Trusted_Connected="Yes",
    Driver="{SQL Server}",
    Server="root",
    Database="batata",
    PWD=""
)
cursor = conn.cursor()

df = pd.read_csv("mario.csv")
df.head()
