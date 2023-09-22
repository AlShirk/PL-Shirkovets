import math
print("Запишите подряд 3 стороны треугольника для формулы Герона")
A=float(input())
B=float(input())
C=float(input())
p=(A+B+C)/2
if A+B>C and B+C>A and C+A>B:
    G=math.sqrt(p*(p-A)*(p-B)*(p-C))
    print("Площадь треугольника:", G)
else:
    print("Это не треугольник")


