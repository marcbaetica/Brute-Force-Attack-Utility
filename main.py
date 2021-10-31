import string
from db.db import DB
from pprintpp import pprint
from random import choice
from time import sleep


db_name = 'my-users.db'

db = DB(db_name)

new_table = 'users_' + ''.join([choice(string.ascii_lowercase) for _ in range(10)])
db.read_all_entries_from_table(new_table)
db.create_table(new_table)

db.insert_into_table(new_table, 1, 'Alice', 26)
db.insert_into_table(new_table, 2, 'Alex', 28)
db.insert_into_table(new_table, 3, 'Cristina', 27)
data = db.read_all_entries_from_table(new_table)

for row in data:
    print(row)

pprint([table[1] for table in db.list_all_tables()])

data = db.delete_table(new_table)
db.delete_db(db_name)
