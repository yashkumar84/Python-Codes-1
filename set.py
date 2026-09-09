s = {1 ,2 ,3 , 4, 5, 1}
a = {1 , 2}

print(s)

print(s.add(10))
print(s)
s.add(1)
print(s)
s.remove(10)
print(s)

uni = s.union(a)
print(uni)

inter = s.intersection(a)
print(inter)

diff = a.difference(s)
print(diff)

symd = s.symmetric_difference(a)
print(symd)
print(a.issubset(s))
print(4 in s)
print(s)
print(s.pop())
s.pop()
print(s)

