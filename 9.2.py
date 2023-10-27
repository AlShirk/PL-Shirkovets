from random import randint

dlina=int(input("Введите длину каждого массива: "))
ot=int(input("Введите начало диапазона: "))
do=int(input("Введите конец диапазона: "))
A=[randint(ot,do) for i in range(dlina)]
B=[randint(ot,do) for i in range(dlina)]
C=[randint(ot,do) for i in range(dlina)]
print("Полученные 3 массива:\n",A,"\n",B,"\n",C)
def pr(X):
    p=1
    for i in X:
        p*=i
    return p
def sr(S):
    return sum(S)/len(S)
print ("Среднее первого массива: ",sr(A),"\nСреднее второго массива: ",sr(B),"\nСреднее Третьего массива: ",sr(C))
print ("Произведение первого массива: ",pr(A),"\nПроизведение второго массива: ",pr(B),"\nПроизведение Третьего массива: ",pr(C))    


        
