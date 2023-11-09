A=str(input("Введите строку: "))
def zmn(X):
    X=' '.join(reversed(X.split()))
    return X
print(zmn(A))