class Track:

    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

    def show(self):
        print(f'{self.name}-{self.duration}')


class Album:

    def __init__(self, name, artist):
        self.name = name
        self.artist = artist
        self.tracks = []

    def get_tracks(self):
        for track in self.tracks:
            track.show()

    def add_track(self, track):
        self.tracks.append(track)

    def get_duration(self):
        full_duration = 0

        for track in self.tracks:
            full_duration += track.duration

        print(f'Full duration {self.name}: {full_duration}')


def place_tracks(album, tracks):
    for track in tracks:
        album.add_track(track)


def main():

    album_scratchpaper = Album('ScratchPaper', 'Fukkit')

    track_flashbang = Track('FlashBang', 2)
    track_woke = Track('Woke', 2)
    track_mincemeat = Track('Mincemeat', 1)

    scratchpaper_tracks = [track_flashbang, track_woke, track_mincemeat]

    album_snowball = Album('Snowball', 'Heartsnow')

    track_onetouch = Track('Одно касание', 2)
    track_darkcases = Track('Темные дела', 3)
    track_shift = Track('Shift', 1)

    snowball_tracks = [track_onetouch, track_darkcases, track_shift]

    place_tracks(album_scratchpaper, scratchpaper_tracks)
    place_tracks(album_snowball, snowball_tracks)

    album_scratchpaper.get_duration()
    album_snowball.get_duration()


if __name__ == '__main__':
    main()