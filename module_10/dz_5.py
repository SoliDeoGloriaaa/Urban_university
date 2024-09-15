import multiprocessing
import datetime


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        line = file.readline()
        while line:
            all_data.append(line)
            line = file.readline()


file_list = ['file_1.txt', 'file_2.txt', 'file_3.txt', 'file_4.txt']

now = datetime.datetime.now()
for file_name in file_list:
    read_info(file_name)
end = datetime.datetime.now()
print(f"Линейный подход занял {end - now} секунд")
# # Линейный подход занял 0:00:07.211002 секунд

if __name__ == '__main__':
    with multiprocessing.Pool(processes=4) as pool:
        now = datetime.datetime.now()
        results = pool.map(read_info, file_list)
    end = datetime.datetime.now()
    print(f"Многопроцессный подход занял {end - now} секунд")
# Многопроцессный подход занял 0:00:03.967868 секунд