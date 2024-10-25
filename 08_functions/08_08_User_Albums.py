active = True
def make_album(artist, album, songs):
    music = {'artist': artist, 'album' : album, 'songs': songs}
   
    return music

print("\nPlease enter information about an album:")
print("Press 'q' at any time to stop.")

while True:
    
    artist = input("Artist Name:")
    if artist == 'q':
        break
    album_name = input("Album Name:")
    if album_name == 'q':
        break
    songs = input("How many songs are on it:")
    if songs == 'q':
        break

    format = make_album(artist, album_name, songs)
    print(format)   

print("\nThanks for responding.")