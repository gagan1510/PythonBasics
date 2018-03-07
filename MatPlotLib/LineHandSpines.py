import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import urllib.request

def byteupdate2num(fmt, encoding = 'utf-8'):
    strconverter = mdates.strpdate2num(fmt)
    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)
    return bytesconverter

def graph_plot(stock):
    fig = plt.figure()
    ax1 = plt.subplot2grid((1,1),(0,0))
    
    url_stock = 'https://pythonprogramming.net/yahoo_finance_replacement'
    ub = urllib.request.urlopen(url_stock).read().decode()
    stock_data = []
    split_source = ub.split()
    for line in split_source:
        split_line = line.split(',')
        if len(split_line) == 7:
            if 'Date' not in line:
                stock_data.append(line)
    # print(stock_data)
    date, openp, highp, lowp, closep, adjustedp, volume = np.loadtxt(stock_data,
                                                                    delimiter = ',',
                                                                    unpack = True,
                                                                    converters = {0 : byteupdate2num('%Y-%m-%d')})

    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)

    
    ax1.spines['left'].set_color('k') # to change the color of the axis
    ax1.spines['top'].set_visible(False) # to change the visibility of the axis
    ax1.spines['right'].set_visible(False) 

    ax1.spines['left'].set_linewidth(5) # to change the width of the axis

    ax1.tick_params(axis = 'x', colors = '#f06215')

    plt.xlabel('Date')
    plt.ylabel('Price')    
    ax1.plot_date(date, closep, '-', label = 'Price', linewidth = 0.5)
    
    ax1.axhline(closep[500], color = 'k', linewidth = 5)
    
    plt.show()

graph_plot('tsla')