# -----------------####the doors ####### Function.....
def die_dragon(why):
    print(f"{why}.. ! Good Job...")
    exit(0)


def red_door():
    # Flee to return to the start of the game, in the room with the blue and red door or die!
    print(""" There is the Great Red Dragon..
              I can see it very clearly with its eyes wide open... """)
    print("""you have 2 options ..
             choose 1 to flee back..
                    2 to die...
            What will you do now...""")
    red_action = input("> ")
    if red_action == "1":
        main_game()
    elif red_action == "2":
        print("you are in the hands of the dargon")
        die_dragon("It eats you. Well, that was tasty!")


def blue_door():
    '''
        The player finds a treasure chest, options to investigate the treasure chest or guard.
        If player chooses
        - Treasure chest: show its contents; option to take treasure or ignore it (proceeds to guard)
        - Guard: nothing for now
          '''
    treasure_chest = ["gold", "silver", "diamond", "platinum"]
    treasure_contents = ", ".join(treasure_chest)
    print("""please enter your choice :
                > 1 to take treasure
                > 2 to move to guard """)
    action = input("> ")
    if action == "1":
        print(f"you have {treasure_contents} ")
        print("""Please enter your choice :
                    >1 to take all
                    >2 to leave all
                    >3 to take any one form them""")
        choice = input("> ")
        treasure_chest_len = len(treasure_chest)
        if choice == "1":
            # treasure_chest_len = len(treasure_chest)
            print(f"you have {treasure_chest_len} iteams in chest, you want to take all ??")
            print("to confirm press 1, to abort press 0")
            confirm_choice = input("> ")
            if confirm_choice == "1":
                temp_treasure_list = treasure_chest[:]
                treasure_contents = ", ".join(treasure_chest)
                print("you tooooooook all, there is nothing left in the treasure..")
                print(f"You received {treasure_contents}.")
                for treasure in treasure_chest:
                    temp_treasure_list.remove(treasure)
            elif confirm_choice == "0":
                print("you left all...you may not get it later...")
        elif choice == "2":
            print(f"you have {treasure_chest_len} iteams in chest, that is waiting for you here ...")
        elif choice == "3":
            print(f"you have {treasure_chest_len} iteam's in chest")
            print(treasure_contents)
            pickup = input("which one do you want to take >")
            if pickup not in treasure_chest:
                while pickup not in ["gold", "silver", "diamond", "platinum"]:
                    print("enter the proper input...")
                    pickup = input(">")
            if pickup in treasure_chest:
                print(f"{pickup} picked up...")
                treasure_chest.remove(pickup)
                treasure_chest_len = len(treasure_chest)
                print(f"you have {treasure_chest_len} iteam's left still..")
    elif action == "2":
        print("Guard is more intresting lets go that way....")
    else:
        print("Well, not sure what you picked there, let's poke the guard cos it's fun!")
# -------------------------------------Main


def main_game():
    print("After entering the main hall you have 2 doors, you can pick any one amoung them...")
    door_picked = input("Please pick either of the doors, red or blue : ")
    if door_picked == "red":
        red_door()
    elif door_picked == "blue":
        blue_door()
    else:
        print("You didn't choose properly, Please enter either blue or red..")

# -------------------------------------Main Function------------------------------


def main():
    player_name = input("Please enter your name : ")
    print(f"your name is: {player_name.upper()}")
    main_game()


# ------------------------------------- Calling - Main Function------------------------------


if __name__ == '__main__':
    main()