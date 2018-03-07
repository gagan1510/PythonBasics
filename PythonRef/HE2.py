def add(l):
    m = ''
    for i in l:
        m = m + i
    return m

vow = ['a', 'e', 'i', 'o', 'u']
to = input()
tof = []
for ch in to:
    if ch in vow and ch not in tof:
        tof.append(ch)

x = add(tof)
print(len(x))