class MusicPlayer:
    # __init__ is a special method that is called when an object is created 
    # __init__ is a constructor in OOP terms
    def __init__(self):
        self.name = "Music Player"
        self.type = "Volume"
        self.level = 20
        self.status = True
        self.songs = ['Knocking on Heaven\'s Door', 'Hotel California', 'Stairway to Heaven',
                        'Sweet Child O\' Mine', 'Bohemian Rhapsody', 'Smells Like Teen Spirit']
        self.current_song = 0
    # turn on the light
    def turn_on(self):
        self.status = True
        print("Music player is on")
    # turn off the light
    def turn_off(self):
        self.status = False
        print("Music player is off")
    # increase the brightness
    def increase(self):
        self.level += 1
        print(f"Volume is increased to {self.level}")
    # decrease the brightness
    def decrease(self):
        self.level -= 1
        print(f"Volume is decreased to {self.level}")
    
    def play(self):
        print(f"Music player is playing {self.songs[self.current_song]}")
    
    def pause(self):
        print(f"Music player is paused")
    
    def next(self):
        self.current_song = (self.current_song + 1) % len(self.songs)
        # if self.current_song == len(self.songs):
        #     self.current_song = 0
        print(f"Music player is playing {self.songs[self.current_song]}")
    
    def previous(self):
        self.current_song = (self.current_song - 1) % len(self.songs)
        print(f"Music player is playing {self.songs[self.current_song]}")