import os
import time

directory = 'D:\\DEV\\Urban_university'
for dirpath, dirnames, filenames in os.walk(directory):
    for file in filenames:
        full_file_path = os.path.join(dirpath, file)
        file_time = os.path.getmtime(full_file_path)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(file_time))
        size = os.path.getsize(full_file_path)
        parent_dir = os.path.dirname(full_file_path)
        print(
            f'Обнаружен файл: {file}\n Путь: {full_file_path}\n Размер: {size} байт\n Время изменения: {formatted_time}\n Родительская директория: {parent_dir}'
        )
        