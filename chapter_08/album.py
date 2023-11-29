# 8-7 Album
def make_album(artist, title, songs=None):
    album = {'artist': artist, 'album': title}
    if songs:
        album['songs'] = int(songs)
    return album

album = make_album('led zeppelin', 'physical graffiti')
print(album)
album = make_album('steely dan', 'aja')
print(album)
album = make_album('herbie hancock', 'head hunters')
print(album)
album = make_album('mac demarco', 'salad days', '11')
print(album)