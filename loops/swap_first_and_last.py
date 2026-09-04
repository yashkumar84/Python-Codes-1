# def countDigits(num):
#     count = 0
#     while num > 0:
#         count += 1
#         num //= 10
#     return num


num = 12345
copy = num

last = num % 10   #---- last = 5
count = 0
while copy > 0:
    count += 1
    copy //= 10
num //= 10 #1234
divisor = 10 ** (count - 2)
middle = num % divisor
first = num // divisor

last = last * divisor  #---- 5 * 1000 = 5000
last += middle  #---- 5000 + 234 = 5234 
last *= 10   #----- 5234 * 10 = 52340
last += first   # 52340 + 1 = 52341
print(last)
    