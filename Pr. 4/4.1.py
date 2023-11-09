a, b = int(input('введите число A: ')), int(input('введите число B: '))
if a > b:
    print("Сделайте A < или = B")
for i in range(a, b + 1):
    print(i)
