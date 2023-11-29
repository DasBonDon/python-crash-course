# 8-8 User Albums
def make_album(artist, title, songs=None):
    album = {'artist': artist, 'album': title}
    if songs:
        album['songs'] = int(songs)
    return album

while True:
    print("\nPlease tell me your favorite album:")
    print("(enter 'q' at any time to quit)")

    artist = input("Artist: ")
    if artist == 'q':
        break

    album = input('Album: ')
    if album == 'q':
        break

    album = make_album(artist, album)
    print(album)