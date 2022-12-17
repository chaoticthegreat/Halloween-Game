from assets import *
from music import *
import random,time
source = play_music() 
while True:
  story = []
  starters = ['It was a dark and spooky night','Lightning flashed and thunder boomed', 'The giant spider', 'A big shadow loomed', "The witch cackled", "A werewolf howled under the bright moon",'The statue twitched', "The door creaked open",'In the middle of nowhere','In a abandonned factory','In a creppy old mansion','Spiders crawled all around the room']
  it = random.choice(starters)
  story.append(it)
  players = []
  color_of_player = {}
  while True:
    try:
      number_player = int(input(f"{bright_magenta}How many players\n{bright_yellow}=>{bright_magenta} "))
    except:
      print("Only numbers")
      continue
    break
  for i in range(1,number_player+1):
    name = input(f"{bright_magenta}Pick a name for Player {bright_yellow}{i}\n=>{bright_magenta} ")
    if input(bright_magenta+"Press "+bright_yellow+"[s] "+bright_magenta+"to show colors you can use for coloring the name. "+bright_yellow+"[enter]"+bright_magenta+" to continue\n=> "+bright_yellow) != '':
      

      print(f"{bright_magenta}We have these {bright_yellow}colors:\n{black}black,\n{red}red,\n{green}green,\n{yellow}orange,\n{blue}blue,\n{magenta}magenta,\n{cyan}cyan,\n{white}white,\n{bright_black}bright black,\n{bright_red}bright red,\n{bright_green}bright green,\n{bright_yellow}yellow,\n{bright_blue}bright blue,\n{bright_magenta}bright magenta,\n{bright_cyan}bright cyan,\n{white}and {bright_white}bright white")
    while True:
      color = input(f"{bright_magenta}Pick a color for {bright_yellow}{name}\n=> {bright_magenta}").lower()
      if color == 'red': 
        color = red
        break
      elif color == 'black':
        color = black
        break
      elif color == 'green':
        color = green
        break
      elif color == 'orange': 
        color = yellow
        break
      elif color == 'blue': 
        color = blue
        break
      elif color == 'magenta': 
        color = magenta
        break
      elif color == 'cyan': 
        color = cyan
        break
      elif color == "white": 
        color = white
        break
      elif color == "bright black": 
        color = bright_black
        break
      elif color == "bright red": 
        color = bright_red
        break
      elif color == "bright green": 
        color = bright_green
        break
      elif color == "yellow": 
        color = bright_yellow
        break
      elif color == "bright blue": 
        color = bright_blue
        break
      elif color == "bright magenta": 
        color = bright_magenta
        break
      elif color == "bright cyan": 
        color = bright_cyan
        break
      elif color == "bright white": 
        color = bright_white
        break
      else: 
        print("We don't have that color!")
        print(f"{bright_magenta}We have these {bright_yellow}colors:\n{black}black,\n{red}red,\n{green}green,\n{yellow}orange,\n{blue}blue,\n{magenta}magenta,\n{cyan}cyan,\n{white}white,\n{bright_black}bright black,\n{bright_red}bright red,\n{bright_green}bright green,\n{bright_yellow}yellow,\n{bright_blue}bright blue,\n{bright_magenta}bright magenta,\n{bright_cyan}bright cyan,\n{white}and {bright_white}bright white")
        continue
    print(f'{bright_magenta}Gotcha, {color}{name}')
    players.append(name)
    color_of_player[name] = color
    time.sleep(2)
    clear()
  while True:
    try:
      words = int(input(f"{bright_magenta}How many words {yellow}(Suggested: 30 - 50)\n{bright_yellow}=>{bright_magenta}  "))
    except:
      print(f"{yellow}Only number please!")
      continue
    break
  player = 0
  max_player = len(players)
  for i in range(words):
    while True:
      if player == max_player-1:
        player = 0
      else:
        player+=1
      print(bright_magenta+"")
      print(*story, sep = ' ')
      current_player = players[player]
      current_color = color_of_player[current_player]
      
      print(bright_magenta+"Player "+current_color+current_player+bright_yellow+" answer "+bright_magenta+"with"+bright_yellow+" one"+bright_magenta+" word")
      word = input(f"{bright_yellow}=>{current_color} ")
      clear()
      if " " in word:
        print(f'{bright_magenta} Only {bright_yellow}one {bright_magenta}word!')
        continue
      else:
        break
    word = current_color + word
    story.append(word)
  print(f"{bright_magenta}The {bright_yellow}story{bright_magenta} is{bright_yellow} finished!{bright_magenta}")
  print(*story,sep=' ')
  print(f"Do you wanna play again {bright_yellow}Yes{bright_magenta}/{bright_yellow}No")
  while True:
    choice = input(f"{yellow}={bright_yellow}>{bright_magenta} ").lower()
    if choice == 'yes':
      break
    elif choice == 'no':
      print(f'{yellow}H{bright_magenta}a{yellow}p{bright_magenta}p{yellow}y{bright_magenta} H{yellow}a{bright_magenta}l{yellow}l{bright_magenta}o{yellow}w{bright_magenta}e{yellow}e{bright_magenta}n')
      print(f"{bright_yellow}Enjoy{bright_magenta}the rest of the {bright_yellow}music!")
      print('Type "quit" to end the music at any time')
      while True:
        if input().lower() == "quit":
          pause(source)
          print("Bye!")
          quit()
    else:
      continue
  clear()
  pause(source)
  source = play_music()
  continue