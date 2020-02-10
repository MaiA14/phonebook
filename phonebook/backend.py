import sqlite3

class Database:

    def __init__(self,db):
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, name text, surname text, address text, phone text)")
        self.conn.commit()


    def insert(self,name,surname,address,phone):
        self.cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(name,surname,address,phone))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM book")
        rows=self.cur.fetchall()
        return rows

    def search(self,name="",surname="",address="",phone=""):
        self.cur.execute("SELECT * FROM book WHERE name=? OR surname=? OR address=? OR phone=?",(name,surname,address,phone))
        rows=self.cur.fetchall()
        return rows

    def delete(self,id):
        self.cur.execute("DELETE FROM book WHERE id=?",(id,))
        self.conn.commit()

    def update(self,id,name,surname,address,phone):
        self.cur.execute("UPDATE book SET name=?,surname=?,address=?,phone=? WHERE id=?",(name,surname,address,phone,id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()



