from sqlalchemy import create_engine
import pandas as pd
import sys

variable = "'" + sys.argv[1] + "'"

POSTGRES = {
    'user': 'cs421g39',
    'pw': 'g3r9o3u9p',
    'db': 'cs421',
    'host': 'comp421.cs.mcgill.ca',
    'port': '5432'
}

engine = create_engine("postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s" % POSTGRES)
connection = engine.connect()

print("SELECT space_id, status FROM RentableSpaces WHERE status = " + variable)
try:
    result = pd.DataFrame(connection.execute("SELECT space_id, status FROM RentableSpaces WHERE status = " + variable))
    result.columns = ['ID', 'Status']
    print(result.head(200))

except:
    print("OUPS! THE ABOVE ERROR OCCURED.")


connection.close()