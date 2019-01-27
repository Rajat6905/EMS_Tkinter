import sqlite3
import os


class main:
    def checkuser(obj):
        
        user_id = obj.getId()
        password=obj.getPassword()
        
        if os.path.exists("Mydb"):
            db=sqlite3.connect("Mydb")
            cursor = db.cursor()
            cursor.execute('''SELECT id,password,name FROM users WHERE id=? AND password=?''', (user_id,password,))
            user = cursor.fetchall()
            
            if len(user)>0:
                return user[0][2]
            else:
                return False
        else:
            db=sqlite3.connect("Mydb")
            cursor = db.cursor()
            cursor.execute('''
                           CREATE TABLE users(id TEXT PRIMARY KEY,name TEXT,password TEXT,user_type TEXT,
                            user_status TEXT,contact INTEGER ,DOB TEXT, email TEXT
                                )''')
            
            
            cursor.execute('''INSERT INTO users(id,name,password,user_type,user_status,contact,DOB,email)
                  VALUES(?,?,?,?,?,?,?,?)''', ("1", "Rajat","admin","Admin","Active",8123432126,"12-09-1996","srajat490@gmail.com"))
            db.commit()
            
            db=sqlite3.connect("Mydb")
            cursor = db.cursor()
            cursor.execute('''SELECT id,password,name FROM users WHERE id=? AND password=?''', (user_id,password,))
        
            user = cursor.fetchall()
            
            if len(user)>0:
                return user[0][2]
            else:
                return False
            
        
    def returnid():
        db=sqlite3.connect("Mydb")
        cursor = db.cursor()
        cursor.execute("SELECT * FROM users ORDER BY id DESC")
        result = cursor.fetchone()
        return int(result[0])+1
       
    def addUsers(obj):
        db=sqlite3.connect("Mydb")
        cursor = db.cursor()
        cursor.execute('''SELECT id FROM users WHERE id=? ''', (obj.getId()))
            
        user = cursor.fetchall()
        if len(user)==1:
            return False
        else:
            cursor.execute('''INSERT INTO users(id,name,password,user_type,user_status,contact,DOB,email)
                      VALUES(?,?,?,?,?,?,?,?)''', (obj.getId(), obj.getName(),obj.getPassword(),obj.getuser_type(),
                      obj.getuser_status(),obj.getcontact(),obj.getdob(),obj.getemail()))
            
            db.commit()
            return True
    
    def search(u_id):
        db=sqlite3.connect("Mydb")
        cursor = db.cursor()
        cursor.execute('''SELECT name,user_type,user_status,contact,DOB,email FROM users WHERE id=?  ''',(u_id,))
        out=cursor.fetchone()
        if out==None:
            return False
        else:
            return out
    def all_user():
        db=sqlite3.connect("Mydb")
        cursor = db.cursor()
        cursor.execute('''SELECT id,name,user_type,user_status,contact,DOB,email FROM users''')
        u_l=cursor.fetchall()
        return u_l
    
    def delete(u_id):
        db=sqlite3.connect("Mydb")
        cursor = db.cursor()
        cursor.execute('''SELECT name,user_type,user_status,contact,DOB,email FROM users WHERE id=?  ''',(u_id,))
        out=cursor.fetchone()
        if out==None:
            return False
        else:
            cursor.execute('''DELETE FROM users WHERE id = ? ''', (u_id,))
            db.commit()
            return True
        
    def update(obj1):
        db=sqlite3.connect("Mydb")
        cursor = db.cursor()
        cursor.execute('''UPDATE users SET name=?,user_status=?,contact=?,DOB=?,email=? WHERE id = ? ''',
                       (obj1.getName(),obj1.getuser_status(),obj1.getcontact(),obj1.getdob(),obj1.getemail(),obj1.getId()))
        out=cursor.rowcount
        db.commit()
        if out==1:
            return True
        else:
            return False
   
        
    
    
        
        
        
        
    
    
        
    

                    
        
        
        
        
        
        
        
