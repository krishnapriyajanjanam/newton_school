def diogonalSum(mat, n):

    primary = 0
    secondary = 0
    for i in range(0, n):
        primary+= mat[i][i]
        secondary += mat[i][n - i - 1]
         
    print("Primary Diagonal Sum:", primary)
    print("Secondary Diagonal Sum:", secondary)
 
n=int(input()) # size of the matrix
mat=[]
for i in range(n):
    mat.append(list(map(int,input().split()))) #reading Matrix
diogonalSum(mat,n)