X=int(input("Введите натуральнольное число X: "))
N=int(input("Введите натуральнольное число N: "))

def fctrl(c):
    if c==0:
        return 1
    return fctrl(c-1)*c

print("Результат выражения x^n/n!")
print(X**N/fctrl(N))