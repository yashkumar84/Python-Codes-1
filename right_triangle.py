# *
# **
# * *
# *  *
# *****

num = 5
for row in range(1 , num + 1):
    for star in range(1 , row + 1):
        if row == 1 or row == num or star == 1 or star == row:
            print("*" , end ="")
        else:
            print(" " , end="")
    print()