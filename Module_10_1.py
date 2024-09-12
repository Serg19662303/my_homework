import time
from datetime import datetime
from threading import Thread

def write_words(word_count, file_name):
    file = open(file_name, 'w', encoding='utf-8')
    for i in range(word_count):
        file.write(f'ЭТО слово № {i+1} \n')
    time.sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')
    file.close()


start_t = datetime.now()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

end_t = datetime.now()
print(end_t - start_t)

data_list1 = [10, 30, 200, 100]
data_list2 = ['example5.txt', 'example6.txt', 'example7.txt', 'example8.txt']

start_t = datetime.now()

w = [Thread(target=write_words, args=(data_list1[i], data_list2[i])) for i in range(len(data_list1))]
for i in range(len(data_list1)):
    w[i].start()
for i in range(len(data_list1)):
    w[i].join()

end_t = datetime.now()
print(end_t - start_t)