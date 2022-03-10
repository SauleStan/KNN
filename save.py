import pandas as pd

def save_to_file(data):
    df = pd.DataFrame(data)
    df.to_csv('wNewData.csv', header=None, index=None)

def add_new_data_to_dataframe(initial_data, new_data):
    updated_data = pd.DataFrame(initial_data)
    updated_data.loc[len(initial_data.index)] = new_data
    return updated_data