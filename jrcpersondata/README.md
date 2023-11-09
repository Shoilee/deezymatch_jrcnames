This script explains how JRC-Names data has been adoped for DeezyMatch tool, in order to train it for differrent spelling and language variation for the same read world person.

# How the data is prepapred?

[dataset_final_jrc_person.csv](data/dataset_final_jrc_person.csv) from JRC-Names dataset has been cleaned with the following code which mainly seperates the columns with '\t' and insert space in between two words of a name. It also replaces 1 or 0 for all 'TRUE' and 'FALSE' respectively. 

```
def clean_text(text):
    text = text.replace('|', '\t')
    text = text.replace('+', ' ')
    text = text.replace('1', 'TRUE')
    text = text.replace('0', 'FALSE')
    with open('data/name_pairs.txt', 'a+') as f:
        f.writelines(text+"\n")
    return 
```    

The output of this script is [name_pairs.txt](data/name_pairs.txt) which has 5,000,000 data points.

## Split Train, Validation and Test Set: 

DeezyMatch library provides script for [data_processing](https://github.com/Living-with-machines/DeezyMatch/blob/master/DeezyMatch/data_processing.py). The function csv_split_tokenize splits data into train, validation and test set of proportion 70%, 15% and 15% respetively if updated parameter is not provided. Using this function, we split [name_pairs.txt](data/name_pairs.txt) into train, validation and test examples, that ultimately results into the followinf stattistics: 

<ul>
<li> Size of Training examples: 3,500,000</li>
<li> Size of Validation examples: 750,000</li>
<li> Size of Test examples: 750,000</li>
</ul>

This data preparation is done using the local script [prepare_data_deezymatch.py](prepare_data_deezymatch.py).


## Train deezymatch on JRCnames

Training is done using the [job script](../cluster.job) on snellius cluster.


## [What is JRC-Names?](https://data.jrc.ec.europa.eu/dataset/jrc-emm-jrc-names#publications)
  - Available for download since September 2011, offering name variant lists and related software.
  - Developed by the European Commission's Joint Research Centre (JRC) as a multilingual resource for person and organization names; a by-product of the Europe Media Monitor (EMM)
  - Contains extensive lists of names and their numerous spelling variants, crossing various scripts (Latin, Greek, Arabic, Cyrillic, Japanese, Chinese, etc.).
  - The new linked data edition, accessible through the European Union's Open Data Portal, provides enhanced information compared to previous releases:
    - Includes historical titles and function names associated with person mentions.
    - Offers information on the period when name variants and their titles were discovered.
    - Provides various frequency counts for the names.
    - Establishes links to other linked datasets like DBPedia, expanding the depth and connections within the dataset.

### Stat

### Resources

### Cite As

```
|--- data
|   |---dataset_final_jrc_name: contains 5 column [name1, name2, match?(0/1), lang1, lang2]
|   |---entites: TODO: what does it contains?
|   |---jrcnames_uri.nt: n-triple of the dataset
|   |---nanes_pairs.txt: engineered dataset for deezymatch with construct_name_pairs.py
```


