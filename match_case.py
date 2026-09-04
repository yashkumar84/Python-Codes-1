a = int(input("Enter The First Number"))
b = int(input("Enter The Second Number"))
print("Press 1 For Addition")
print("Press 2 For Subtraction ")
print("Press 3 For Multiplication ")
print("Press 4 For Division ")
print("Press 5 For Remainder")
operation = int(input("Enter the Choice Between 1 and 5 4"))

match operation:
    case 1:
        print("Your Choice is 1 For Addition")
        print(a + b)
    case 2:
        print("Your Choice is 2 For Subtraction ")
        print(a - b)
    case 3:
        print("Your Choice is 3 For MULTIPLICATION")
        print(a * b)
    case   4:
        print("Your Choice is 4 For Division ")
        print(a / b)
    case 5:
        print("Your Choice is 5 For Remainder")
        print(a % b)

