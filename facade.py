class Lights:
    def dim(self): print("Lights dimmed")

class TV:
    def on(self): print("TV turned on")

class SoundSystem:
    def play(self): print("Playing sound")

class HomeTheaterFacade:
    def start_movie(self):
        Lights().dim()
        TV().on()
        SoundSystem().play()

# Usage
theater = HomeTheaterFacade()
theater.start_movie()