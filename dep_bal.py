import sqlite3 as sql
def checkbal(uname):
    db=sql.connect("userdetails.db")
    cursor=db.cursor()
    cursor.execute(f"select balance from user where username='{uname}'")
    re=cursor.fetchall()
    return int(re[0][0])
    
def deposit(uname,balance):
    db=sql.connect("userdetails.db")
    cursor=db.cursor()
    cursor.execute(f"update user set balance=balance+{balance} where username='{uname}'")
    db.commit()
    db.close()
    
def update(uname,bal):
    db=sql.connect("userdetails.db")
    cursor=db.cursor()
    cursor.execute(f"update user set balance={bal} where username='{uname}'")
    db.commit()
    db.close()
    