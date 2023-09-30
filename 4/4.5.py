N=input("Введите n для алгоритма 1^3+2^3+3^3+...+n^3: ")
F=int(1)
S=int(0)
while F < int(N) or F == int(N):
    S += F**3
    F += 1
print("Ответ:", S)