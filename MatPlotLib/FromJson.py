import json
import matplotlib.pyplot as plt

def graph_show():
    final = []
    dates = []
    openp = []

    with open('query.json') as json_file:
        json_data = json.load(json_file)
        # print(json_data)
        for keys in json_data['Time Series (1min)']:
            print(keys)
            dates.append(keys)
            openp.append(json_data[keys]['1. open'])
    print(openp)

graph_show()