def add_songs(*songs):
    final_songs = dict()
    for curr_song in songs:
        song_name = curr_song[0]
        lyrics = curr_song[1]
        if song_name not in final_songs:
            final_songs[song_name] = []
        final_songs[song_name].extend(lyrics)
    result = []
    for name, lyr in final_songs.items():
        if len(lyr) == 0:
            result.append(f"- {name}")
        else:
            n = "\n"
            result.append(f"- {name}\n{n.join(lyr)}")
    return "\n".join(result)


print(add_songs(
    ("Love of my life",
     ["Love of my life, you've hurt me",
      "You've broken my heart, and now you leave me",
      "Love of my life, can't you see?",
      "Bring it back, bring it back"]),
    ("Beat It", []),
    ("Love of my life",
     ["Don't take it away from me",
      "Because you don't know",
      "What it means to me"]),
    ("Dream On",
     ["Every time that I look in the mirror"]),
))


