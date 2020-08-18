# Wander wander
from time import sleep
from datetime import time

def door():
    print("you are at the door")
    sleep(1)
    action = input("what do you want to do? \n> ")
    if action == "turn knob" or "open door":
        print("You've opened the door.")
    return True

def wake_up():
    print("You wake up.")
    print("You're feeling a little groggy.")
    print("You sit up.")

    
    # action: will be the placeholder variable to control user choices
  
    action = input("What should you do next? \n> ").lower()

    if action == "get up" or "stand up":
        print("you stand up")
        print("you look around and see a door, computer, and bureau.")
        sleep(1)
        action = input("What do you choose? \n> ")
    elif action == "look around":
        print("you look around and see a door, computer, and bureau.")
        sleep(1)
        action = input("What do you choose? \n> ")
    else:
        print("You kinda get tired of just sitting there looking stupid.")
        print("you look around and see a door, computer, and bureau.")
        sleep(1)
        action = input("What do you choose? \n> ")

    if action == "door":
        door()

wake_up()





# if action == "leave room" or "leave the room":
    # print("you left the room")
