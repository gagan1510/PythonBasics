import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.finance import candlestick_ohlc
import datetime as dt
import csv
import numpy as np
from matplotlib import style

# style.use('fivethirtyeight')

def bytespdate2num(fmt, encoding='utf-8'):
    strconverter = mdates.strpdate2num(fmt)
    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)
    return bytesconverter

def graph_plot(stock):

    ax1 = plt.subplot2grid((1,1),(0,0))
    timestamp, openp, highp, lowp, closep, adjustedp, volume = np.loadtxt('stockdata.txt',
                                                               delimiter=',',
                                                               unpack=True,
                                                               converters={0 : bytespdate2num('%Y-%m-%d')})

    x = 0
    y = len(timestamp)
    ohlc = []

    while x < y:
        append_me = timestamp[x], openp[x] , highp[x], lowp[x], closep[x], adjustedp[x], volume[x]
        ohlc.append(append_me)
        x += 1

    candlestick_ohlc(ax1, ohlc)

    plt.show()

graph_plot('TSLA')