import sqlite3

conn = sqlite3.connect("studata.db")

crs = conn.cursor()


a:int = int(input("enter no of student:"))
for i in range(a):
    roll = input("roll no.:")
    initial = input("Initial.:")
    Fname = input("Fname.:")
    Lname = input("Lname.:")
    Cls = 12
    Sec = "A1"
    group = input("group.:")
    sql_com = """INSERT INTO 'st_det' (`Sno`, `Rollno`, `Initial`, `Fname`, `Lname`, `class`, `section`, `course`) 
    VALUES (NULL, "{roll}", "{initial}", "{Fname}", "{Lname}", {Cls}, "{Sec}", "{group}");"""
    crs.execute(sql_com.format(roll=roll , initial=initial , Fname = Fname , Lname = Lname , Cls = Cls , Sec = Sec , group = group))
    conn.commit()
