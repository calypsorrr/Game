#!/usr/bin/env python
"""
It's a game
"""


import sys
import os
import time
import pygame


__author__ = "Bo Claes"
__email__ = "bo.claes@student.kdg.be"
__status__ = "Deployed"


screen_width = 100

##### Player Setup #####
class player:
    def __init__(self):
        self.name = ''
        self.feeling = ''
        self.astrological = ''
        self.location = 'b2'
        self.solves = 0
        self.won = False
        self.hp = 20
        self.count = 0
        self.key = 0
        self.sword = 0
        self.skeleton_bones = 0

class skeleton:
    def __init__(self):
        self.hp = 10

myPlayer = player()
myskeleton = skeleton()

pygame.mixer.init()
victory_music_end = pygame.mixer.Sound("music/victory_music_end.mp3")
punch = pygame.mixer.Sound("music/punch.mp3")
flee = pygame.mixer.Sound("music/run.mp3")
sword_skeleton = pygame.mixer.Sound("music/sword_skeleton.mp3")
sword_skeleton_u = pygame.mixer.Sound("music/sword_skeleton_u.mp3")
bell = pygame.mixer.Sound("music/bell_church.mp3")
victory_game = pygame.mixer.Sound("music/victory game.mp3")
key_sound = pygame.mixer.Sound("music/pick key.mp3")
locked_sound = pygame.mixer.Sound("music/locked.mp3")
solved = pygame.mixer.Sound("music/Puzzle Solved.mp3")
sword_sound = pygame.mixer.Sound("music/sword.mp3")
witch = pygame.mixer.Sound("music/witch.mp3")
iron = pygame.mixer.Sound("music/door.mp3")
road = pygame.mixer.Sound("music/road.mp3")
home_sound = pygame.mixer.Sound("music/Home.mp3")
crypt = pygame.mixer.Sound("music/crypt.mp3")
basment = pygame.mixer.Sound("music/basement.mp3")
cemetery = pygame.mixer.Sound("music/graveyard.mp3")
monk_blessing = pygame.mixer.Sound("music/monk.mp3")
door_church = pygame.mixer.Sound("music/church door.mp3")
step = pygame.mixer.Sound("music/step.mp3")
kill = pygame.mixer.Sound("music/evil.mp3")
door_town = pygame.mixer.Sound("music/door mayor.mp3")
food = pygame.mixer.Sound("music/food.mp3")
victory = pygame.mixer.Sound("music/victory.mp3")
game_sound = pygame.mixer.music.load("26-Terra's Theme-FFVI OST.wav")
battle_sound = pygame.mixer.Sound("music/battle.mp3")

pygame.mixer.init()
pygame.mixer.music.play(-1)

def reset_player():
    myPlayer.location = 'b2'
    myPlayer.hp = 20
    myPlayer.solves = 0
    myPlayer.count = 0
    myPlayer.key = 0
    myPlayer.sword = 0
    myPlayer.skeleton_bones = 0

def reset_skeleton():
    myskeleton.hp = 10

##### Title Screen #####
def title_screen_selections():
    option = input("> ")
    if option.lower() == ("play"):
        setup_game()
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("quit"):
        sys.exit()
    while option.lower() not in ['play', 'help', 'quit']:
        print("please enter a valid command")
        option = input("> ")
        if option.lower() == ("play"):
            setup_game()
        elif option.lower() == ("help"):
            help_menu()
        elif option.lower() == ("quit"):
            sys.exit()

def title_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('############################')
    print('#    The lonely puzzle!    #')
    print('############################')
    print('          - play -          ')
    print('          - help -          ')
    print('          - quit -          ')
    print('  Copyright 2021 Bo Claes   ')
    title_screen_selections()

def help_menu():
    print('#############################################')
    print('#######   Welcome to the text RPG!     ######')
    print('#############################################')
    print('    - Use up, Down, Left, Right to move -    ')
    print('      - Type your commands to do them -      ')
    print('     - Use "look" to inspect something -     ')
    print('        - Good luck and have fun! -          ')
    print(' - Type play if you want to go on a adventure')
    title_screen_selections()

##### Map #####

ZONENAME = ""
DESCRIPTION = 'description'
EXAMINATION = 'examine'
SOLVED = False
UP = 'up', 'north'
DOWN = 'down', 'south'
LEFT = 'left', 'west'
RIGHT = 'right', 'east'

solved_places = {'a1': False, 'a2': '1', 'a3': '1', 'a4': False,
                'b1': '1', 'b2': False, 'b3': False, 'b4': False,
                'c1': False, 'c2': False, 'c3': False, 'c4': False,
                'd1': False, 'd2': False, 'd3': False, 'd4': False,
                }

zonemap = {
    'a1': {
        ZONENAME: 'Town Market',
        DESCRIPTION: 'The market is abandoned, only rotten food fills the air - but you see a sign.',
        EXAMINATION: 'What goes up but never comes down, every person has it. What am I?',
        SOLVED: False,
        UP: '',
        DOWN: '',
        LEFT: '',
        RIGHT: 'a2',
    },

    'a2': {
        ZONENAME: 'Town Entrance',
        DESCRIPTION: 'The gate opens by itself... Strange normally there would be guards around.',
        EXAMINATION: 'The gate is made out of bones and the town feels abandoned.',
        SOLVED: True,
        UP: '',
        DOWN: 'b2',
        LEFT: 'a1',
        RIGHT: 'a3',
    },

    'a3': {
        ZONENAME: 'Town Square',
        DESCRIPTION: 'The town square is totally empty, it gives you chills.',
        EXAMINATION: 'You see on the right the town hall. \nThere is light shining true a window... I should go'
                     ' take a look. \nOr I can go down into the church, they say strange people live there.',
        SOLVED: True,
        UP: '',
        DOWN: 'b3',
        LEFT: 'a2',
        RIGHT: 'a4',
    },

    'a4': {
        ZONENAME: 'Town Hall',
        DESCRIPTION: 'You go inside and see a person behind a desk, maybe I should go talk to him. \n'
                     'But first I should look at the TOWN ENTRANCE...',
        EXAMINATION: 'It has been so long since I have been outside these doors... \n'
                     'Hey mate, can you tell me what the old gate is made off?',
        SOLVED: False,
        UP: '',
        DOWN: 'b4',
        LEFT: 'a3',
        RIGHT: '',
    },

    'b1': {
        ZONENAME: "crypt",
        DESCRIPTION: 'A spooky crypt with lots of bones and skeletons.',
        EXAMINATION: 'I hear loud noises coming up the stairs, maybe I should go look.',
        SOLVED: True,
        UP: '',
        DOWN: 'c1',
        LEFT: '',
        RIGHT: 'b2',
    },

    'b2': {
        ZONENAME: 'Home',
        DESCRIPTION: 'This is your home!',
        EXAMINATION: 'Your home looks the same - nothing has changed, but there is a safe with a five number code. '
                     '\nGive it a try when you have the 5 digits.',
        SOLVED: False,
        UP: 'a2',
        DOWN: 'c2',
        LEFT: 'b1',
        RIGHT: '',
    },

    'b3': {
        ZONENAME: 'Church',
        DESCRIPTION: 'The church bells rings 5 times when you approach it. \nInside there is a priest that stares at'
                     ' a strange table',
        EXAMINATION: "Each side of the table has a unique symbol, though all are familiar to you. \nWhich symbol do you"
                     " sit by?",
        SOLVED: False,
        UP: 'a3',
        DOWN: '',
        LEFT: '',
        RIGHT: '',
    },

    'b4': {
        ZONENAME: 'Basement',
        DESCRIPTION: 'It is empty, but you see a safe with a keyhole. \nMaybe you need a closer look.',
        EXAMINATION: 'You can use a key here... If you have one.',
        SOLVED: False,
        UP: 'a4',
        DOWN: '',
        LEFT: '',
        RIGHT: '',
    },

    'c1': {
        ZONENAME: 'Crypt basement',
        DESCRIPTION: 'You see a traveler chained up, maybe I should free him, '
                     'but he seems confused and may ask the time.',
        EXAMINATION: '\nThank you sir/madam I thought for sure I would die here. \nAnyway do you know what time it is?',
        SOLVED: False,
        UP: 'b1',
        DOWN: '',
        LEFT: '',
        RIGHT: '',
    },

    'c2': {
        ZONENAME: 'road',
        DESCRIPTION: 'This is a road with a thick mist, but you see something shining on the side of the road  ',
        EXAMINATION: 'you see a key on the side of the road, you want to pick it up?',
        SOLVED: False,
        UP: 'b2',
        DOWN: '',
        LEFT: '',
        RIGHT: 'c3',
    },

    'c3': {
        ZONENAME: 'Graveyard',
        DESCRIPTION: 'It is still foggy, but you see in the distance something moving...',
        EXAMINATION: 'It is a skeleton... it comes right at you. \nYou should flee or fight.',
        SOLVED: False,
        UP: '',
        DOWN: '',
        LEFT: 'c2',
        RIGHT: 'c4',
    },

    'c4': {
        ZONENAME: 'Witches house',
        DESCRIPTION: 'It looks like a scary place and I can see some light true a window... \n'
                     'I can see a woman outside and she is doing something in a pot. '
                     '\nMaybe i could talk to her, but beware she needs something.',
        EXAMINATION: 'I hope you have some skeleton bones with you...',
        SOLVED: False,
        UP: '',
        DOWN: '',
        LEFT: 'c3',
        RIGHT: '',
    },

}

##### Game Interactivity #####
def print_location():
    print('\n' + ('#' * (4 + len(zonemap[myPlayer.location][ZONENAME]))))
    print('# ' + (zonemap[myPlayer.location][ZONENAME] + ' #'))
    print(('#' * (4 + len(zonemap[myPlayer.location][ZONENAME]))))
    print('\n' + (zonemap[myPlayer.location][DESCRIPTION]))


def prompt():
    print("\n" + "=======================")
    print("What would you like to do? You can choose between for example [move or look].")
    action = input("> ")
    acceptable_actions = ['move', 'go', 'travel', 'walk', 'quit', 'examine', 'inspect', 'interact', 'look',
                          'examine sign', 'talk', 'look at sign', 'read sign', 'attack', 'strike', 'free him', 'inspect'
                          , 'look around', 'kill mayor', 'kill priest', 'fight', 'kill witch']
    while action.lower() not in acceptable_actions:
        print("Unknown action, the actions are for example [Move, examine, travel, look], try again.\n")
        action = input("> ")
    if action.lower() == 'quit':
        sys.exit()
    elif action.lower() in ['move', 'go', 'travel', 'walk']:
        player_move(action.lower())
    elif action.lower() in ['examine', 'inspect', 'interact', 'look', 'examine sign', 'talk', 'look at sign',
                            'read sign', 'free him', 'inspect', 'look around']:
        player_examine(action.lower())
    elif action.lower() in ['kill mayor', 'kill priest', 'kill witch']:
        player_death(action.lower())

def player_death(action):
    pygame.mixer.Sound.play(kill)
    os.system('cls' if os.name == 'nt' else 'clear')
    attack_1 = ("You killed a innocent person.\nThe shadow consumed you.\n")
    for charaters in attack_1:
        sys.stdout.write(charaters)
        sys.stdout.flush()
        time.sleep(0.1)
    print()
    print(" You want to Try Again?\n~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("1: Yes I want to defeat the darkness.")
    print("2: No, just let the darkness win, I quit.")
    restart = input("> ")
    if restart == '1':
        pygame.mixer.init()
        pygame.mixer.music.play(-1)
        reset_player()
        reset_skeleton()
        title_screen()
    else:
        sys.exit()


def player_move(myAction):
    ask = "Where would you like to move to? choose between [up, down, left or right].\n"
    dest = input(ask)
    if dest in ['up', 'north']:
        destination = zonemap[myPlayer.location][UP]
        movement_handeler(destination)
    elif dest in ['left', 'west']:
        destination = zonemap[myPlayer.location][LEFT]
        movement_handeler(destination)
    elif dest in ['right', 'east']:
        destination = zonemap[myPlayer.location][RIGHT]
        movement_handeler(destination)
    elif dest in ['down', 'south']:
        destination = zonemap[myPlayer.location][DOWN]
        movement_handeler(destination)
    else:
        print("Invalid direction command, try using up, down, left, or right.\n")
        player_move(myAction)

def movement_handeler(destination):
    if destination in ['a3', 'c1']:
        pygame.mixer.Sound.stop(iron)
        pygame.mixer.Sound.stop(crypt)
        pygame.mixer.Sound.stop(door_town)
        pygame.mixer.Sound.stop(door_church)
        pygame.mixer.Sound.stop(bell)
        pygame.mixer.Sound.play(step)
        print("\n" + "You have moved to " + destination + ".")
        myPlayer.location = destination
        print_location()
    elif destination == '':
        print('A shadow is blocking you, you need to find another way.')
        player_move('myAction')
    elif destination is 'b3':
        pygame.mixer.Sound.stop(step)
        pygame.mixer.Sound.play(bell)
        pygame.mixer.Sound.play(door_church)
        print("\n" + "You have moved to " + destination + ".")
        myPlayer.location = destination
        print_location()
    elif destination is 'a4':
        pygame.mixer.Sound.stop(step)
        pygame.mixer.Sound.stop(basment)
        pygame.mixer.Sound.play(door_town)
        print("\n" + "You have moved to " + destination + ".")
        myPlayer.location = destination
        print_location()
    elif destination is 'b2':
        pygame.mixer.Sound.stop(iron)
        pygame.mixer.Sound.stop(road)
        pygame.mixer.Sound.stop(crypt)
        pygame.mixer.Sound.play(home_sound)
        print("\n" + "You have moved to " + destination + ".")
        myPlayer.location = destination
        print_location()
    elif destination is 'b1':
        pygame.mixer.Sound.stop(home_sound)
        pygame.mixer.Sound.stop(step)
        pygame.mixer.Sound.play(crypt)
        print("\n" + "You have moved to " + destination + ".")
        myPlayer.location = destination
        print_location()
    elif destination is 'b4':
        pygame.mixer.Sound.stop(door_town)
        pygame.mixer.Sound.play(basment)
        print("\n" + "You have moved to " + destination + ".")
        myPlayer.location = destination
        print_location()
    elif destination is 'a1':
        pygame.mixer.Sound.stop(iron)
        pygame.mixer.Sound.play(food)
        print("\n" + "You have moved to " + destination + ".")
        myPlayer.location = destination
        print_location()
    elif destination is 'c3':
        pygame.mixer.Sound.stop(witch)
        pygame.mixer.Sound.stop(road)
        pygame.mixer.Sound.play(cemetery)
        print("\n" + "You have moved to " + destination + ".")
        myPlayer.location = destination
        print_location()
    elif destination is 'c2':
        pygame.mixer.Sound.stop(cemetery)
        pygame.mixer.Sound.stop(home_sound)
        pygame.mixer.Sound.play(road)
        print("\n" + "You have moved to " + destination + ".")
        myPlayer.location = destination
        print_location()
    elif destination is 'a2':
        pygame.mixer.Sound.stop(home_sound)
        pygame.mixer.Sound.stop(food)
        pygame.mixer.Sound.stop(step)
        pygame.mixer.Sound.play(iron)
        print("\n" + "You have moved to " + destination + ".")
        myPlayer.location = destination
        print_location()
    elif destination is 'c4':
        pygame.mixer.Sound.stop(cemetery)
        pygame.mixer.Sound.play(witch)
        print("\n" + "You have moved to " + destination + ".")
        myPlayer.location = destination
        print_location()

def player_examine(action):
    if solved_places[myPlayer.location] == False:
        print((zonemap[myPlayer.location][EXAMINATION]))
        puzzle_answer = input("> ")
        checkpuzzle(puzzle_answer)
    elif solved_places[myPlayer.location] == '1':
        print((zonemap[myPlayer.location][EXAMINATION]))
        prompt()
    else:
        print("There is nothing new to see here.")

def attack_no_sword():
    for n in range (4):
        if myPlayer.count is not 3:
            attack_14 = ("\nThe skeleton swings with his sword.")
            for character in attack_14:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.08)
            pygame.mixer.Sound.play(sword_skeleton)
            myPlayer.hp -= 5
            myPlayer.count += 1
            attack_15 = ("\nSkeleton's health: " + str(myskeleton.hp))
            for character in attack_15:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.08)
            attack_16 = ("\nYour health: " + str(myPlayer.hp))
            for character in attack_16:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.08)
            attack_17 = ("\nYou punch him again.")
            for character in attack_17:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.08)
            pygame.mixer.Sound.play(punch)
            myskeleton.hp -= 2
            attack_18 = ("\nSkeleton's health: " + str(myskeleton.hp))
            for character in attack_18:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.08)
            attack_19 = ("\nYour health: " + str(myPlayer.hp))
            for character in attack_19:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.08)
        elif myPlayer.count is 3:
            attack_87 = ("\nThe skeleton swings with his sword.")
            myPlayer.hp -= 5
            for character in attack_87:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.08)
            pygame.mixer.Sound.play(sword_skeleton)
            attack_98 = ("\nSkeleton's health: " + str(myskeleton.hp))
            for character in attack_98:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.08)
            attack_79 = ("\nYour health: " + str(myPlayer.hp))
            for character in attack_79:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.08)
            time.sleep(1)
            game_over()

def checkpuzzle(puzzle_answer):
    if myPlayer.location == 'c3':
        if puzzle_answer == 'fight':
            os.system('cls' if os.name == 'nt' else 'clear')
            pygame.mixer.Sound.stop(cemetery)
            pygame.mixer.Sound.play(battle_sound)
            attack_1 = ("You are now in fight mode. \nThis progress will go automaticly\n")
            for character in attack_1:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.08)
            if myPlayer.sword == 1:
                attack_2 = ("You have a sword, so you have more damage. \nYou swing your sword for 5 damage.")
                for character in attack_2:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.08)
                pygame.mixer.Sound.play(sword_skeleton_u)
                myskeleton.hp -= 5
                attack_3 = ("\nSkeleton's health: " + str(myskeleton.hp))
                for character in attack_3:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.08)
                attack_4 = ("\nYour health: " + str(myPlayer.hp))
                for character in attack_4:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.08)
                attack_5 = ("\nThe skeleton swings with his sword.")
                for character in attack_5:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.08)
                pygame.mixer.Sound.play(sword_skeleton_u)
                myPlayer.hp -= 5
                myPlayer.count += 1
                attack_6 = ("\nSkeleton's health: " + str(myskeleton.hp))
                for character in attack_6:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.08)
                attack_7 = ("\nYour health: " + str(myPlayer.hp))
                for character in attack_7:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.08)
                attack_8 = ("\nYou swing your sword again.")
                for character in attack_8:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.08)
                pygame.mixer.Sound.play(sword_skeleton_u)
                myskeleton.hp -= 5
                attack_9 = ("\nThe skeleton has no more hp and died.")
                for character in attack_9:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.08)
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
                pygame.mixer.Sound.stop(battle_sound)
                pygame.mixer.Sound.play(victory)
                attack_10 = ("The skeleton has a number written on the side of his sword, it says - 6 - ")
                for character in attack_10:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.08)
                solved_places[myPlayer.location] = True
                myPlayer.solves += 1
                myPlayer.skeleton_bones += 1
                print("\nPuzzles solved: " + str(myPlayer.solves))
                attack_11 = ("You picked up some bones from the skeleton as well. \nMaybe these will come in handy later\n")
                for character in attack_11:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.08)
            elif myPlayer.sword == 0:
                attack_11 = ("You dont have a sword, so your damage will be lower. \nYou punch the ugly bastard.")
                for character in attack_11:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.08)
                pygame.mixer.Sound.play(punch)
                myskeleton.hp -= 2
                attack_12 = ("\nSkeleton's health: " + str(myskeleton.hp))
                for character in attack_12:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.08)
                attack_13 = ("\nYour health: " + str(myPlayer.hp))
                for character in attack_13:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.08)
                attack_no_sword()
                attack_20 = ("\nThe skeleton has no more hp and died.")
                for character in attack_20:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.08)
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
                pygame.mixer.Sound.stop(battle_sound)
                pygame.mixer.Sound.play(victory)
                attack_21 = ("The skeleton has a number written on the side of his sword, it says - 6 -"
                             "\nThis is the second number of the vault. ")
                for character in attack_21:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.08)
                solved_places[myPlayer.location] = True
                myPlayer.solves += 1
                myPlayer.skeleton_bones += 1
                print("\nPuzzles solved: " + str(myPlayer.solves))
                attack_22 = ("You picked up some bones from the skeleton as well. "
                             "\nMaybe these will come in handy later\n")
                for character in attack_22:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.08)
                prompt()
        elif myPlayer.count == 3:
            time.sleep(1)
            game_over()
        elif puzzle_answer is 'fight' and myPlayer.solves == 4:
            home()
        elif puzzle_answer == 'flee':
            pygame.mixer.Sound.play(flee)
            run_1 = ("You ran from the fight.\n")
            for character in run_1:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            prompt()

    elif myPlayer.location == 'c4':
        if puzzle_answer == 'use skeleton bones':
            solved_places[myPlayer.location] = True
            myPlayer.solves += 1
            os.system('cls' if os.name == 'nt' else 'clear')
            pygame.mixer.Sound.play(solved)
            witch_1 = ("Thank you kind stranger.\nI heard there is a vault in the darkness and one of the numbers of"
                       " this vault is - 8 - \nThis is the last number of the vault."
                       "\nNow go, I have business to attend to.")
            for characters in witch_1:
                sys.stdout.write(characters)
                sys.stdout.flush()
                time.sleep(0.05)
            print("\nPuzzles solved: " + str(myPlayer.solves))
        elif myPlayer.skeleton_bones is 0 and myPlayer.count is not 3:
            witch_2 = ("\nSo you dont have what I want... Maybe I just have to take it from your ugly body.")
            for characters in witch_2:
                sys.stdout.write(characters)
                sys.stdout.flush()
                time.sleep(0.05)
            witch_3 = ("\nCome back when you have what I want. ")
            for characters in witch_3:
                sys.stdout.write(characters)
                sys.stdout.flush()
                time.sleep(0.08)
            myPlayer.hp -= 5
            myPlayer.count += 1
            witch_4 = ("\nYou have been damaged by 5 health points. \nYour total health is " + str(myPlayer.hp))
            for characters in witch_4:
                sys.stdout.write(characters)
                sys.stdout.flush()
                time.sleep(0.05)
        elif puzzle_answer is not 'use skeleton bones' and myPlayer.count is 3:
            game_over()


    elif myPlayer.location == 'c2':
        if puzzle_answer == 'pick up key':
            myPlayer.key += 1
            os.system('cls' if os.name == 'nt' else 'clear')
            pygame.mixer.Sound.play(key_sound)
            key_1 = ("You picked up the shiny key and it says 'Vault mayor'. \nMaybe you should go to the town hall."
                     "\n")
            for character in key_1:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            print("\nKey count: " + str(myPlayer.key))
        else:
            print("You ignore the key")

    elif myPlayer.location == 'b4':
        if myPlayer.key is 1 and puzzle_answer == 'use key':
            myPlayer.sword += 1
            os.system('cls' if os.name == 'nt' else 'clear')
            pygame.mixer.Sound.play(sword_sound)
            sword_1 = ("The safe opens and inside you find a sword. \nYou picked it up.\n")
            for character in sword_1:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
        elif myPlayer.key is 0 and puzzle_answer == 'use key':
            pygame.mixer.Sound.play(locked_sound)
            print("You try to break it open without a key but it was no use...")
            prompt()
        else:
            print("You try to break it open without a key but it was no use...")
            prompt()

    elif myPlayer.location == 'b2':
        if puzzle_answer == '36298':
            pygame.mixer.Sound.play(victory_music_end)
            os.system('cls' if os.name == 'nt' else 'clear')
            endspeech = (
                "The vault opens and in the vault lays a paper. \nYou read the paper and it says - You where in a game"
                " the whole time. \nHeh. Heh.. Heh... \nGood job " + myPlayer.name)
            for character in endspeech:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.12)
            time.sleep(2)
            sys.exit()
        else:
            print("Nothing seems to happen still...")

    elif myPlayer.location == 'a1':
        if puzzle_answer == 'age':
            solved_places[myPlayer.location] = True
            myPlayer.solves += 1
            os.system('cls' if os.name == 'nt' else 'clear')
            pygame.mixer.Sound.play(solved)
            good = ("You have solved the puzzle, a number of the vault is - 2 - . Now, onwards!")
            for characters in good:
                sys.stdout.write(characters)
                sys.stdout.flush()
                time.sleep(0.05)
            print("\nPuzzles solved: " + str(myPlayer.solves))
        elif puzzle_answer is not 'age' and myPlayer.count is not 3:
            myPlayer.hp -= 5
            myPlayer.count += 1
            end = ("\nWrong answer! you have been damaged for 5 health, your total health is " + str(myPlayer.hp)) + "\n"
            for charaters in end:
                sys.stdout.write(charaters)
                sys.stdout.flush()
                time.sleep(0.05)
            print("You want to Try Again?\n~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("1: Yes I want to solve it.")
            print("2: No I want to go somewhere else.")
            restart = input("> ")
            if restart == '1':
                player_examine('action')
            elif restart == '2':
                prompt()
        elif puzzle_answer is not 'age' and myPlayer.count == 3:
            game_over()
        elif puzzle_answer is 'age' and myPlayer.solves == 4:
            home()

    elif myPlayer.location == 'a4':
        if puzzle_answer == 'bones':
            solved_places[myPlayer.location] = True
            myPlayer.solves += 1
            os.system('cls' if os.name == 'nt' else 'clear')
            pygame.mixer.Sound.play(solved)
            good = ("You have solved the puzzle, a number of the vault is - 3 - .\nThis is the first number of the "
                    "vault.\nNow onwards!")
            for characters in good:
                sys.stdout.write(characters)
                sys.stdout.flush()
                time.sleep(0.05)
            print("\nPuzzles solved: " + str(myPlayer.solves))
        elif puzzle_answer is not 'iron' and myPlayer.count is not 3:
            myPlayer.hp -= 5
            myPlayer.count += 1
            end = ("\nWrong answer! you have been damaged for 5 health, your total health is " + str(
                myPlayer.hp)) + "\n"
            for charaters in end:
                sys.stdout.write(charaters)
                sys.stdout.flush()
                time.sleep(0.05)
            print("you want to Try again?\n~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("1: Yes I want to solve it.")
            print("2: No I want to go somewhere else.")
            restart = input("> ")
            if restart == '1':
                player_examine('action')
            elif restart == '2':
                prompt()
        elif puzzle_answer is not 'iron' and myPlayer.count == 3:
            game_over()
        elif puzzle_answer is 'iron' and myPlayer.solves == 4:
            home()
        elif puzzle_answer is 'i do not know':
            prompt()

    elif myPlayer.location == 'b3':
        if puzzle_answer == (myPlayer.astrological):
            solved_places[myPlayer.location] = True
            myPlayer.hp += 10
            myPlayer.count -= 2
            os.system('cls' if os.name == 'nt' else 'clear')
            pygame.mixer.Sound.play(monk_blessing)
            good = ("You have solved the puzzle, the priest blessed you with 10 health points \nyour hp is now "
                    + str(myPlayer.hp))
            for characters in good:
                sys.stdout.write(characters)
                sys.stdout.flush()
                time.sleep(0.05)
        elif puzzle_answer is not (myPlayer.astrological):
            end = ("The priest looks funny at you and just says 'that's not it my man'\n")
            for charaters in end:
                sys.stdout.write(charaters)
                sys.stdout.flush()
                time.sleep(0.05)
            print("you want to Try again?\n~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("1: Yes I want to solve it.")
            print("2: No I want to go somewhere else.")
            restart = input("> ")
            if restart == '1':
                player_examine('action')
            elif restart == '2':
                prompt()


    elif myPlayer.location == 'c1':
        if puzzle_answer == "5 o'clock":
            solved_places[myPlayer.location] = True
            myPlayer.solves += 1
            os.system('cls' if os.name == 'nt' else 'clear')
            pygame.mixer.Sound.play(solved)
            good = ("You have solved the puzzle, a number of the vault is - 9 - . Now, onwards!")
            for characters in good:
                sys.stdout.write(characters)
                sys.stdout.flush()
                time.sleep(0.05)
            print("\nPuzzles solved: " + str(myPlayer.solves))
        elif puzzle_answer is not '5 a clock' and myPlayer.count is not 3:
            myPlayer.hp -= 5
            myPlayer.count += 1
            end = ("\nWrong answer! you have been damaged for 5 health, your total health is " + str(
                myPlayer.hp)) + "\n"
            for charaters in end:
                sys.stdout.write(charaters)
                sys.stdout.flush()
                time.sleep(0.05)
            print("you want to Try again?\n~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("1: Yes I want to solve it.")
            print("2: No I want to go somewhere else.")
            restart = input("> ")
            if restart == '1':
                player_examine('action')
            elif restart == '2':
                prompt()
        elif puzzle_answer is not '5 a clock' and myPlayer.count == 3:
            game_over()
        elif puzzle_answer is '5 a clock' and myPlayer.solves == 4:
            home()
        elif puzzle_answer is 'i do not know':
            prompt()

def home():
    os.system('cls' if os.name == 'nt' else 'clear')
    home_1 = ("You have all the numbers now for the save, go get your ass over there!!!")
    for charaters in home_1:
        sys.stdout.write(charaters)
        sys.stdout.flush()
        time.sleep(0.1)
        prompt()

def game_over():
    pygame.mixer.Sound.stop(battle_sound)
    pygame.mixer.Sound.play(kill)
    os.system('cls' if os.name == 'nt' else 'clear')
    game_over_1 = ("The darkness has consumed you\n")
    for charaters in game_over_1:
        sys.stdout.write(charaters)
        sys.stdout.flush()
        time.sleep(0.1)
    print()
    print(" you want to Try again?\n~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("1: Yes I want to defeat the darkness.")
    print("2: No, just let the darkness win, I quit.")
    restart = input("> ")
    if restart == '1':
        pygame.mixer.init()
        pygame.mixer.music.play(-1)
        reset_player()
        reset_skeleton()
        title_screen()
    else:
        sys.exit()


def main_game_loop():
    total_puzzles = 5
    while myPlayer.won is False:
        prompt()


def setup_game():
    os.system('cls' if os.name == 'nt' else 'clear')

    # QUESTION NAME: Obtains the player's name.
    question1 = "Hello there, what is your name?\n"
    for character in question1:
        # This will occur throughout the intro code.  It allows the string to be typed gradually - like a typerwriter effect.
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player_name = input("> ")
    myPlayer.name = player_name

    # QUESTION FEELING: Obtains the player's feeling.
    question2 = "My dear friend " + myPlayer.name + ", how are you feeling?\n"
    for character in question2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    feeling = input("> ")
    myPlayer.feeling = feeling.lower()

    # Creates the adjective vocabulary for the player's feeling.
    good_adj = ['good', 'great', 'rohit', 'happy', 'aight', 'understanding', 'great', 'alright', 'calm', 'confident',
                'not bad', 'courageous', 'peaceful', 'reliable', 'joyous', 'energetic', 'at', 'ease', 'easy', 'lucky',
                'k', 'comfortable', 'amazed', 'fortunate', 'optimistic', 'pleased', 'free', 'delighted', 'swag',
                'encouraged', 'ok', 'overjoyed', 'impulsive', 'clever', 'interested', 'gleeful', 'free', 'surprised',
                'satisfied', 'thankful', 'frisky', 'content', 'receptive', 'important', 'animated', 'quiet', 'okay',
                'festive', 'spirited', 'certain', 'kind', 'ecstatic', 'thrilled', 'relaxed', 'satisfied', 'wonderful',
                'serene', 'glad', 'free', 'and', 'easy', 'cheerful', 'bright', 'sunny', 'blessed', 'merry', 'reassured',
                'elated', '1914', 'love', 'interested', 'positive', 'strong', 'loving']
    hmm_adj = ['idk', 'concerned', 'lakshya', 'eager', 'impulsive', 'considerate', 'affected', 'keen', 'free',
               'affectionate', 'fascinated', 'earnest', 'sure', 'sensitive', 'intrigued', 'intent', 'certain', 'tender',
               'absorbed', 'anxious', 'rebellious', 'devoted', 'inquisitive', 'inspired', 'unique', 'attracted', 'nosy',
               'determined', 'dynamic', 'passionate', 'snoopy', 'excited', 'tenacious', 'admiration', 'engrossed',
               'enthusiastic', 'hardy', 'warm', 'curious', 'bold', 'secure', 'touched', 'brave', 'sympathy', 'daring',
               'close', 'challenged', 'loved', 'optimistic', 'comforted', 're', 'enforced', 'drawn', 'toward',
               'confident', 'hopeful', 'difficult']
    bad_adj = ['bad', 'meh', 'sad', 'hungry', 'unpleasant', 'feelings', 'angry', 'depressed', 'confused', 'helpless',
               'irritated', 'lousy', 'upset', 'incapable', 'enraged', 'disappointed', 'doubtful', 'alone', 'hostile',
               'discouraged', 'uncertain', 'paralyzed', 'insulting', 'ashamed', 'indecisive', 'fatigued', 'sore',
               'powerless', 'perplexed', 'useless', 'annoyed', 'diminished', 'embarrassed', 'inferior', 'upset',
               'guilty', 'hesitant', 'vulnerable', 'hateful', 'dissatisfied', 'shy', 'empty', 'unpleasant', 'miserable',
               'stupefied', 'forced', 'offensive', 'detestable', 'disillusioned', 'hesitant', 'bitter', 'repugnant',
               'unbelieving', 'despair', 'aggressive', 'despicable', 'skeptical', 'frustrated', 'resentful',
               'disgusting', 'distrustful', 'distressed', 'inflamed', 'abominable', 'misgiving', 'woeful', 'provoked',
               'terrible', 'lost', 'pathetic', 'incensed', 'in', 'despair', 'unsure', 'tragic', 'infuriated', 'sulky',
               'uneasy', 'cross', 'bad', 'pessimistic', 'dominated', 'worked', 'up', 'a', 'sense', 'of', 'loss',
               'tense', 'boiling', 'fuming', 'indignant', 'indifferent', 'afraid', 'hurt', 'sad', 'insensitive',
               'fearful', 'crushed', 'tearful', 'dull', 'terrified', 'tormented', 'sorrowful', 'nonchalant',
               'suspicious', 'deprived', 'pained', 'neutral', 'anxious', 'pained', 'grief', 'reserved', 'alarmed',
               'tortured', 'anguish', 'weary', 'panic', 'dejected', 'desolate', 'bored', 'nervous', 'rejected',
               'desperate', 'preoccupied', 'scared', 'injured', 'pessimistic', 'cold', 'worried', 'offended', 'unhappy',
               'disinterested', 'frightened', 'afflicted', 'lonely', 'lifeless', 'timid', 'aching', 'grieved', 'shaky',
               'victimized', 'mournful', 'restless', 'heartbroken', 'dismayed', 'doubtful', 'agonized', 'threatened',
               'appalled', 'cowardly', 'humiliated', 'quaking', 'wronged', 'menaced', 'alienated', 'wary', 'stressful']

    # Identifies what type of feeling the player is having and gives a related-sounding string.
    if myPlayer.feeling in good_adj:
        feeling_string = "I am glad you feel"
    elif myPlayer.feeling in hmm_adj:
        feeling_string = "that is interesting you feel"
    elif myPlayer.feeling in bad_adj:
        feeling_string = "I am sorry to hear you feel"
    else:
        feeling_string = "I do not know what it is like to feel"

    # Combines all the above parts.
    question3 = "Well then, " + myPlayer.name + ", " + feeling_string + " " + myPlayer.feeling + ".\n"
    for character in question3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)

    # QUESTION SIGN: Obtains the player's astrological sign for a later puzzle.
    question4 = "Now tell me, what is your astrological sign?\n"
    for character in question4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)

    # Prints the astrological sign guide for the player.  Also converts text to be case-insensitive, as with most inputs.
    print("#####################################################")
    print("# Please print the proper name to indicate your sign.")
    print("# ♈ Aries (The Ram)")
    print("# ♉ Taurus (The Bull)")
    print("# ♊ Gemini (The Twins)")
    print("# ♋ Cancer (The Crab)")
    print("# ♌ Leo (The Lion)")
    print("# ♍ Virgo (The Virgin)")
    print("# ♎ Libra (The Scales)")
    print("# ♏ Scorpio (The Scorpion)")
    print("# ♐ Sagittarius (Centaur)")
    print("# ♑ Capricorn (The Goat)")
    print("# ♒ Aquarius (The Water Bearer)")
    print("# ♓ Pisces (The Fish)")
    print("#####################################################")
    astrological = input("> ")
    acceptable_signs = ['aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo', 'libra', 'scorpio', 'sagittarius',
                        'capricorn', 'aquarius', 'pisces']
    # Forces the player to write an acceptable sign, as this is essential to solving a puzzle later.  Also stores it in class.

    while astrological.lower() not in acceptable_signs:
        print("That is not an acceptable sign, please try again.")
        astrological = input("> ")
    myPlayer.astrological = astrological.lower()

    # Leads the player into the puzzle now!
    speech1 = "Ah, " + myPlayer.astrological + ", how interesting.  Well then.\n"
    speech2 = "It seems this is where we must part, " + myPlayer.name + ".\n"
    speech3 = "How unfortunate.\n"
    speech4 = "Oh, you don't know where you are?  Well...\n"
    speech5 = "Luckily, I've left you at home with a little puzzle.  Hopefully you can escape this nightmare.\n"
    speech6 = "Heh. Heh.. Heh...\n"
    for character in speech1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.07)
    for character in speech2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.07)
    for character in speech3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.1)
    for character in speech4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.07)
    for character in speech5:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.07)
    for character in speech6:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.2)
    time.sleep(1)

    os.system('cls' if os.name == 'nt' else 'clear')
    print("################################")
    print("# Here begins the adventure... #")
    print("################################\n")
    ask = ("You find yourself at home \nBut it seems quiet, to quiet\n")
    for character in ask:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.08)
    print("\n")
    ask_2 = ("So you go out and investigate\n")
    for character in ask_2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.08)
    print("\n")
    ask_3 = ("You have 20 health points in the beginning.\nBe carefull with them.\n")
    for character in ask_3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.08)
    print()
    pygame.mixer.music.stop()
    main_game_loop()

title_screen()