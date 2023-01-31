import pandas as pd

def read_file():
    df = pd.read_csv(r'C:\Users\elena.zampieri\Desktop\Study\ed_sheeran_spotify.csv',index_col=0)
    return df

def show_head(df):
    return df.head(10)

df = read_file()
print(show_head(df))

def unique_songs(df):
    total_songs = str(df.name.nunique());
    return total_songs
print(unique_songs(df))

def oldest_song(df):
    oldest_song = str(df.release_date.min());
    return oldest_song
print(oldest_song(df))

def newest_song(df):
    newest_song = str(df.release_date.max());
    return newest_song
print(newest_song(df))

def lowest_danceability(df):
    df_lowest_danceability = df[df['danceability']==df.danceability.min()]
    song_lowest_danceability = str(df_lowest_danceability["name"].values[1])
    return song_lowest_danceability
print(lowest_danceability(df))

def highest_danceability(df):
    df_highest_danceability = df[df['danceability']==df.danceability.max()]
    song_highest_danceability = str(df_highest_danceability["name"].values[1])
    return song_highest_danceability
print(highest_danceability(df))

def unique_albumns(df):
    albumns = (df['album'].unique())
    return albumns
print(unique_albumns(df))

def avg_songs_per_albumn(df):
    avg_songs=str(df.groupby('album').name.nunique().mean())
    return avg_songs
print(avg_songs_per_albumn(df))

def most_popular_songs(df):
    popular_songs = df[["name","popularity"]].sort_values(['popularity'], ascending=[False])
    top_10_songs = popular_songs[:10]
    return top_10_songs
print(most_popular_songs(df))

def least_popular_songs(df):
    least_popular_songs = df[["name","popularity"]].sort_values(['popularity'])
    last_10_songs = least_popular_songs[:10]
    return last_10_songs
print(least_popular_songs(df))

def longest_song(df):
    longest_song_duration_ms = df[df['duration_ms']==df.duration_ms.max()]
    longest_song = str(longest_song_duration_ms["name"].values[0])+ '  ' +str(longest_song_duration_ms["duration_ms"].values[0]/60000)
    return longest_song
print(longest_song(df))

def check_nulls(df):
    nulls = df.isnull().values.any()
    return nulls
print(check_nulls(df))




