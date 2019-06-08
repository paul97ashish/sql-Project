from sqlalchemy import create_engine
import pandas as pd
import sys

name = " ".join(sys.argv[1:])

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
    result = pd.DataFrame(connection.execute("SELECT * FROM employees WHERE name = '" + name + "'"))
    result.columns = ['ID', 'Location', 'Name', 'Type', 'Salary', 'Date']
    print(result.head(200))
except:
    print("OUPS! THE ABOVE ERROR OCCURED.")

connection.close()