import random

options = [None,'Rock', 'Scissor', 'Paper']
rock = '''
          _    ,-,    _
     ,--, /: :\\/': :`\\/: :
    |`;  ' `,'   `.;    `: |
    |    |     |  '  |     |.
    | :  |     | pb  |     ||
    | :. |  :  |  :  |  :  | 
     \\__/: :.. : :.. | :.. |  )
          `---',\\___/,\\___/ /'
               `==._ .. . /'
                    `-::-'
'''

paper = '''
         /"\\
     /"\\|\\./|/"\\
    |\\./|   |\\./|
    |   |   |   |
    |   |>~<|   |/"\\
    |>~<|   |>~<|\\./|
    |   |   |   |   |
/~T\\|   |   =[@]=   |
|_/ |   |   |   |   |
|   | ~   ~   ~ |   |
|~< |             ~ |
|   '               |
\\                   |
 \\                 /
  \\               /
   \\.            /
     |          |
     |          |
'''

scissor = '''
    .-.  _
    | | / )
    | |/ /
   _|__ /_
  / __)-' )
  \\  `(.-')
   > ._>-'
  / \\/

'''

hand_diagrams = []
print("\n\n\nWelcome to Rock , Paper, Scissor game !!!!")
print('''

Press
1 For Rock
2 For Scissor
3 For Paper
'''
)

hands = [None, rock, scissor, paper]
player_choice = input()

machine_choice = random.randint(1,3)

print(player_choice, machine_choice)
print("Your choice is - ", options[int(player_choice)])
print(hands[int(player_choice)])

print("Machine Choice - ", options[int(machine_choice)])
print(hands[int(machine_choice)])

if int(player_choice) == machine_choice:
    print("Ohhhh ---- It's a tie.")
elif int(player_choice) == 3 and machine_choice == 1:
    print("Hoyla ---- You are winner")
elif int(player_choice) == 1 and machine_choice == 3:
    print("Oopss ---- You Lost the Game")
elif int(player_choice) != 3 and int(player_choice) < machine_choice:
    print("Hoyla ---- You are winner")
elif machine_choice != 3 and machine_choice < int(player_choice):
    print("Oopss ---- You Lost the Game")

