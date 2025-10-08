# 9 вариант (по последней цифре из студенческого билета)

import random

arr = []
for i in range (5):
    arr.append(int(input()))

min_mod = min(arr, key=abs) #abs добавлено, чтобы сравнить результаты (-3) = 3 
print("Наименьшее число по модулю: ", min_mod)