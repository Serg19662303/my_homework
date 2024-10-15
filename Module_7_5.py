import os
import time

directory = os.getcwd()

for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(root, file)
        filetime = time.strftime("%d.%m.%Y %H:%M", time.localtime(os.path.getmtime(filepath)))
        # дзугой вариант
        # filetime = time.ctime(os.path.getmtime(file))
        size_file = os.path.getsize(filepath)
        dir_name = os.path.dirname(filepath)
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {size_file} байт, '
          f'Время изменения: {filetime}, Родительская директория: {dir_name}')