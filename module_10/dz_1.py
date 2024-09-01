import time
from datetime import datetime
from threading import Thread

now = datetime.now()


def wite_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf8') as file:
        for i in range(word_count):
            file.write(f'Какое-то слово № {i} \n')
            time.sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


wite_words(10, 'exemple1.txt')
wite_words(30, 'exemple2.txt')
wite_words(200, 'exemple3.txt')
wite_words(100, 'exemple4.txt')

end = datetime.now()
result_1 = end - now
print(f'Время работы потоков: {result_1}')


mult_now = datetime.now()

the_first = Thread(target=wite_words, args=(10, 'exemple5.txt'))
the_second = Thread(target=wite_words, args=(30, 'exemple6.txt'))
the_thrid = Thread(target=wite_words, args=(200, 'exemple7.txt'))
the_fourth = Thread(target=wite_words, args=(100, 'exemple8.txt'))

the_first.start()
the_second.start()
the_thrid.start()
the_fourth.start()

the_first.join()
the_second.join()
the_thrid.join()
the_fourth.join()

mult_end = datetime.now()
result_2 = mult_end - mult_now
print(f'Время работы потоков: {result_2}')