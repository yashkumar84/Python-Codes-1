num = 123456   #623451
even_sum = 0 
odd_sum = 0
isEven = False
while num>0:
    rem = num%10
    num=num//10
    if isEven:
        even_sum+=rem
    else:
        odd_sum+=rem
    isEven = not isEven
        
print("Even SUM : " ,even_sum)
print("Odd SUM : " ,odd_sum)