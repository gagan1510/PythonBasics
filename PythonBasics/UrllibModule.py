import urllib.request
import urllib.parse

x = urllib.request.urlopen('https://www.google.com')
# print(x.read())

url = 'http://www.pythonprogramming.net'
values = {'s' : 'basic',
          'submit' : 'search'}

data = urllib.parse.urlencode(values) # encodes the values as it should be in the url
data = data.encode('utf-8') # encodes the data in the utf-8 form

req = urllib.request.Request(url, data) # it passes the encoded data to the url
resp = urllib.request.urlopen(req) # visiting the url
respData = resp.read()

# print(respData)

try:
    x = urllib.request.urlopen('https://www.google.com/search?q=test')
    print(x.read())

except Exception as e:
    print(str(e))

try:
    url1 = urllib.request.urlopen('https://www.google.com/search?q=test')
    headers = {}
    headers['User-Agent'] =  'Mozilla/4.0'
    #'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'
    # from the User-Agent, the website will not be able to know that we are using a program on their website
    # ATTEMPT TO FOOL GOOGLE
    req1 = urllib.request.Request(url, headers=headers)
    resp1 = urllib.request.urlopen(req1)
    respData1 = resp1.read()
    saveFile = open('headers.txt', 'w')
    saveFile.write(str(respData))
    saveFile.close()

except Exception as e:
    print(str(e))