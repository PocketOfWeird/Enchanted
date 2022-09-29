import subprocess

play_audio = lambda filename: subprocess.Popen(["mplayer", filename])