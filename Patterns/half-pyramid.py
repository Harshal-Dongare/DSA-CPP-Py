
""" 
Half Pyramid
*
* *
* * *
* * * *
* * * * *
"""


# Approach 1
for row in range(9):
  for col in range(row+1):
    print("*", end=" ")
  print()  
  
  
# Approach 2
for row in range(7):
  print("* " * (row + 1))


# Approach 3
for row in range(1, 8):
  print(" ".join(["*"] * row))