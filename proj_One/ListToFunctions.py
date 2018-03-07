def sumList(*lis):
    x = 0
    for i in lis:
        x = x + i
    return x

def getDict(**dic):
    ret = 0
    for key in dic:
        ret += dic(key)
    return ret


toSum = [1,2,3,4,5,6,7,8,9,10]
tot = sumList()
print(tot)

keep = {'k1' : 100,
        'k2' : 200,
        'k3' : 300}
fin =getDict(keep)
