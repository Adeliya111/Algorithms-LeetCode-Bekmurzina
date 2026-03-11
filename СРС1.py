import random  # для генерации случайных чисел
import time    # для измерения времени выполнения
import matplotlib.pyplot as plt  # для построения графиков

#алгоритмы сортировки (до 36 строки)
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i] #текущий элемент для вставки
        j = i - 1 #индекс последнего отсортированного элемента
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge_sort(arr):
    if len(arr) <= 1: #если массив из одного или нуля элементов уже отсортирован
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

#генераторы данных (до 53 строки)
def random_array(n): #Генерирует массив случайных чисел
    return [random.randint(0, n) for _ in range(n)]

def sorted_array(n): #Генерирует отсортированный массив
    return list(range(n))

def reversed_array(n): #Генерирует обратный массив
    return list(range(n - 1, -1, -1))

def almost_sorted_array(n, swap_fraction=0.01): #Генерирует почти отсортированный массив
    arr = list(range(n))
    swaps = int(n * swap_fraction)
    for _ in range(swaps):
        i, j = random.sample(range(n), 2)
        arr[i], arr[j] = arr[j], arr[i]
    return arr

#замер времени (до 64 строки)
def measure_time(sort_func, arr, repeats=5):
    total = 0
    for _ in range(repeats):
        test_arr = arr.copy()
        start = time.time()
        sort_func(test_arr)
        end = time.time()
        total += (end - start)
    return total / repeats

#параметры тестирования  (до 73 строки)
sizes = [1000, 5000, 10000, 50000]
data_types = {
    'random': random_array,
    'sorted': sorted_array,
    'reversed': reversed_array,
    'almost_sorted': almost_sorted_array
}

results = {
    'insertion': {dtype: [] for dtype in data_types},
    'merge': {dtype: [] for dtype in data_types}
}

#запуск тестов (до 89 строки)
for dtype, generator in data_types.items():
    print(f"\nТестирование: {dtype}")
    for n in sizes:
        arr = generator(n)
        t_ins = measure_time(insertion_sort, arr)
        t_mer = measure_time(merge_sort, arr)
        results['insertion'][dtype].append(t_ins)
        results['merge'][dtype].append(t_mer)
        print(f"  n={n}: insertion = {t_ins:.6f} сек, merge = {t_mer:.6f} сек")

#построение графиков (до 101 строки)
for dtype in data_types:
    plt.figure(figsize=(8, 5))
    plt.plot(sizes, results['insertion'][dtype], marker='o', label='Insertion Sort')
    plt.plot(sizes, results['merge'][dtype], marker='s', label='Merge Sort')
    plt.xlabel('Размер массива (n)')
    plt.ylabel('Среднее время выполнения (сек)')
    plt.title(f'Сравнение на {dtype} данных')
    plt.legend()
    plt.grid(True)
    plt.show()

#для случайных данных (до 112 строки)
plt.figure(figsize=(8, 5))
plt.plot(sizes, results['insertion']['random'], marker='o', label='Insertion Sort')
plt.plot(sizes, results['merge']['random'], marker='s', label='Merge Sort')
plt.xlabel('Размер массива (n)')
plt.ylabel('Среднее время выполнения (сек)')
plt.title('Сравнение на случайных данных')
plt.legend()
plt.grid(True)
plt.show()

#вывод таблиц
import pandas as pd
for dtype in data_types:
    df = pd.DataFrame({
        'Размер': sizes,
        'Insertion Sort': results['insertion'][dtype],
        'Merge Sort': results['merge'][dtype]
    })
    print(f"\n{dtype.upper()} данные:")
    print(df.to_string(index=False))
