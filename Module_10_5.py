import multiprocessing
from datetime import datetime

def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        while True:
            line = file.readline().strip()
            if not line:
                break
            all_data.append(line)

if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    start_time = datetime.now()
    for name in filenames:
        read_info(name)
    end_time_1 = datetime.now()
    res_time_1 = end_time_1 - start_time
    print('Время выполнения:', res_time_1, '(линейный вызов)')


    start_time = datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
         pool.map(read_info, filenames)
    end_time_2 = datetime.now()
    res_time_2 = end_time_2 - start_time
    print('Время выполнения:', res_time_2, '(многопроцессный)')