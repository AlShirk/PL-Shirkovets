from random import randint

size = int(input("Введите размер матрицы: "))
minimum = int(input("Введите минимальное значение матрицы: "))
maximum = int(input("Введите максимальное значение матрицы: "))

a = []
print("Начальная матрица:")
for i in range(size):
    b = []
    for j in range(size):
        b.append(int(randint(minimum,maximum)))
        print(b[j],end = ' ')
    a.append(b)
    print()

maxi = abs(a[0][0])
imax = jmax = 0

for i in range(size):
    for j in range(size):
        if maxi < abs(a[i][j]):
            imax, jmax = i, j
            maxi = abs(a[i][j])

print("Максимальное значение: ",maxi)
print("Измененная матрица:")
C=[]
for i in range(size):
    D=[]
    if i != imax:
        for j in range(size):
            if j != jmax:
                D.append(a[i][j])
        C.append(D)

for p in C:
    print(*p)
