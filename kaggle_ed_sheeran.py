import pandas as pd

def read_file():
    df = pd.read_csv(r'C:\Users\elena.zampieri\Desktop\Study\ed_sheeran_spotify.csv',index_col=0)
    return df

def show_head(df):
    return df.head(10)

df = read_file()
print(show_head(df))
