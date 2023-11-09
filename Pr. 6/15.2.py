n=int(input("Введите длину массива\n"))
S=[]
for i in range(n):
    print("Введите", i, "элемент:")
    S.append(int(input()))
drugoi=[]
for i in S:
    if i%2!=0:
        drugoi.append(i)
if len(drugoi)==0:
    print("В массиве нет нечетных чисел")
else:
    drugoi.sort()
    drugoi.reverse()
    print("Полученный массив в порядке убывания элементов\n",drugoi)
