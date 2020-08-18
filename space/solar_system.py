from time import sleep
from planets import *

# Planets ---> planets.py

####### Definitions #######

solar_system = [
    "Earth",
    "Mercury",
    "Venus",
    "Mars",
    "Jupiter",
    "Saturn",
    "Uranus",
    "Neptune",
    "Pluto",
    "Sun",
]

# Rocket & Launch Pad Properties
def rocket():
    print(
        """
    You're in the cock-pit of a rocket.
    It's a lot to take in.
    """
    )
    # While you're on the "launch_pad", the program will loop until the user types "blast off"-like keywords
    # The loop also has an option for you to open up a map()
    launch_pad = True
    while launch_pad:
        player_choice = input("What would you like to do? ").lower()
        # This will launch rocket --> planet_of_choice
        if player_choice in ("take off", "ignition", "blast off"):
            print("boom lift-off")
            launch_pad = False
        # Map Check
        elif player_choice == "check map":
            map()
        # Unintelligible response by user
        else:
            print("I'm not sure what to do, try again.")


def brew_coffee():
    print("Ah... a nice cup of Joe.")
    print("We're got an Ethopia, Colombia, and West Java")
    coffee_choice = input("Which beans should we choose today")
    print(f"Nice the {coffee_choice}, good choice")
    sleep(1)
    print("Brewing . . .")
    sleep(1)
    print("Ah nice, smell those juicy notes.")


# Map of the Solar System
def planet_map():
    planet_sys_dict = {
        "Earth": earth,
        "Mercury": mercury,
        "Venus": venus,
        "Mars": mars,
        "Jupiter": jupiter,
        "Saturn": saturn,
        "Uranus": uranus,
        "Neptune": neptune,
        "Pluto": pluto,
        "Sun": sun,
    }

    player_choice = input("Would you like me to list the planets for you? ").lower()

    if player_choice == "yes":
        print(", ".join(solar_system).title())  # displays list w/o [, ,]

    destination = input("Choose your destination: ").title()

    # Find the chosen destination in the planetary list then call it ()
    for planet in solar_system:
        if planet == destination:
            planet_sys_dict[str(planet)]()


# Welcome Message ~~~~ PROGRAM START ~~~~
print(":::Welcome to Solar System:::\n")
print(
    """You get up, grab your helmet off the table and look to the chamber window.
A beautiful clear sky today. It's crazy that only 5 years ago you were pushing games at GameStop.
Now I look in the mirror and see a five star michellin astronaut.
There's a bunch of items in the room...
Which do I choose?
"""
)
inventory = []
player_choice = input("> ").lower()
if player_choice == "map":
    map()
elif player_choice in ["gun", "weapon", "rifle"]:
    inventory.append(player_choice)
elif player_choice == "coffee":
    brew_coffee()

#
#
#
#
# CHECK BACK AFTER LEARNING HOW TO PASS INFO FROM BACKEND TO FRONT #

# def map_v2():
# map
# @ map launch map.html
# let user pick which planet
# whatever planet they choose, pass choice back to python
# use planet function
# Going to need AJAX/DJANGO + flask to pass variables
# from Javascript to python or something

