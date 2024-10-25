def make_album(artist, album, songs=None):
    music = {'artist': artist, 'album' : album}
    if songs:
        music['Songs'] = songs
    return music

album_artist = make_album('Rihanna','Anti')
print(album_artist)

album_artist = make_album("The Weeknd","Beauty Behind the Madness")
print(album_artist)

album_artist = make_album('Labrinth','Ends & Begins','10')
print(album_artist)
