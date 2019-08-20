from sclib import SoundcloudAPI, Track, Playlist

api = SoundcloudAPI()
playlist = api.resolve('https://soundcloud.com/playlist/sets/started-on-soundcloud')

assert type(playlist) is Playlist

for track in playlist.tracks:
    filename = f'./RoomifySongs/{track.artist} - {track.title}.mp3'
    with open(filename, 'wb+') as fp:
        track.write_mp3_to(fp)