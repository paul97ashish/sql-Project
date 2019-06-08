from sqlalchemy import create_engine
import pandas as pd
import sys

date = "'" + sys.argv[1] + "'"
space_id = sys.argv[2]

POSTGRES = {
    'user': 'cs421g39',
    'pw': 'g3r9o3u9p',
    'db': 'cs421',
    'host': 'comp421.cs.mcgill.ca',
    'port': '5432'
}

engine = create_engine("postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s" % POSTGRES)

connection = engine.connect()
result = pd.DataFrame(connection.execute("SELECT p.card_holder, p.number_of_guests, room_number, start_date, end_date FROM parties p, occupies o, rentablespaces r WHERE p.booking_id = o.booking_id and o.space_id = r.space_id and start_date = " + date + " and room_number = " + space_id))
print(result.head())
# try:
#     result = pd.DataFrame(connection.execute("SELECT p.card_holder,p.number_of_guests,room_number, start_date,end_date FROM parties p,occupies o,rentablespaces r WHERE p.booking_id=o.booking_id and o.space_id = r.space_id and start_date = " + date + " and room_number = " + space_id))
#     result.columns = ['Card Holder', 'Number of Guests', 'Space ID', 'Start Date', 'End Date']
#     print(result.head())

# except:
#     print("OUPS! THE ABOVE ERROR OCCURED.")

connection.close()