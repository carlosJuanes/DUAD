
class Telephone:
    def __init__(self, number):
        self.number=number

    def call(self):
        print(f"Calling the number {self.number}")

    def turn_on(self):
        print("Hello moto!!!")


class MusicPlayer:
    def __init__(self, current_song):
        self.current_song=current_song

    def turn_on(self):
        print("welcome...")

    def play(self):
        print(f"playing the song {self.current_song}")


class Smartphone(Telephone, MusicPlayer):
    def __init__(self, number, current_song):
        Telephone.__init__(self, number)
        MusicPlayer.__init__(self,current_song)

    def stop(self):
        print(f"stopping music {self.current_song} and the call {self.number}")

Motorola=Smartphone("301-756-6573", "bohemian rhapsody")
Motorola.turn_on()
Motorola.stop()