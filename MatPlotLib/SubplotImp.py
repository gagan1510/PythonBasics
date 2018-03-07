import matplotlib.pyplot as plt
from matplotlib.finance import candlestick_ohlc
from matplotlib import style
import matplotlib.dates as mdates
import numpy as np
import matplotlib.ticker as mticker
import datetime as dt
import random

style.use('fivethirtyeight')

MA1 = 10
MA2 = 30


def moving_average(values, window):
    weights = np.repeat(1.0, window)/window
    smas = np.convolve(values, weights, 'valid')
    return smas


def high_minus_low(highs,lows):
    return highs-lows


def bytespdate2num(fmt, encoding='utf-8'):
    strconverter = mdates.strpdate2num(fmt)
    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)
    return bytesconverter


def graph_data():
    with (open('monthly_MSFT.csv')) as csvFile:

        ax1 = plt.subplot2grid((6,1), (0,0), rowspan=1, colspan=1)
        plt.title("Monthly MSFT")
        plt.ylabel('H-L')

        ax2 = plt.subplot2grid((6,1), (1,0), rowspan=4, colspan=1, sharex = ax1)
        plt.ylabel('Price')

        ax2v = ax2.twinx()

        ax3 = plt.subplot2grid((6, 1), (5, 0), rowspan=1, colspan=1, sharex = ax1)
        plt.ylabel('MAvgs')

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

        h_l = list(map(high_minus_low, highp, lowp))

        ax1.plot(date, h_l, '-')
        ax1.yaxis.set_major_locator(mticker.MaxNLocator(nbins = 5, prune = 'lower'))

        while x < y:
            append_me = date[x], openp[x], highp[x], lowp[x], closep[x]
            ohlc.append(append_me)
            x += 1

        ma1 = moving_average(closep, MA1)
        ma2 = moving_average(closep, MA2)

        start = len(date[MA2-1:])

        font_dict = {'family': 'Monospace',
                     'color': 'darkred',
                     'size': 8}

        # ax1.plot()

        candlestick_ohlc(ax2, ohlc, width=0.4, colorup='g', colordown='r')

        ax2.yaxis.set_major_locator(mticker.MaxNLocator(nbins=7, prune='lower'))
        # ax1.grid(True)
        #
        # ax1.text(date[195], closep[0], 'Example', fontdict = font_dict) # at which date we want the text to be shown, the price at which the text is to be shown
        #
        ax2.annotate('Bad News', (date[210], highp[2]),
                     xytext = (0.8, 0.9), textcoords = 'axes fraction',
                     arrowprops = dict(facecolor = 'grey', color = 'grey'))
        #
        bbox_props = dict(boxstyle = 'round', fc = 'w', ec = 'k', lw = 1)
        #
        ax2.annotate(str(closep[0]), (date[0], closep[0]),
                     xytext = (date[0] , closep[0]), bbox = bbox_props)


        ax2.fill_between(date[-start:], 0,  adjustedp[-start:], facecolor = '#0079a3', alpha = 0.4)
        ax2v.axes.yaxis.set_ticklabels([])
        ax2v.grid(False)
        ax2v.set_ylim(0,6*adjustedp.max()) # setting the limit to 3 times less than the maximum adjustedp


        for label in ax2.xaxis.get_ticklabels():
            label.set_rotation(45)

        ax3.plot(date[-start:], ma1[-start:], linewidth = 1)
        ax3.plot(date[-start:], ma2[-start:], linewidth = 1)

        ax3.yaxis.set_major_locator(mticker.MaxNLocator(nbins=5, prune='upper'))

        ax3.fill_between(date[-start:], ma2[-start:], ma1[-start:],
                         where=(ma1[-start:] < ma2[-start:]),
                         facecolor = 'r', edgecolor = 'r', alpha = 0.5)

        ax3.fill_between(date[-start:], ma2[-start:], ma1[-start:],
                         where=(ma1[-start:] > ma2[-start:]),
                         facecolor='g', edgecolor='g', alpha=0.5)



        ax3.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        for label in ax3.xaxis.get_ticklabels():
            label.set_rotation(45)

        plt.setp(ax1.get_xticklabels(), visible = False)
        plt.setp(ax2.get_xticklabels(), visible = False)

        # ax2.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        # plt.xlabel('Date')
        # plt.ylabel('Price')
        # plt.title('Stock YFA')

        plt.show()


graph_data()