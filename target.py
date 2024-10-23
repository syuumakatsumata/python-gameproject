import tkinter as tk
import random

class Target:
    def __init__(self, canvas, x, y, level):
        # Depending on the remainder of y divided by 5, a different target image is selected
        if y % 5 == 0:
            self.image = tk.PhotoImage(file='image/target1.png')  
        elif y % 5 == 1:
            self.image = tk.PhotoImage(file='image/target2.png')
        elif y % 5 == 2:
            self.image = tk.PhotoImage(file='image/target3.png')
        elif y % 5 == 3:
            self.image = tk.PhotoImage(file='image/target4.png')
        elif y % 5 == 4:
            self.image = tk.PhotoImage(file='image/target5.png')

        # Create target image at position (x, y)
        self.target = canvas.create_image(x, y, image=self.image, anchor='nw')

        # Store canvas and level variables
        self.canvas = canvas
        self.level = level
        
    def move(self):
        # Move target to the left by level*2+1 units
        self.canvas.move(self.target, -self.level*2 -1, 0)