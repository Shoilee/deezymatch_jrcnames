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


## Train DeezyMatch on JRC-Names

Training is done using the [job script](../cluster.job) on snellius cluster.


## [What is JRC-Names?](https://data.jrc.ec.europa.eu/dataset/jrc-emm-jrc-names#publications)
  - Developed by the European Commission's Joint Research Centre (JRC) as a multilingual resource for person and organization names; a by-product of the Europe Media Monitor (EMM)
  - Contains extensive lists of names and their numerous spelling variants, crossing various scripts (Latin, Greek, Arabic, Cyrillic, Japanese, Chinese, etc.).
  - The new linked data edition, accessible through the European Union's Open Data Portal, provides enhanced information compared to previous releases:
    - Includes historical titles and function names associated with person mentions.
    - Offers information on the period when name variants and their titles were discovered.
    - Provides various frequency counts for the names.
    - Establishes links to other linked datasets like DBPedia, expanding the depth and connections within the dataset.

### Stat

- 307,000 distinct entities with 333,000 variants.
-  the database included names spelt in 27 different scripts. The most frequently used scripts are:
   -   Latin (including English and most other European languages), 
   -   Cyrillic (e.g. Russian and Bulgarian), 
   -   Arabic (including Farsi), 
   -   Japanese (Han, Hiragana and Katakana) and 
   -   Chinese Han (simplified variant)
- 64% of the names in JRC-Names do not have additional spelling variants. 
- For 28% of the names, JRC-Names knows two or three spellings. 
- There are 3760 entities with ten spellings or more, and 
- 37 entities with over 100 spelling variants.  


### Resources
#### Publication
- Steinberger Ralf, Bruno Pouliquen, Mijail Kabadjov, Jenya Belyaeva & Erik van der Goot (2011). JRC-Names: A freely available, highly multilingual named entity resource. Proceedings of the 8th International Conference Recent Advances in Natural Language Processing (RANLP). Hissar, Bulgaria, 12-14 September 2011.
- Ehrmann Maud, Guillaume Jacquet & Ralf Steinberger (2016). 
JRC-Names: Multilingual Entity Name Variants and Titles as Linked Data. Semantic Web Journal (March 2016).
#### Dataset
- https://data.jrc.ec.europa.eu/dataset/jrc-emm-jrc-names#publications
### Cite As

```
Jacquet, Guillaume; Verile, Marco (2015): JRC-Names RDF: Person and organisation spelling variants as found in multilingual news articles. European Commission, Joint Research Centre (JRC) [Dataset] PID: http://data.europa.eu/89h/jrc-emm-jrc-names
```

OR, BibTeX

```
@techreport{JRC-Names2016 ,
author = {Guillaume Jacquet and Marco Verile},
year = 2015 ,
title = {JRC-Names RDF: Person and organisation spelling variants as found in multilingual news articles},
institution = {European Commission, Joint Research Centre (JRC)},
type = {Dataset},
note = {\url{http://data.europa.eu/89h/jrc-emm-jrc-names}}
}

```

### Data Description
```
|--- data
|   |---dataset_final_jrc_name: contains 5 column [name1, name2, match?(0/1), lang1, lang2]
|   |---entites: TODO: what does it contains?
|   |---jrcnames_uri.nt: n-triple of the dataset
|   |---nanes_pairs.txt: engineered dataset for deezymatch with construct_name_pairs.py
```


