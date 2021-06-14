import time
import random
import turtle
import lists


def print_pause(message):
    print(message)
    time.sleep(1)


# This is the intro
def intro(name):
    print_pause(f"Once, long ago, in a post-apocalyptic wasteland there "
                f"was a {random.choice(lists.character)} that went "
                f"by the name of {name}")
    print_pause(f"{name} loved exploring the wasteland, trying to "
                f"find loot and gaining new skills in this "
                f"dangerous post-apocalyptic world.")


# The first path option
def first_path(name):
    print_pause("The dark and dangerous road leads to a magical chest.")
    while True:
        chance = input("would you like to open the magical "
                       "chest? (yes/no)\n").lower()
        if "yes" in chance:
            print_pause(f"{name} opens the chest and "
                        f"finds a {random.choice(lists.weapon)}.")
            break
        elif "no" in chance:
            print_pause(f"{name} continues on his/her journey.")
            break
        else:
            print_pause("Please type yes or no.")


# The second path option
def second_path(name):
    print_pause(f"While trying to cross the river, "
                f"{name} falls into the water.")
    print_pause(f"Oh no!!! It appears that the water is infested "
                f"with blood-thursty, flesh-eating paranas.")
    print_pause(f"They eat {name}!")
    print_pause(f"Game over!!!")
    print_pause("You lose.")


# The third path option
def third_path(name):
    print_pause(f"{name} follows the flight of stairs all the way to "
                f"the top and crosses the bridge with no trouble at all.")
    print_pause(f"{name} continues walking when he/she hears a growl. "
                f"Scared, {name} pulls out a small pocket knife.")
    print_pause(f"The growling noise gets loader and loader as this animal "
                f"gets closer, and {name} prepares himself/herself "
                f"to go into battle.")
    print_pause(f"Then just as {name} was about to charge whatever was "
                f"lurking behind the bushes, a friendly dog emerged.")
    print_pause("You just made a companion.")


# The first boss fight:
def boss_fight_1(name):
    print_pause(f"While {name} explores, he/she stumble across a "
                f"{random.choice(lists.villains)} that goes "
                f"by the name of Goliath.")
    print_pause(f"Goliath walks up to {name} and then suddenly "
                f"pulls out a {random.choice(lists.weapon)}:")
    print_pause(f"What should {name} do?")
    fight = input("Select 1 to fight Goliath.\n"
                  "Select 2 to run away.\n"
                  "Select 3 to beg for mercy.\n")
    while True:
        if fight == "1":
            print_pause(f"{name} charges Goliath as they battle it out.")
            print_pause(f"{name} defeats Goliath!!!")
            print_pause("You've beaten the game.")
            print_pause("You win.")
            you_win()
            break
        elif fight == "2":
            print_pause(f"{name} starts running, but as it turns out "
                        f"Goliath is an expert sprinter and catches "
                        f"up to you quiet easilly.")
            print_pause(f"Goliath cathes {name} and murders him/her.")
            print_pause("Game over.")
            print_pause("You lose.")
            you_lose()
            break
        elif fight == "3":
            print_pause(f"{name} begs Goliath for mercy and Goliath pulls "
                        f"out a dice and makes {name} a silly offer.")
            print_pause(f"He says that if {name} rolls a higher number "
                        f"than he does, he/she is free to leave...")
            print_pause("But if he doesn't, Goliath is going to kill him.")
            print_pause(f"{name} rolls first and rolls a:")
            dice1 = random.randint(1, 6)
            print_pause(dice1)
            print_pause("Goliath is next to roll and rolls a:")
            dice2 = random.randint(1, 6)
            print_pause(dice2)
            while True:
                if dice1 > dice2:
                    print_pause("Yes!!! You win.")
                    you_win()
                    break
                elif dice1 < dice2:
                    print_pause("Goliath wins.")
                    print_pause("Game over.")
                    you_lose()
                    break
                else:
                    print_pause("It's a tie. They roll again.")
        else:
            print_pause("Please enter 1, 2 or 3")
            boss_fight_1(name)
        break


# The second boss fight:
def boss_fight_2(name):
    companion = input("What would you like to name your companion?\n")
    print_pause(f"And so, {name} and {companion} continue their journey")
    print_pause(f"As {name} and {companion} continue their journey,"
                f"they cross paths with a "
                f"{random.choice(lists.villains)}, named Jake Paul")
    print_pause(f"Jake charges {name} and {companion}. What should they do?")
    print_pause(f"Should {name} and {companion}:")
    choices_2 = input("Run away from Jake. (Press 1)\n"
                      "Stay and fight it out. (Press 2)\n")
    while True:
        if choices_2 == "1":
            print_pause(f"{name} and {companion} run away from Jake.")
            print_pause("Unfortunatelly Jake is really fast and "
                        "cathes up to them and kill them.")
            print_pause("You lose!")
            you_lose()
            break
        elif choices_2 == "2":
            print_pause(f"{name} and {companion} battle it out against Jake.")
            print_pause(f"Jake is outnumberd 2 to 1 and {name} "
                        f"and {companion} manage to defeat him!")
            print_pause("You win!")
            you_win()
            break
        else:
            print_pause("Please type 1 or 2.")
            boss_fight_2(name)
        break


# All paths
def paths(name):
    print_pause(f"While exploring the wasteland, {name} comes across "
                f"a path that lead to three directions:")
    print_pause("1. A dark and dangerous looking road, with a "
                "bunch of \"No entrance\" signs.\n"
                "2. A road that leads to a river.\n"
                "3. A flight of stairs that lead to a hanging-brigde.")
    print_pause(f"Which path should {name} take?")
    choice = input("Please select an option: (choose a number 1,2 or 3.)\n")
    if choice == "1":
        first_path(name)
        boss_fight_1(name)
        play_again()
    elif choice == "2":
        second_path(name)
        you_lose()
        play_again()
    elif choice == "3":
        third_path(name)
        boss_fight_2(name)
        play_again()
    else:
        print_pause("Please enter 1, 2 or 3.")
        paths(name)


# The type of turtle:
def tur(t_name, color):
    t_name.color(color)
    t_name.speed(0)
    t_name.width(5)
    t_name.hideturtle()


# How the turtle moves
def move(t_name, angle, forward, angle2):
    t_name.penup()
    t_name.right(angle)
    t_name.forward(forward)
    t_name.left(angle2)
    t_name.pendown()


# Drawing the turtle
def draw_shape(t_name, area, direction, angle):
    for n in range(area):
        t_name.forward(direction)
        t_name.left(angle)


# If the user wins
def you_win():
    win = turtle.Turtle()
    tur(win, "green")

    move(win, 90, 100, 90)
# Draw face
    draw_shape(win, 99, 10, 4)
    move(win, -120, 150, 180)
# Draw mouth
    draw_shape(win, 12, 10, 5)
    move(win, -100, 150, 0)
    win.width(4)
# Draw left eye
    draw_shape(win, 80, 2, 5)
    move(win, 175, 120, 0)
# Draw right eye
    draw_shape(win, 80, 2, -5)


# If the user loses
def you_lose():
    lose = turtle.Turtle()
    tur(lose, "red")

    move(lose, 90, 100, 90)
# Draw face
    draw_shape(lose, 99, 10, 4)
    move(lose, -120, 150, -130)
# Draw mouth
    draw_shape(lose, 12, 10, -5)
    move(lose, -170, 150, 0)
    lose.width(4)
# Draw left eye
    draw_shape(lose, 80, 2, 5)
    move(lose, 175, 120, 0)
# Draw right eye
    draw_shape(lose, 80, 2, -5)
    time.sleep(1)


# function to play again
def play_again():
    while True:
        print_pause("Would you like to play again?")
        again = input("Select 1 to play again.\n"
                      "select 2 to quit.\n")
        if again == "1":
            print_pause("Okay, your next game will be starting shortly!")
            play_game()
        elif again == "2":
            print_pause("Okay, thanks for playing.\n"
                        "Goodbye!")
            break
        else:
            print_pause("Select '1' or '2' please:")
        break


# This calls all functions together to play the game
def play_game():
    name = input("Please enter your character name:\n")
    intro(name)
    paths(name)


play_game()
