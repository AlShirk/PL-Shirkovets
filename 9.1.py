N=int(input("Введите число: "))
def dlyavichitania(x):
    sumcifr=0
    while x!=0:
        sumcifr+=x%10
        x=x//10
    return sumcifr
cnt=0
while N!=0:
    N=N-dlyavichitania(N)
    cnt+=1
#    print(N) # Строка для просмотра последовательности
print("Действий, пока число не стало ноль: ",cnt)