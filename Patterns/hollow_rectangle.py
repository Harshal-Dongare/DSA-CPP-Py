
# Approach 1
rowCount = int(input("Enter the number of rows: "))
colCount = int(input("Enter the number of cols: "))

for row in range(0, rowCount):
  if (row == 0 or row == rowCount - 1):
    # first row and last row
    for col in range(0, colCount):
      print("*", end=" ")
  else:
    # middle rows
    print("*", end=" ")
    for i in range(0, colCount - 2):
      print(" ", end=" ")
    print("*", end=" ")
  print()
  
# --------------------------------------------------------------------------

# Approach 2
rowCount = int(input("Enter the number of rows: "))
colCount = int(input("Enter the number of cols: "))


if rowCount < 2 or colCount < 2:
  print("Both rows and columns must be at least 2 to form a hollow rectangle.")
else:
  for row in range(rowCount):
    if row == 0 or row == rowCount - 1:
      print("* " * colCount)
    else:
      print("* " + "  "* (colCount - 2) + "* ")