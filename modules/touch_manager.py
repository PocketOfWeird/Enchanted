from random import randrange
from pygame import mixer
from .touch_map import touch_map
from .play_audio import play_audio

def touch_manager(input: int) -> str:
    print('Touched {}'.format(input))
    

    files = touch_map(input)
    index = randrange(0,len(files))
    filename = files[index]
    print('Playing Audio: {}'.format(filename))
    play_audio(filename)
    while mixer.get_busy():
        pass
    
    print('Stopping Audio: {}'.format(filename))

    return filename