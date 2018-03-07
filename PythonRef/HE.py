def reverse(torev):
    m = ""
    for i in torev[::-1]:
        m = m + i
    return m

x = int(input())
while x > 0:
    st = input()
    is_what = ''
    isrev = ''
    strev = reverse(st)
    if st == strev:
        isrev = 'YES'
    else:
        isrev = 'NO'
    if isrev == 'YES':
        if len(st)%2 == 0:
            is_what = 'EVEN'
        else:
            is_what = 'ODD'
    print(isrev, is_what)
    x = x-1