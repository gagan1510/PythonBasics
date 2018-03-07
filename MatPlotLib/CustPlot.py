import matplotlib.pyplot as plt
import numpy as np
import urllib.request
import matplotlib.dates as mdates


def bytespdate2num(fmt, encoding='utf-8'):
    strconverter = mdates.strpdate2num(fmt)
    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)
    return bytesconverter


def graph_data(stock):
    fig = plt.figure()
    ax1 = plt.subplot2grid((1, 1), (0, 0))  

    stock_price_url = 'https://pythonprogramming.net/yahoo_finance_replacement'
    source_code = urllib.request.urlopen(stock_price_url).read().decode()
    stock_data = []
    split_source = source_code.split()

    for line in split_source:
        split_line = line.split(',')
        # print(split_line)
        if len(split_line) == 7:
            if 'Date' not in line:
                stock_data.append(line)

    date, openp, highp, lowp, closep, adjustedp, volume = np.loadtxt(stock_data,
                                                                     delimiter=',',
                                                                     unpack=True,
                                                                     converters={0: bytespdate2num('%Y-%m-%d')})

    ax1.plot_date(date, closep, '-',label='price', linewidth = 0.1)

    # ax1.fill_between(date, closep, 360, alpha = 0.3) # shade about 360

    ax1.plot([], [], color = 'g', label = 'Gain')

    ax1.plot([], [], color = 'r', label = 'Loss')

    ax1.fill_between(date, closep, 100, where = (closep>100), facecolor = 'g', alpha = 0.6) # where limits the fill upto the condition

    ax1.fill_between(date, closep, 100, where = (closep<100), facecolor = 'r', alpha = 0.6) # where limits the fill upto the condition

    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)  # to tilt the label so they don't get overlapped

    ax1.grid(True)  # , color = 'g', linestyle = '-')
    ax1.xaxis.label.set_color('c')
    ax1.yaxis.label.set_color('r')
    # ax1.set_yticks([0,25,50,75]) # to limit the set of displaying the numbers on the y-axis
    plt.xlabel("dates")
    plt.ylabel("closing price")
    plt.title(stock)
    plt.legend()
    plt.subplots_adjust(left=0.09, bottom=0.18, right=0.94, wspace=0.2, hspace=0)
    plt.show()


graph_data('TSLA')