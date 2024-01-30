import pandas
import rdflib
import time
from tqdm import tqdm


def read_file(file):
    df = pandas.read_csv(file, sep="\t")
    return df


# TODO add more languages; consider the language spoken by dutch colony or just specify I did it for two language
def retrieve_uri_from_label(label, df=pandas.read_pickle("../k_fold_validation/data/ground_truth.pkl")):
    wiki_uri_list = []

    for i, row in df.iterrows():
        if label in row['wiki_label']:
            wiki_uri_list.append(row['wiki_uri'])

    return list(set(wiki_uri_list))


def run(source_file, destination_file, directory='../k_fold_validation/data/'):
    df = pandas.read_pickle("../k_fold_validation/data/ground_truth.pkl")

    # DICTIONARY MAPS ID TO ALL DIFFERENT NAME VARIANTS
    id_to_names = dict()
    for i, row in df.iterrows():
        id = row['wiki_uri'].toPython()
        altnames = list(set([row['name_label']] + [label for label in row["wiki_label"]]))
        id_to_names[id] = altnames

    # DICTIONARY MAPS NAME VARIATION TO ITS ID
    name_to_id = dict()
    for id in id_to_names:
        for name in id_to_names[id]:
            if name in name_to_id:
                name_to_id[name].append(id)
            else:
                name_to_id[name] = [id]

    candidate_df = pandas.read_pickle(source_file, compression='infer')

    try:
        result_table = pandas.DataFrame(columns=['name_label', 'retrieved_uri'])
        truth_list = []
        for i, row in tqdm(candidate_df.iterrows()):
            retrieved_uri = []
            for candidate_label in row['cosine_dist'].keys():
                try:
                    retrieved_uri += retrieve_uri_from_label(str(candidate_label))
                except:
                    retrieved_uri += []
            retrieved_uri = list(set(retrieved_uri))

            try:
                truth_list.append(name_to_id[row['query']][0])
            except KeyError:
                truth_list.append('')
            # df2 = {'name': label, 'wiki_uri': run_query(str(label))}
            temp_df = pandas.DataFrame([[row['query'], retrieved_uri]], columns=['name_label', 'retrieved_uri'])
            result_table = pandas.concat([result_table, temp_df], ignore_index=True)
            time.sleep(.5)

    finally:
        # append truth_uri to the dataframe
        temp_series = pandas.Series(truth_list)
        result_table['wiki_uri'] = temp_series
        result_table.to_pickle(destination_file)
