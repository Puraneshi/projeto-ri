import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
from nltk.corpus import wordnet

# Client ID contido no dashboard
cid = "fd2ea91cf94f49848dfdc035f84d2b70"
# Client Secret contido no dashboard
secret = "d7ddb37948e84510a9bcb8cab92451b3"

client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# top 10 genres from https://ifpi.org/downloads/Music-Consumer-Insight-Report-2018.pdf
# with same genre names from spotify's tags
collapsed_genres = {"pop": ["pop"],
                    "rock": ["rock"],
                    "dance-electronic-house": ["dance", "electronic", "house"],
                    "soundtracks": ["soundtracks"],
                    "hip-hop-rap-trap": ["hip-hop"],
                    "singer-songwriter": ["singer-songwriter", "songwriter"],
                    "classical-opera": ["classical", "opera"],
                    "r&b": ["r-n-b"],
                    "soul-blues": ["soul", "blues"],
                    "metal": ["metal", "black-metal", "death-metal", "heavy-metal", "metalcore"]}

for key in collapsed_genres:
    genre = key
    genres = collapsed_genres[key]

    # pandas table
    df = pd.DataFrame(columns=["name", "artist", "genre"])

    index = 0
    repetitions = 0
    while len(df) < 900:
        # gets recommendations by genre
        results = sp.recommendations(seed_genres=genres, limit=100)
        for field in results["tracks"]:
            # if the song is not in the table, insert it
            if not df["name"].isin([field["name"].split(' -')[0]]).any():
                df.loc[index] = [field["name"].split(' -')[0], field["artists"][0]["name"], genre]
                index += 1
            else:
                print(len(df), genre)
    # exports genre table to csv
    df.to_csv("{}.csv".format(genre), index=False)
    print("Done {}".format(genre), len(df))

print("ALL DONE")
