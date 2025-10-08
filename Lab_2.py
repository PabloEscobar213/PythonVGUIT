import random

x = int(input())

arr1 = [random.randint(0, 100) for _ in range(10)]
arr2 = [random.randint(0, 100) for _ in range(10)]
arr3 = [random.randint(0, 100) for _ in range(10)]

def how(x):
    num = int(len(str(x)))
    count = 0
    while x >=0:
        x = x - num
        count += 1
    print("Нужно действий, чтобы получить нуль: ", count)

def array(arr1, arr2, arr3):
    sum_arr1, sum_arr2, sum_arr3 = sum(arr1), sum(arr2), sum(arr3)
    
    print(f"Сумма 1: {sum_arr1}")
    print(f"Сумма 2: {sum_arr2}") 
    print(f"Сумма 3: {sum_arr3}")
    
    print(f"Среднее 1: {sum_arr1 / len(arr1)}")
    print(f"Среднее 2: {sum_arr2 / len(arr2)}")
    print(f"Среднее 3: {sum_arr3 / len(arr3)}")

array(arr1, arr2, arr3)
how(x)
