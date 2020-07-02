#Setting alarm
import datetime
import os
import time
import vlc

class MusicPlayer():
    
    def __init__(self, filename):
        try:
            self.p = vlc.MediaPlayer(filename)
        except:
            print("error:initializing")

    def playMusic(self):
        try:
            print("MusicPlaying")
            self.p.play()
        except:
            print("playing error")

    def stopMusic(self):
        try:
            print("MusicStop")
            self.p.stop()
        except:
            print("Stopping error")
            
            
            
if __name__ == '__main__':
    mp = MusicPlayer("Wishful_Thinking.mp3")
    mp.stopMusic()