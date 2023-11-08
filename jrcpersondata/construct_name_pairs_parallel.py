# This is a sample Python script.
from rdflib.graph import Graph
import pandas
import os
from tqdm import tqdm
import sys
import multiprocessing as mp


def clean_text(text):
    text = text.replace('|', '\t')
    text = text.replace('+', ' ')
    text = text.replace('1', 'TRUE')
    text = text.replace('0', 'FALSE')
    with open('data/name_pairs.txt', 'a+') as f:
        f.writelines(text+"\n")

    #print(text)
    return 0


if __name__ == '__main__':
    n_workers = int(mp.cpu_count()/2)

    filename = 'data/dataset_final_jrc_person.csv'
    df = pandas.read_csv(filename, sep='\s+', names=['data'], header=None)
    print(f"Shape:{df.shape}\n\nColumn Names:\n{df.columns}\n")

    # tqdm.pandas()
    # df['data'].progress_apply(clean_text)

    p = mp.Pool(n_workers)
    #with open('data/new_name_pairs.txt', 'a+') as f:
    p.map(clean_text, tqdm(df['data']))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
