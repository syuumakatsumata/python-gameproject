import tkinter as tk
from game import Game
from startingpage import Startingpage

def main():

    # Initialize the Startingpage object. This object handles the starting menu of the game.
    page = Startingpage()

    # Get the level from the start page
    level = page.level

    # Initialize the main window
    root = tk.Tk()
    
    # Initialize the Game object. The Game object handles the gameplay.
    game = Game(root,level)

    # Start the tkinter event loop
    root.mainloop()

# If this script is run directly (as opposed to being imported), then start the main function.
if __name__ == "__main__":
    main() 