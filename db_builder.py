import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE
courses = csv.DictReader(open("courses.csv"))
peeps = csv.DictReader(open("peeps.csv"))

c.execute('CREATE TABLE courses (code str,mark int,id int)')
for row in courses:
	c.execute('INSERT INTO courses VALUES ("' + row['code'] + '",' + row['mark'] + ',' + row['id'] + ');')

c.execute('CREATE TABLE peeps (name str,age int,id int)')
for row in peeps:
	c.execute('INSERT INTO peeps VALUES ("' + row['name'] + '",' + row ['age'] + ',' + row['id'] + ');')


#==========================================================
db.commit() #save changes
db.close()  #close database


