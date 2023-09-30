N=input("Введите количество чисел Фибоначчи: ")
F=[0, 1]

while len(F) < int(N):
    NewNomber=F[-1]+F[-2]
    F.append(NewNomber)

print("Сумма чисел Фибоначчи:", sum(F))