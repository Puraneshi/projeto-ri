import lyricsgenius as genius
import pandas as pd

api = genius.Genius('QIQi7D4STCYtQIbXA6rX9VeUI6CLo75XZ6Vu_7PqMOSNPDx695d4FVn6sUHKY0za')
genres = {"pop": ["pop"],
          "rock": ["rock"],
          "dance-electronic-house": ["dance", "electronic", "house"],
          "soundtracks": ["soundtracks"],
          "hip-hop-rap-trap": ["hip-hop"],
          "singer-songwriter": ["singer-songwriter", "songwriter"],
          "classical-opera": ["classical", "opera"],
          "r&b": ["r-n-b"],
          "soul-blues": ["soul", "blues"],
          "metal": ["metal", "black-metal", "death-metal", "heavy-metal", "metalcore"]}

for key in genres:
    lyrics_series = []
    # read the genre csv
    df = pd.read_csv("{}.csv".format(key))
    # 'index' used to enumerate the redundancy files
    # IF PROGRAM STOPS, USE INDEX TO RESTART FROM THE LAST HUNDRED
    # ALTER 'index' TO THE NUMBER ON LAST FILE GENERATED
    index = 0
    for row in list(df.iterrows())[(index*100)::]:
        try:
            # use gathered songnames and artists to search on the api
            lyrics = api.search_song(row[1]["name"], row[1]["artist"]).lyrics
        except:
            # if api doesn't find, it catches the error and writes "none" as lyrics
            lyrics = "none"
        lyrics_series.append(lyrics)
        # redundancy for every 100 lyrics
        if len(lyrics_series) >= 100:
            index += 1
            with open("{}-lyrics{}.txt".format(key, index), "a", encoding="utf-8") as f:
                for item in lyrics_series:
                    f.write(item)
                    # used to create a split key for future use
                    f.write("LYRIC_SEPARATOR_SPLIT")
                lyrics_series = []
    index = 0
