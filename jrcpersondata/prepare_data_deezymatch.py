from DeezyMatch import data_processing
import os, pickle
# in case ofilehandler doubt see: https://github.com/Living-with-machines/DeezyMatch/blob/master/DeezyMatch/data_processing.py


if __name__ == '__main__':
    file = "data/name_pairs.txt"
    mode = {
        "tokenize": ['char'],
        "min_gram": 1,
        "max_gram": 3,
        "token_sep": "default",
        "prefix_suffix":  ["|", "|"]

    }
    # by default split into train_prop=0.7, val_prop=0.15, test_prop=0.15, if parameter is not changed during call
    train_dc, valid_dc, test_dc, dataset_vocab = data_processing.csv_split_tokenize(dataset_path=file, csv_sep='\t', mode=mode)

    filehandler = open("data/dataset-string-matching_train.pkl", "wb")
    # pickle.dump(train_dc, filehandler)
    train_dc.df.iloc[:, 1:4].to_csv("data/dataset-string-matching_train.txt", sep='\t', index=False)

    filehandler = open("data/dataset-string-matching_test.pkl", "wb")
    # pickle.dump(test_dc, filehandler)
    test_dc.df.iloc[:, 1:4].to_csv("data/dataset-string-matching_test.txt", sep='\t', index=False)

    filehandler = open("data/dataset-string-matching_val.pkl", "wb")
    # pickle.dump(valid_dc, filehandler)
    valid_dc.df.iloc[:, 1:4].to_csv("data/dataset-string-matching_val.txt", sep='\t', index=False)

    filehandler = open("characters_v001.pkl", "wb")
    pickle.dump(dataset_vocab, filehandler)



