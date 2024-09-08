import os
import glob
import shutil
import csv

data_path = '/Users/kdy1021/Desktop/2024-2/TA/stanford_cars_repackage/car_data/car_data'
#file = open(data_path, 'r')

def remove_dirs(mode):
    with open('remove_dirs.csv', newline='', encoding='utf-8-sig') as file:
        dirs = csv.reader(file)  # csv 파일 읽기
        data = os.path.join(data_path, mode)
        for dir_name in dirs:
            path = os.path.join(data, ''.join(dir_name))
            print("Removed:", path)
            try:
                shutil.rmtree(path)
            except Exception as e:
                print(e)

remove_dirs('train')
remove_dirs('test')