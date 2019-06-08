from sqlalchemy import create_engine
import pandas as pd
import sys

location = "'" + sys.argv[1] + "'"
area = sys.argv[2]

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
    connection.execute("INSERT INTO hotels VALUES ( " + location + ", " + area + ")")
    print("New Hotel added successfully")
except:
    print("OUPS! THE ABOVE ERROR OCCURED.")


connection.close()