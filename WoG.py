def welcome():
    name = input("what is your name?")
    return(f"hello {name} and  welcome to the World of Games (WoG). Here you can find many cool games to play.")
print(welcome())

def load_game():
    choosegame=input("Please choose a game to play:"
                    "1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back"
                    "2. Guess Game - guess a number and see if you chose like the computer"
                    "3. Currency Roulette - try and guess the value of a random amount of USD in ILS")
    return(choosegame)
print(load_game())
def difficulty():
    level=input("please choose difficulty from 1 to 5:")
    if level > 5 or level < 1:
        print("the number is incorrect")
    return(level)
print(difficulty())
