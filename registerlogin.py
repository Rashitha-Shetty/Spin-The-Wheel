import sqlite3 as sql

def register(uname,password,balance):
    
    db=sql.connect("userdetails.db")
    cursor=db.cursor()
    cursor.execute("create table if not exists user (username text primary key,password text,balance number)")
    
    try:
        cursor.execute(f"insert into user values ('{uname}','{password}',{balance})")  
        result = True
    except:
        result = False  
    
    db.commit()
    db.close() 
    return(result)



def login(uname,password):
    db=sql.connect("userdetails.db")
    cursor=db.cursor()
    cursor.execute("create table if not exists user (username text primary key,password text,balance number)")
    cursor.execute(f"select username,password from user where username='{uname}' and password='{password}'")
    match=cursor.fetchall()
    db.commit()
    db.close()
    return False if match ==[] else True
    # if match==[]:
    #     return False
    # else:
    #     return True
    
    