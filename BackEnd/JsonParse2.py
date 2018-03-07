import json
import mysql.connector
import MySQLdb

with open('query.json') as f:
    times = []
    highp = []
    closep = []
    volume = []
    lowp = []
    openp = []
    data = json.load(f)
    for key in data['Time Series (1min)']:
        # print(key, end=':')
        x = data['Time Series (1min)'][key]
        times.append(key)
        openp.append(float(x['1. open']))
        highp.append(x['2. high'])
        lowp.append(x['3. low'])
        closep.append(x['4. close'])
        volume.append(x['5. volume'])


    db = MySQLdb.connect(host = 'localhost',
                         user = 'root',
                         passwd = 'gagankainth',
                         db = 'stock_data')

    cur = db.cursor()
    cur.execute('drop table stock_info;')
    cmd = 'create table stock_info(Date DATETIME, Open FLOAT, High FLOAT, Low FLOAT, Close FLOAT, Volume INT);'
    cur.execute(cmd)
    for key in data['Time Series (1min)']:
        try:
            x = data['Time Series (1min)'][key]
            cmd = 'insert into stock_data values(' + str(key) + ',' + x['1. open'] + ',' + x['2. high'] + ',' + x['3. low'] + ',' + x['4. close'] + ',' + x['5. volume']+');'
            cur.execute(cmd)
        except Exception as e:
            print(e)
        # print(cmd)
    db.commit()