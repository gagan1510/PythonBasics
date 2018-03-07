import io

f = io.open("abc.txt", "wt", encoding = "utf-8")
f.write(u"Imagine non-English language here")
f.close()

text = io.open("abc.txt", "r", encoding="utf-8").read()
print(text)