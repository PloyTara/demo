class Audio:
    def PlaySong(self):
        print('Radio can play songs')

class Camera:
    def TakePhoto(self):
        print('Camera can take photo')

class Mobile(Audio, Camera):
    def PlayInternet(self):
        print('Mobile can play internet')

m = Mobile()
m.PlaySong()
m.TakePhoto()
m.PlayInternet()