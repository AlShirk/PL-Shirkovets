
def max_posl():
    n=int(input())
    if n == 0:
        return 0
    m=max_posl()
    if n > m:
        return n
    else:
        return m
    

print("Максимальная последовательности: ",max_posl())