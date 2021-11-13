import pandas as pd


# convert json file to xlsx 

def convert(lst):
    
    json_list = []
    converted_list = []
    S
    for i in lst:
        df_json = pd.read_json(i)
        converted_list = df_json.to_excel(i)
    return (converted_list)