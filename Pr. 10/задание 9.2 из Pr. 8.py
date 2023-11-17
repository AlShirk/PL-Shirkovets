file = open("D:\PL-Shirkovets\Pr. 10\Ширковец_УБ-32_vvod.txt", "r")
A=[]
for line in file:
    A.append(line.split())
file.close()        

maxi = abs(int(A[0][0]))
imax = jmax = 0

for i in A:
    for j in range(len(i)):
        if maxi < abs(int(i[j])):
            imax, jmax = i, j
            maxi = abs(int(i[j]))

C=[]
for i in A:
    D=[]
    if i != imax:
        for j in range(len(i)):
            if j != jmax:
                D.append(i[j])
        C.append(D)


with open("D:\PL-Shirkovets\Pr. 10\Ширковец_УБ-32_vivod.txt", "w", encoding="utf-8") as fvivod:
    fvivod.write("Максимальное значение:")
    fvivod.write(str(maxi))
    fvivod.write("\n")
    fvivod.write("Измененная матрица:")
    fvivod.write("\n")
    for i in C:
        for j in i:
            fvivod.write(j)
            fvivod.write(" ")
        fvivod.write("\n")