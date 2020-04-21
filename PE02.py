import random
import re
import sys

db = {'State': 0,  # 0:Generate / 1:Active / 2:Won / 3:Loss / 4:Post / 5:Terminate
      'Counter': {'Guess': 0, 'Win': 0, 'Loss': 0, 'Game': 0},
      'Guess': {
          'Max': 10,
          'Left': 0,
          'List': []
      },
      'Input': None,
      'List': ('adult', 'aeroplane', 'air', 'airforce', 'airport', 'album', 'alphabet', 'apple', 'arm', 'army',
               'baby', 'backpack', 'balloon', 'banana', 'bank', 'barbecue', 'bathroom', 'bathtub', 'bed', 'bee',
               'bible', 'bird', 'bomb', 'book', 'boss', 'bottle', 'bowl', 'box', 'boy', 'brain', 'bridge',
               'butterfly', 'button', 'cappuccino', 'car', 'carpet', 'carrot', 'cave', 'chair', 'chief', 'child',
               'chisel', 'chocolates', 'church', 'circle', 'circus', 'clock', 'clown', 'coffee', 'comet', 'compass',
               'computer', 'crystal', 'cup', 'cycle', 'database', 'desk', 'diamond', 'dress', 'drill', 'drink',
               'drum', 'dung', 'ears', 'earth', 'egg', 'electricity', 'elephant', 'eraser', 'explosive', 'eyes',
               'family', 'fan', 'feather', 'festival', 'film', 'finger', 'fire', 'floodlight', 'flower', 'foot',
               'fork', 'freeway', 'fruit', 'fungus', 'game', 'garden', 'gas', 'gate', 'gemstone', 'girl', 'gloves',
               'god', 'grapes', 'guitar', 'hammer', 'hat', 'hieroglyph', 'highway', 'horoscope', 'horse', 'hose',
               'ice', 'insect', 'jet fighter', 'junk', 'kaleidoscope', 'kitchen', 'knife', 'leg', 'library',
               'liquid', 'magnet', 'man', 'map', 'maze', 'meat', 'meteor', 'microscope', 'milk', 'milkshake', 'mist',
               'money', 'monster', 'mosquito', 'mouth', 'nail', 'navy', 'necklace', 'needle', 'onion', 'paintbrush',
               'pants', 'parachute', 'passport', 'pebble', 'pendulum', 'pepper', 'perfume', 'pillow', 'plane',
               'planet', 'pocket', 'potato', 'printer', 'prison', 'pyramid', 'radar', 'rainbow', 'record',
               'restaurant', 'rifle', 'ring', 'robot', 'rock', 'rocket', 'roof', 'room', 'rope', 'saddle', 'salt',
               'sandpaper', 'sandwich', 'satellite', 'school', 'sex', 'ship', 'shoes', 'shop', 'shower', 'signature',
               'skeleton', 'slave', 'snail', 'software', 'solid', 'spectrum', 'sphere', 'spice', 'spiral', 'spoon',
               'square', 'staircase', 'star', 'stomach', 'sun', 'sunglasses', 'surveyor', 'sword', 'table',
               'tapestry', 'teeth', 'telescope', 'television', 'thermometer', 'tiger', 'toilet', 'tongue', 'torch',
               'torpedo', 'train', 'treadmill', 'triangle', 'tunnel', 'typewriter', 'umbrella', 'vacuum', 'vampire',
               'videotape', 'vulture', 'water', 'weapon', 'web', 'wheelchair', 'window', 'woman', 'worm')
      }


def refresh_counter(data):
    state = db['State']
    if state is 0:  # Generate
        db['Counter']['Game'] += 1
        db['Counter']['Guess'] = 0
    elif state is 1:  # Active
        db['Counter']['Guess'] += 1
        db['Guess']['Left'] = db['Guess']['Max'] - db['Counter']['Guess']
    elif state is 2:  # Won
        db['Counter']['Win'] += 1
    elif state is 3:  # Loss
        db['Counter']['Loss'] += 1


def game():
    word = []
    workspace = []

    def create():
        word.clear()
        workspace.clear()
        selection = random.choice(db['List'])
        for char in selection:
            word.append(char.upper())
            workspace.append('*')
        db['Guess']['List'].clear()
        refresh_counter(db)
        return 1

    def exit():
        print("\n Sorry to see you go. You have won {} games and lost {} games.  See you again soon."
              .format(db['Counter']['Win'], db['Counter']['Loss']))
        db['State'] = 5

    def status():
        show_word = str(''.join(word))
        show_workspace = str(''.join(workspace))
        show_guesses = str(', '.join(db['Guess']['List']))
        if db['State'] is 1:
            print("\n Current Word: {} with {} characters."
                  "\n Previous Choices: {}"
                  "\n You have {} out of {} guesses left. \n".format(show_workspace, len(workspace), show_guesses,
                                                                     db['Guess']['Left'], db['Guess']['Max']))
        elif db['State'] is 2:
            refresh_counter(db)
            print("\n Congratulations, You won this round with the word {}."
                  "\n You have won {} games and lost {} games.".format(show_workspace, db['Counter']['Win']
                                                                       , db['Counter']['Loss']))
        elif db['State'] is 3:
            refresh_counter(db)
            print("\n Sorry, You lost this round. The word you were looking for was {}."
                  "\n You have won {} games and lost {} games.".format(show_word, db['Counter']['Win']
                                                                       , db['Counter']['Loss']))
        elif db['State'] is 4:
            prompt = input("Would you like to play again? ('y' for yes or 'n' for no): ").lower()
            if prompt == 'y':
                db['State'] = 0
                db['State'] = create()
            elif prompt == 'n':
                exit()

    def validate(data):
        if data is '!':
            exit()
            refresh_counter(db)
            return None
        elif not data.isalpha() and len(data) == 1 or data.upper() in db['Guess']['List']:
            if not data.isalpha() and len(data) == 1:
                print("{} is invalid input. Single letters are only acceptable input.".format(data))
            elif data.upper() in db['Guess']['List']:
                print("{} has already been used in this round.".format(data.upper()))
            refresh_counter(db)
            return None
        else:
            return data.upper()

    def process():
        if db['Input'] in word:
            word_indexes = [i for i, x in enumerate(word) if x == str(db['Input'])]
            for word_index in word_indexes:
                workspace.pop(word_index)
                workspace.insert(word_index, db['Input'])
        else:
            print("{} is not a winning letter for you.  Please choose again.".format(db['Input']))
        db['Guess']['List'].append(str(db['Input']))
        db['Input'] = None
        refresh_counter(db)
        return

    while db['State'] != 5:
        if not word:
            db['State'] = create()
        elif db['Counter']['Guess'] <= db['Guess']['Max']:
            if word != workspace:
                if db['Input'] is None:
                    status()
                    prompt = input("Please choose a single letter from the alphabet ('!' to quit): ")
                    db['Input'] = validate(prompt)
                else:
                    process()
            else:
                db['State'] = 2
                status()
                db['State'] = 4
                status()
        else:
            db['State'] = 3
            status()
            db['State'] = 4
            status()


if __name__ == "__main__":
    game()
