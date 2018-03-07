import matplotlib.pyplot as plt
import urllib.request
import matplotlib.dates as mdates
from matplotlib.finance import candlestick_ohlc
import datetime as dt
from matplotlib import style
import numpy as np


style.use('fivethirtyeight')

def bytespdate2num(fmt, encoding='utf-8'):
    strconverter = mdates.strpdate2num(fmt)
    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)
    return bytesconverter


def graph_data():
    with (open('monthly_MSFT.csv')) as csvFile:
        ax1 = plt.subplot2grid((1,1),(0,0))
        # stock_url = 'https://pythonprogramming.net/yahoo_finance_replacement'
        # source_data = urllib.request.urlopen(stock_url).read().decode()
        stock_data = []
        source_data = csvFile.read()
        split_source = source_data.split('\n')


        for line in split_source:
            split_line = line.split(',')
            if len(split_line) == 6:
                if 'Date' not in line:
                    stock_data.append(line)

        date, openp, highp, lowp, closep, adjustedp = np.loadtxt(stock_data,
                                                                 delimiter=',',
                                                                 unpack=True,
                                                                 converters={0: bytespdate2num('%Y-%m-%d')})

        x = 0
        y = len(date)
        ohlc = []

        while x < y:
            append_me = date[x], openp[x], highp[x], lowp[x], closep[x]
            ohlc.append(append_me)
            x += 1

        # ax1.plot_date(date, openp, '-', linewidth = 1)
        # ax1.plot_date(date, highp, '-', linewidth = 1)
        candlestick_ohlc(ax1, ohlc, width = 0.4, colorup = '#77d879', colordown = '#db3f3f')

        for label in ax1.xaxis.get_ticklabels():
            label.set_rotation(45)

        ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.title('Stock YFA')

        plt.show()

graph_data()