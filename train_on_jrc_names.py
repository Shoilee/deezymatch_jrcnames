import DeezyMatch
import sys

from DeezyMatch import train as dm_train
import os


if __name__ == '__main__':
    script_name, *args = sys.argv

    # args[0]:  hyper_parameter specification
    # args[1]: input data file for training
    # args[1]: name of the output folder

    # train a new model
    dm_train(input_file_path= str(args[0]), 
         dataset_path=str(args[1]), 
         model_name=str(args[2]))