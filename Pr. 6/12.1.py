s = [11, 21, 5, 45, 58, 63, 74, 81, 92, 13] 
min_n = max(s) 
for i in range(len(s)):
    if s[i] % 2 != 0:  
        if min_n >= s[i]: 
            min_n = s[i]
print('Наименьший нечетный элемент списка:', min_n)