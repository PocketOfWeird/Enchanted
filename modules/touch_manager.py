from random import randrange
from .touch_map import touch_map
from .play_audio import play_audio

def touch_manager(input: int) -> str:

    files = touch_map(input)
    index = randrange(0,len(files))
    filename = files[index]
    player = play_audio(filename)
    #player.wait()

    return filename