# Линейный вызов

from datetime import datetime
import multiprocessing

def read_info(name):
    print(name)
    all_data = []
    with open(name, 'r') as f:
        for line in f:
            l = line.replace('\n', '')
            all_data.append(l)
        f.close()

# filenames = [f'./file {number}.txt' for number in range(1, 5)]
# start = datetime.now()
#
# for file in filenames:
#     read_info(file)
#
# end = datetime.now()
# print(end - start)

# 0:00:29.347758
# 0:00:43.405526
# 0:00:42.201592
# 0:00:24.717803
# 0:00:19.715614

# Многопроцессорный

if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    with multiprocessing.Pool(processes=4) as pool:
        start = datetime.now()
        pool.map(read_info, filenames)

    end = datetime.now()
    print(end - start)

# 0:00:58.660670
# 0:01:19.219595
# 0:01:07.785394
# 0:00:25.166222