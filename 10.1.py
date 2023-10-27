from random import randint

N=randint(210,231)
cnt=0
def abc(a,b,c):
    if a!=b and b!=c and a!=c:
        return True
for i in range(100,N+1):
    if abc(i//100,(i//10)%10,i%10):
        cnt+=1
#        print(i) # Если нужно просмотреть последовательность
print(cnt)