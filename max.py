list = [20 , 40 , 20 , 90 , 40 , 10 , 30]

# print(max(list))

maxIndex = 0
for i in range(len(list)):
    if list[i] > list[maxIndex]:
        maxIndex = i

minIndex = 0
for i in range(len(list)):
    if list[i] < list[minIndex]:
        minIndex = i

print("min" , minIndex)
print("max", maxIndex)
temp = list[minIndex]
list[minIndex] = list[maxIndex]
list[maxIndex] = temp

print(list)