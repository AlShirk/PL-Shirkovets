n=int(input("Введите длину массива\n"))
S=[]
for i in range(n):
    print("Введите", i, "элемент:")
    S.append(int(input()))
Unikalnie=list(set(S))
povtor=[]
for i in S:
    if S.count(i) > 1 and i not in povtor:
        povtor.append(i)
print("Полученный массив\n", povtor)
