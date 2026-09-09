#List

a = [2 ,  4, 5, 6 , 3]
print(a)

print(a[4])

a.append(7)
print(a)
#[2,  3, 4, 5, 6, 7]
a.insert(1 , 2)
print(a)

print(len(a))

print(a.count(2))

a.extend([20 , 30 , 40])
print(a)

# a.clear()

print(a.pop(2))
print(a)

a.remove(2)
print(a)

print(a.index(2))


# b = a.copy()
b = a
a.pop()
print(a)
print(b)


a.sort(reverse=True)
print(a)

a.reverse()
print(a)

for i in a:
    print(i)

