import numpy as np

a = np.array([1, 2, 3])
print(a.ndim, a.shape)
print(a)
print(a / 2) # все элементы массива делим на 2
a[0] = 234
print(a)
print()

b = np.array([[1, 2, 3], [5, 6, 7]])
print(b.ndim, b.shape)
print(b)
print(b * 2) # все элементы массива умножаем на 2
b[1, 2] = 0
print(b)
print()

c = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])
print(c.ndim, c.shape)
print(c)
print(c[1, 0]) # вторая строка, первый столбец
print(c[0, :]) # первая строка
print(c[:, 0]) # первый столбец
print()

e = np.random.randint(1, 100, (2, 7))
print(e)
print()

d = c + e # сложение массивов
print(d)

print(d.min(), d.max(), d.sum(), d.prod(), d.mean()) # минимум, максимум, сумма, произведение, среднее арифметическое
                                                     # массива (все элементы)
print(d.min(axis=0), d.max(axis=0), d.sum(axis=0), d.prod(axis=0), d.mean(axis=0)) # минимум, максимум, сумма,
                                                    # произведение, среднее арифметическое массива (по столбцам)
print(d.min(axis=1), d.max(axis=1), d.sum(axis=1), d.prod(axis=1), d.mean(axis=1)) # минимум, максимум, сумма,
                                                    # произведение, среднее арифметическое массива (по строкам)
print()

b = b.reshape((3, 2)) # изменение размера массива
print(b)

a = np.resize(a, (2, 4)) # изменение формы и размера массива
print(a)
print(a.transpose())