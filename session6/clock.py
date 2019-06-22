import datetime
import pyglet
from pyglet.media import Source, Player, load

alarm = int(input("alarm: "))
m = datetime.datetime.now().minute
while True:
    if m == alarm:
        mp3File = "crowd-cheering.mp3"

        player = Player()
        source = load(mp3File)
        player.queue(source)
        player.play()

        while True:
            interact = (input("play, pause or stop: "))
            if interact == "play":
                player.play()
            elif interact == "pause":
                player.pause()
            elif interact == "stop":
                player.pause()
                break
        break
    else:
        m = datetime.datetime.now().minute