import pickle

class Game:
    def __init__(self):
        self.Name = None
        self.Platform = None
        self.Genre = None
        self.Cost = None
        self.NoP = None
        self.Online = None


def load_games(filename):
    with open (file = filename,mode ="rb") as game_file:
        games = pickle.load(game_file)
        return games
    pass

def save_games(filename, games):
    with open (file = filename,mode ="wb") as game_file:
        pickle.dump(games,game_file)
    
    pass

def get_game_from_user(games):       
    rouge = 0
    while rouge != -1:
        game = Game()
        game.Name = input("Please enter the games name: ")
        game.Platform = input("Please enter a platform: ")
        game.Genre = input("Please enter a Genre: ")
        game.Cost = input("Please enter the cost(£): ")
        game.Nop = input("Please enter the number of players: ")
        game.Online = input("Please enter weather it has online functionality or not: ")
        games.append(game)
        rouge = int(input("Enter -1 to terminate, anything else will continue the program: "))
    return games   
    


def display_games(games):
    print("__________________________________________________________________")
    print("|Name   |Platform |Genre     |Cost |Number of players   |Online  |")
    print("------------------------------------------------------------------")
    for game in games:
        print( "|{0:7}|{1:9}|{2:10}|{3:5}|{4:20}|{5:8}|".format(game.Name,game.Platform,game.Genre,game.Cost,game.Nop,game.Online))
        print("------------------------------------------------------------------")
    pass


def display_menu():
    print()
    print("***Welcome to the Computer and Video Game Database***")
    print()
    print("1. Add new games")
    print("2. Display games")
    print("3. Exit program")
    print()

def main():
    exit_program = False
    games = []
    filename = input("Enter the filename: ")
    try:
        games = load_games(filename)
    except FileNotFoundError:
        pass
    while not exit_program:
        display_menu()
        selected_option = int(input("Please select a menu option: "))
        if selected_option == 1:
            games = get_game_from_user(games)
            
        elif selected_option == 2:
            display_games(games)
            
        elif selected_option == 3:
            save_games(filename,games)
            exit_program = True
        else:
            print("Please enter a valid option (1-3)")
            print()

if __name__ == "__main__":
    main()
