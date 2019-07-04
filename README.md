# projeto-ri
Lyrics and song genres dataset

"Spotify genre.py" can be run by itself and will produce 10 csv files in the same folder,  
containing 900 song names, artist name, genre in each  
  
  
"geniusLIB.py" needs to be run in the same folder as the csv files,  
it will use the rows of the database to search for the song lyrics in the genius api.  
Lyrics with no matching result will return "none" and be written for later processing in the csv
