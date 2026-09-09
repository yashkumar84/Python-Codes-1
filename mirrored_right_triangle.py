#     *
#    **
#   ***
#  ****
# *****

# SPACE ---- 
# 1 - 4
# 2 - 3
# 3 - 2
# 4 - 1
# 5 - 0
# n - row 

# STARS --- 
# 1 - 1
# 2 - 2
# 3 - 3
# 4 - 4
# 5 - 5

# star <= row

n = 5
for row in range(1 , n + 1):
    for space in range(1 , n - row + 1):
        print(" " , end="")
    for star in range(1 , row + 1):
        print("*" ,end="")
    print()