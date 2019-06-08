from sqlalchemy import create_engine
import pandas as pd
import sys

id_ = sys.argv[1]
salary = sys.argv[2]
start_date = "'" + sys.argv[3] + "'"
name_first = "'" + sys.argv[4] + " "
name_last = sys.argv[5] + "'"
type_ = "'" + sys.argv[6] + "'"
location = "'" + " ".join(sys.argv[7:]) + "'"

POSTGRES = {
    'user': 'cs421g39',
    'pw': 'g3r9o3u9p',
    'db': 'cs421',
    'host': 'comp421.cs.mcgill.ca',
    'port': '5432'
}

engine = create_engine("postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s" % POSTGRES)
connection = engine.connect()

try:
    connection.execute("INSERT INTO employees( id, location, name, type, start_date, salary) VALUES (" + id_ + "," + location + "," + name_first + name_last + "," + type_ + "," + start_date + "," + salary +")")
    print("New employee added successfully")
except:
    print("OUPS! THE ABOVE ERROR OCCURED.")


connection.close()