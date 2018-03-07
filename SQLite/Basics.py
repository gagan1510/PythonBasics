import sqlite3
import time
import datetime
import random
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import style

style.use('fivethirtyeight')

conn = sqlite3.connect('tutorial.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS stuffplot(unix REAL, date TEXT, key TEXT, value REAL)')

def data_entry():
    c.execute("INSERT INTO stuffplot VALUES(989995, '2017-02-04', 'Gagan', 18)")
    conn.commit()
    c.close()
    conn.close()

def dynamic_data_entry():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    keyword = 'Google'
    value = random.randrange(0,100)
    c.execute('INSERT INTO stuffplot VALUES(?, ?, ?, ?)',
              (unix, date, keyword, value))
    conn.commit()

def read_from_db():
    c.execute('SELECT * FROM stuffplot')
    for row in c.fetchall():
        print(row)

def graph_data():
    c.execute('SELECT unix, value FROM stuffplot')
    dates = []
    values = []
    for row in c.fetchall():
        dates.append(datetime.datetime.fromtimestamp(row[0])) # this converts the unix to the official format
        values.append(row[1])
    plt.plot(dates, values, color = 'g', linewidth = 1 )
    plt.show()

# for i in range(50):
#     dynamic_data_entry()

graph_data()

c.close()
conn.close()