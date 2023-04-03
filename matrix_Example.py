ROW = int(input("enter number of rows:"))
Col = int(input("enter number of Columns:"))
matrix=[]
print("Enter the values in row:")

for i in range(ROW):
    a=[]
    for j in range(Col):
        a.append(int(input()))
    matrix.append(a)
for i in range(ROW):
    for j in range(Col):
        print(matrix[i][j],end=" ")
    print()
