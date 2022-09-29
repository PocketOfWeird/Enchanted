import subprocess

play_audio = lambda filename: subprocess.Popen(["cvlc", filename])