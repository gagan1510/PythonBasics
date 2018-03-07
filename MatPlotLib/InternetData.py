import matplotlib.pyplot as plt
import numpy as np
import urllib.request
import matplotlib.dates as mdates

def bytespdate2num(fmt, encoding = 'utf-8'):
    strconverter = mdates.strpdate2num(fmt)
    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)
    return bytesconverter

def graph_data(stock):
    fig = plt.figure()
    ax1 = plt.subplot2grid((1,1), (0,0))
    
    stock_price_url = 'https://pythonprogramming.net/yahoo_finance_replacement'
    source_code = urllib.request.urlopen(stock_price_url).read().decode()
    stock_data = []
    split_source = source_code.split()

    for line in split_source:
        split_line = line.split(',')
        # print(split_line)
        if len(split_line) == 7:
            # if 'Date' not in split_line:
            stock_data.append(line)

    print(stock_data)

    date, openp, highp, lowp, closep, adjustedp, volume = np.loadtxt(stock_data,
                                                                     delimiter=',',
                                                                     unpack=True,
                                                                     converters={0 : bytespdate2num('%Y-%m-%d')})

    ax1.plot_date(date, closep, '-', label = 'price')

    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)              # to tilt the label so they don't get overlapped

    ax1.grid(True)#, color = 'g', linestyle = '-')

    plt.xlabel("dates")
    plt.ylabel("closing price")
    plt.title("Interesting Graph\nCheck this out")
    plt.legend()
    plt.subplots_adjust(left = 0.09, bottom = 0.18, right = 0.94, wspace = 0.2, hspace = 0)
    plt.show()

graph_data('TSLA')