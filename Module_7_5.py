import os
import time

directory = os.getcwd()

for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(root, file)
        #filetime = os.path.getmtime(file)
        filetime = time.ctime(os.path.getmtime(file))
        # formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        size_file = os.path.getsize(file)
        dir_name = os.path.dirname(root)
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {size_file} байт, '
          f'Время изменения: {filetime}, Родительская директория: {dir_name}')