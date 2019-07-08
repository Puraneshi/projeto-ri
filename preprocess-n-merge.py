import pandas as pd
import re
import langdetect

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
    lyrics = []
    for i in range(1, 10):
        with open("{}-lyrics{}.txt".format(key, i), "r", encoding="utf-8") as f:
            partial = f.read().split("LYRIC_SEPARATOR_SPLIT")[:-1]
            for song in partial:
                ly = re.sub(r'\[.*?\]', '', song).lower()
                ly = re.sub(r'^w+', '', ly)
                lyrics.append(ly)
    df = pd.read_csv("{}.csv".format(key))
    df["lyrics"] = lyrics

    print("before -> {}".format(df.shape))

    # COUNTING PART
    no_lyrics = []
    for index, row in enumerate(df.iterrows()):
        if row[1]["lyrics"]:
            try:
                languages = langdetect.detect_langs(row[1]["lyrics"])
                if "en" not in str(languages[0]):
                    no_lyrics.append(index)
            except:
                no_lyrics.append(index)
        else:
            no_lyrics.append(index)
    df = df.drop(no_lyrics)

    print("final {} -> {}".format(key, df.shape))
    df.to_csv("final{}-lyrics.csv".format(key), sep="|", index=False)
