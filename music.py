
from assets import *
from replit import audio


def play_music():

		while True:
				which_music = input(bright_magenta +"What music?\n"+bright_yellow+"[a]"+bright_magenta+" Spooky Scary Skeletons Remix\n"+bright_yellow+"[b]"+bright_magenta+" Danse Macabre\n"+bright_yellow+"[c]"+bright_magenta+" No Music\n=> "+bright_yellow)
				
				clear()

				if which_music == "b":
					
						source = audio.play_file('audio (2).mp3')
						break
						clear()

				elif which_music == "a":
					
						source = audio.play_file('audioNEW.mp3');source.set_loop(99999999)
						break
						clear()

				elif which_music == "c":
						
						source = audio.play_file('audio (2).mp3')
						source.paused = True
						break 
						clear()

				else:
					print(bright_magenta+"Sorry, we don't have that.")
    

		return source
def pause(source):
		
		source.paused = True