"""from playsound import playsound
playsound("C:/Users/Abner/Music/cool for the summer- demi lovato (sped up) tik tok.mp3")"""

from pygame import mixer

mixer.init()
mixer.music.load(
    "C:/Users/Abner/Music/cool for the summer- demi lovato (sped up) tik tok.mp3")
mixer.music.play()

color_red = '\033[31m'
reset_color = '\033[m'

read_key = input("Enter anything to stop...")
print(color_red + 'Finished' + reset_color)
