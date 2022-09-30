import subprocess
from pygame import mixer

def play_audio(filename): 
    sound = mixer.Sound(filename)
    sound.play()