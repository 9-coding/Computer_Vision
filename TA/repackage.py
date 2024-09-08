import os
import glob
import shutil
import csv
import pandas as pd

data_path = '/Users/kdy1021/Desktop/2024-2/TA/stanford_cars_repackage/car_data/car_data'

def get_filelist(mode):
    list = []
    with open('remove_dirs.csv', newline='', encoding='utf-8-sig') as file:
        dirs = csv.reader(file)  # csv 파일 읽기
        data = os.path.join(data_path, mode)
        for dir_name in dirs:
            path = os.path.join(data, ''.join(dir_name))
            try:
                list = list + os.listdir(path)
            except Exception as e:
                print(e)

    return list

def annot_config(mode, list):
    if mode == 'train':
        annot = 'anno_train.csv'
        file_name = 'annoted_train.csv'
    elif mode == 'test':
        annot = 'anno_test.csv'
        file_name = 'annoted_test.csv'
    else:
        annot = ''
        file_name = ''

    df = pd.read_csv(os.path.join(os.path.dirname(os.path.dirname(data_path)), annot))
    df_filtered = df[~df.iloc[:, 0].isin(list)]
    df_filtered.to_csv(file_name, index=False)

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

for mode in ['train', 'test']:
    list = get_filelist(mode)
    annot_config(mode, list)
    remove_dirs(mode)