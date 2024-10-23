import tkinter as tk

class Bullet:
    def __init__(self, canvas, x, y):
        # Load the bullet image file
        self.image = tk.PhotoImage(file='image/bullet.png')
        
        # Place the image in the canvas at the given coordinates (x,y) with northwest ('nw') anchoring
        self.bullet = canvas.create_image(x, y, image=self.image, anchor='nw')
        
        # Store a reference to the canvas so it can be used later
        self.canvas = canvas

    def move(self):
        # Move the bullet image 5 pixels to the right (positive x direction)
        self.canvas.move(self.bullet, 5, 0)
