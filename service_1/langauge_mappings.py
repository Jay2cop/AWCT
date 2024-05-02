import pandas as pd

def load_language_mappings():
    df = pd.read_csv("FLORES_200_LANG_MAPPING.csv", index_col=0, header=None, skipinitialspace=True)
    language_mappings = {key.strip(): value.strip() for key, value in df[1].to_dict().items()}
    #print(language_mappings)
    return language_mappings

mappings = load_language_mappings()