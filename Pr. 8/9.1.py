n=int(input("Введите n для матрицы размером n*n:\n"))

A=[]
for i in range(n):
    B=[]
    for j in range(n):
        print("Введите[",i,",",j,"]элемент")
        B.append(int(input()))
    A.append(B)

k=int(input("Введите кратное k: "))
cnt=0
C=[]
for i in range(n):
    for j in range(n):
        if A[i][j]%k==0:
            cnt+=1
            C.append(A[i][j])

for i in range(n):
    for j in range(n):
        print(A[i][j], end=" ")
    print()
print("Количество чисел кратных k:", cnt,"\nНаибольшее из них:", max(C))
