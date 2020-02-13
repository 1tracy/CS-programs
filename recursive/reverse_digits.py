"""
Create recursive method that returns the
result of reversing the digits in integer n
"""
def rev(num):
    num = str(num)
    if len(num) < 1:
        return num
    else:
        return (num[-1] + rev(num[:-1]))

number = rev(12345)
print(number)
