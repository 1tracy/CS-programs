def addCommas(n):
    s = str(n)
    if len(s)<=3:
        return s
    else:
        return addCommas(s[:-3])+","+s[-3:]

num = addCommas(222333444)
print(num)
