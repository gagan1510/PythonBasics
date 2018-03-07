import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.finance import candlestick_ohlc
import matplotlib.dates as mdates
import numpy as np
import urllib.request
import datetime as dt

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

        font_dict = {'family': 'Monospace',
                     'color': 'darkred',
                     'size': 8}

        candlestick_ohlc(ax1, ohlc, width = 1, colorup = '#77d879', colordown = '#db3f3f')

        ax1.grid(True)

        ax1.text(date[195], closep[0], 'Example', fontdict = font_dict) # at which date we want the text to be shown, the price at which the text is to be shown

        ax1.annotate('Big News', (date[210], highp[2]),
                     xytext = (0.8, 0.9), textcoords = 'axes fraction',
                     arrowprops = dict(facecolor = 'grey', color = 'grey'))

        bbox_props = dict(boxstyle = 'round', fc = 'w', ec = 'k', lw = 1)

        ax1.annotate(str(closep[0]), (date[0], closep[0]),
                     xytext = (date[0] , closep[0]), bbox = bbox_props)

        for label in ax1.xaxis.get_ticklabels():
            label.set_rotation(45)

        ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.title('Stock YFA')

        plt.show()

graph_data()