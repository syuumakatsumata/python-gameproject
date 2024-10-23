import tkinter as tk

class Player:
    def __init__(self, canvas, x, y):
        # Load the player image file
        self.image = tk.PhotoImage(file='image/player.png')
        
        # Place the image in the canvas at the given coordinates (x,y) with northwest ('nw') anchoring
        self.player = canvas.create_image(x, y, image=self.image, anchor='nw')
        
        # Store a reference to the canvas so it can be used later
        self.canvas = canvas

    def move(self, dy):
        # Move the player image in the vertical direction by dy pixels (positive values move down, negative values move up)
        self.canvas.move(self.player, 0, dy)
