import sqlite3 as lite


# functionality goes here

class DatabaseManage(object):
    def __init__(self):
        global con
        try:
            con = lite.connect('Courses.db')
            with con:
                cur = con.cursor()
                cur.execute("CREATE TABLE IF NOT EXISTS course(Id INTEGER PRIMARY KEY AUTOINCREMENT,"
                            "name TEXT, description TEXT, price TEXT,is_private TEXT)")

        except Exception:
            print("Unable to Create a DB !!!!!")
    def insert_data(self, data):
        try:
            with con:
                cur = con.cursor()
                cur.execute("INSERT INTO course(name,description,price,is_private) VALUES (?,?,?,?)", data)
                return True
        except Exception:
            print("Unable to Connect a DB !!!!!")


    def fetch_data(self):
        try:
            with con:
                cur = con.cursor()
                cur.execute("SELECT * FROM course")
                return cur.fetchall()
        except Exception:
            print("Unable to Connect a DB !!!!!")
    def delete_data(self, id):
        try:
            with con:
                cur = con.cursor()
                sql = "DELETE FROM course WHERE Id = ?"
                cur.execute(sql, [id])
                return True
        except Exception:
            print("Unable to Connect a DB !!!!!")


