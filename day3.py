print("Welcome to Escape Room.")
print("Your mission is to escape before they get you! ")
print('''
   _________________________________________________________
 /|                                                         |\
/ |                                                         | \
  |                                                         |
  |                                                         |
  |      .-'````````'.         (         .-'```````'-.      |
  |    .` |           `.       )       .` |           `.    |
  |   /   |             \      U      /   |             \   |
  |  |    |              | o   T   o |    |              |  |
  |  |    |              |  .  |  .  |    |              |  |
  |  |    |              |   . | .   |    |              |  |
  |  |    |              |    .|.    |    |              |  |
  |  |    |______________|     |     |    |______________|  |
  |  |   /               |     !     |   /               |  |
  |  |  /                |           |  /                |  |
  |  | /                 |           | /                 |  |
  |__|/__________________|___________|/__________________|__|
 /                                                           \
/                                                             \
''')
direction1 = input("Only two paths, left or right? ")
if direction1.lower()[0] == 'r':
    print("Wrong way, you walked into them :( Game over")
    quit()
elif direction1.lower()[0] == 'l':
    print("Nice, theres no one around")
    print('''
                    -_
        Cnn-.__   A_._
      ,' / `.$$&7.\\  `.
      :  0--:(o) : `0  :
       `._.'      `._.'
   ''')
    direction2 = input("There is a motorcycle. Do you want to take it? ")
    if direction2.lower()[0] == 'y':
        print("It's too loud, they heard you :(")
    elif direction2.lower()[0] == 'n':
        print("Good choice, let's keep walking")
        print('''
            __________
           |  __  __  |
           | |  ||  | |
           | |  ||  | |
           | |__||__| |
           |  __  __()|
           | |  ||  | |
           | |  ||  | |
           | |  ||  | |
           | |  ||  | |
           | |__||__| |
           |__________|
        ''')
        door = input("Last door and we are out, choose wisely, red, blue or yellow? ")
        if door.lower()[0] == 'y':
            print("We made it!! we are save!")
        elif door.lower()[0] == 'r':
            print("Burned alive :(")
            quit()
        elif door.lower()[0] == 'b':
            print("Right into the lions den :(")
        else:
            print("Thats not even a door -_-. Game Over.")
            print('''

      ,/`|;V\.;
     ,\;`~\,;\;`\,
    /;|\_|,\~/`,\/;,
   `\`/;`\,`;`|;\`\'
   ;|V`,;'|'/'`/'/|\

   `/;'|`\V'/;\,\_V/
    `;|\, |;`,_|_,'
       `,`\_\/;'
          \;`/     _____________
         \\| |    |  WARNING!   |
        _oo| |    |SOME TROLLS! |
        `\.| |    |_____________|
 ---....__/  `\,____  |    |
      _,-'     `-   ""|---.|...
               ''')
            quit()
