# *****
# *   *
# *   *
# *   *
# *****
num = 5
for row in range(num):
    for star in range(num):
        if row == 0 or row == num - 1 or star == 0 or star == num - 1:
            print("*" , end="")
        else:
            print(" " , end="")
    print()