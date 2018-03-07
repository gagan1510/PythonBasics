import matplotlib.pyplot as plt
import urllib.request
import matplotlib.dates as mdates
import datetime as dt
import numpy as np
import csv


def bytespdate2num(fmt, encoding='utf-8'):
    strconverter = mdates.strpdate2num(fmt)
    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)
    return bytesconverter

def graph_show():
    total_stock = []
    # with open('down.csv') as csvfile:
    #     lines = csvfile.read().split('\n')
    # for each in lines:
    #     each_diff = each.split(',')
    #     if len(each_diff) == 6:
    #         if 'open' not in each:
    #             total_stock.append(each_diff)

    timestamp, openp, highp, lowp, closep, volume = np.loadtxt('down.csv',
                                                               delimiter=',',
                                                               unpack=True,
                                                               converters={0 : bytespdate2num("%Y-%m-%d %H:%M:%S")})

    plt.plot_date(timestamp, closep, '-', linewidth = 0.5)
    plt.show()

graph_show()