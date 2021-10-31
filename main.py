import csv
from db.db import DB
from flask import Flask, render_template, request, redirect, url_for
from pprintpp import pprint


db_name = 'my-users.db'
table_name = 'users'


db = DB(db_name)

db.read_all_entries_from_table(table_name)
db.create_table(table_name)

with open('user_pass.txt', 'r') as f:
    entities = csv.reader(f)
    headers = next(entities)
    user_pass = list(entities)

for i in range(len(user_pass)):
    db.insert_into_table(table_name, i, user_pass[i][0], user_pass[i][1])

data = db.read_all_entries_from_table(table_name)

for row in data:
    print(row)

pprint([table[1] for table in db.list_all_tables()])

# data = db.delete_table(table_name)
# db.delete_db(db_name)

credentials = db.read_all_entries_from_table(table_name)
for credential in credentials:
    print(credential[1])  # TODO: make this with params


app = Flask('Login_Page')


@app.route('/')
def home():
    return 'Hello world!'


@app.route('/welcome')
def welcome():
    return render_template('welcome.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'masteradmin' or request.form['password'] != 'masteradmin':
            error = 'Invalid credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)


app.run()
