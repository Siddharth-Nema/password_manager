import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
)

cursor = mydb.cursor(buffered=True)

sql = 'CREATE DATABASE IF NOT EXISTS password_manager'
cursor.execute(sql)

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="password_manager"
)

cursor = mydb.cursor(buffered=True)

sql = 'CREATE TABLE IF NOT EXISTS admin(username varchar(255), password varchar(255))'
cursor.execute(sql)


