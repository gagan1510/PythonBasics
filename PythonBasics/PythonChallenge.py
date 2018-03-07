import pickle
import urllib.request

x = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/banner.p")
f = open("pc.pickle", "wb")
pickle.dump(x.read(), f)
f.close()

f = open("pc.pickle", "rb")
dic = pickle.load(urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/banner.p"))
# print(dic)

for a in dic:
    print("".join([k*v for k,v in a]))
f.close()