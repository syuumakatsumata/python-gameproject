import tkinter as tk

class Background:
    def __init__(self, canvas):
        # Load the background image file
        self.image = tk.PhotoImage(file="image/bg.png")
        
        # Place the image in the canvas at the top left corner (coordinates (0,0)) with northwest ('nw') anchoring
        self.background = canvas.create_image(0, 0, image=self.image, anchor='nw')
        
        # Store a reference to the canvas so it can be used later
        self.canvas = canvas
