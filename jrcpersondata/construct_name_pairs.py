# This is a sample Python script.
from rdflib.graph import Graph
import pandas
import os
from tqdm import tqdm
import sys
import multiprocessing as mp

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    filename = 'data/dataset_final_jrc_person.csv'
    for chunk in tqdm(pandas.read_csv(filename, sep='\s+',chunksize=1)):
        with open('data/name_pairs.txt', 'a+') as f:
            for row in chunk.iloc[:, 0]:
                row = row.replace('|', '\t')
                row = row.replace('+', ' ')
                row = row.replace('1', 'TRUE')
                row = row.replace('0', 'FALSE')
                # print(row)
                # f.write(row+"\n")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
