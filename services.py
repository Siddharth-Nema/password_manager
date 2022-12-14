import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="password_manager"
)

cursor = mydb.cursor(buffered=True)

def addPassword(entry, name):
    sql = "INSERT INTO {table} (site , username, password) VALUES (%s , %s , %s)"
    values = (entry['site'], entry['username'], entry['password'])

    cursor.execute(sql.format(table=name), values)
    mydb.commit()

    print(cursor.rowcount, "record inserted.")


def deletePassword(id, name):
    print(id)
    sql = "DELETE FROM {table} WHERE id=%s"
    values = (id,)

    cursor.execute(sql.format(table=name), values)
    mydb.commit()

    print(cursor.rowcount, "record deleted.")


def getPasswords(name):
    we = 'SELECT * FROM {table};'
    cursor.execute(we.format(table=name))
    passwords = cursor.fetchall()
    
    for x in passwords:
        print(x)
    
    return passwords

def createAccount(entry):
    sql = "INSERT INTO admin (username, password) VALUES (%s , %s)"
    values = (entry['username'], entry['password'])

    cursor.execute(sql, values)
    mydb.commit()

    sql = "CREATE TABLE {table} ( id int NOT NULL AUTO_INCREMENT, site VARCHAR(255) , username VARCHAR(255) , password VARCHAR(255), PRIMARY KEY(id))"
    cursor.execute(sql.format(table=entry['username']))

    print(cursor.rowcount, "record inserted.")

def login(entry):
    sql = 'SELECT * FROM admin'
    cursor.execute(sql)
    mydb.commit()

    users = cursor.fetchall()

    if((entry['username'], entry['password']) in users):
        return True
    else:
        return False
