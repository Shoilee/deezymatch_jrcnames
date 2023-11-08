# [JRC-Names Overview](https://data.jrc.ec.europa.eu/dataset/jrc-emm-jrc-names#publications)
  - Available for download since September 2011, offering name variant lists and related software.
  - Developed by the European Commission's Joint Research Centre (JRC) as a multilingual resource for person and organization names; a by-product of the Europe Media Monitor (EMM)
  - Contains extensive lists of names and their numerous spelling variants, crossing various scripts (Latin, Greek, Arabic, Cyrillic, Japanese, Chinese, etc.).
  - The new linked data edition, accessible through the European Union's Open Data Portal, provides enhanced information compared to previous releases:
    - Includes historical titles and function names associated with person mentions.
    - Offers information on the period when name variants and their titles were discovered.
    - Provides various frequency counts for the names.
    - Establishes links to other linked datasets like DBPedia, expanding the depth and connections within the dataset.

```
|--- data
|   |---dataset_final_jrc_name: contains 5 column [name1, name2, match?(0/1), lang1, lang2]
|   |---entites: TODO: what does it contains?
|   |---jrcnames_uri.nt: n-triple of the dataset
|   |---nanes_pairs.txt: engineered dataset for deezymatch with construct_name_pairs.py
```
TODO: prepare data for deeezymatch (example: [prepare_data](../entity_linking/deezymatch/deezy_match_data_construction.py))

TODO: Explain the train, test and validation data

TODO: train deezymatch on JRCnames
