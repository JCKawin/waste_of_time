import sqlite3
conn = sqlite3.connect("studata.db")
crs = conn.cursor()

crs.execute("UPDATE st_det SET D_O_B = 2007-10-03 where Fname = 'KAWIN' ;")
conn.commit()

