import tkinter as tk
from tkinter import messagebox
import time
from player import Player
from bullet import Bullet
from target import Target
from background import Background
from sound import Sound
import random

class Game:
    def __init__(self, root, level):
        # Set up game window and canvas
        self.root = root
        self.canvas = tk.Canvas(root, width=500, height=400)
        self.canvas.pack()

        # Initialize game elements
        self.background = Background(self.canvas)
        self.player = Player(self.canvas, 50, 200)
        self.targets = []
        self.bullets = []
        self.time_start = time.time()

        # Initialize a counter
        self.count = 0

        # Initialize sound elements
        self.sound0 = Sound('music/bgm.mp3', -1)
        self.sound1 = Sound('music/target.wav', 0)
        self.sound2 = Sound('music/player.wav', 0)

        # Bind keyboard inputs to their respective actions
        self.root.bind("<Up>", self.move_up)
        self.root.bind("<Down>", self.move_down)
        self.root.bind("<space>", self.fire)

        # Start background music
        self.bgm()

        # Start game loop
        self.game_loop(level)

    def move_up(self, event):
        # Handle the "move up" event
        self.player.move(-20)

    def move_down(self, event):
        # Handle the "move down" event
        self.player.move(20)

    def fire(self, event):
        # Handle the "fire" event
        x1, y1  = self.canvas.coords(self.player.player)
        self.bullets.append(Bullet(self.canvas, x1+25, y1+10))
        self.sound2.play_sound()

    def bgm(self):
        # Play background music
        self.sound0.play_sound()

    def game_loop(self, level):
        # Handle bullet motion, remove if out of canvas
        for bullet in self.bullets.copy():
            bullet.move()
            if self.canvas.coords(bullet.bullet)[0] > 500:
                self.canvas.delete(bullet.bullet)
                self.bullets.remove(bullet)

        # Handle target motion, end game if target reaches left edge of canvas
        for target in self.targets.copy():
            if self.canvas.coords(target.target)[0] > 0:
                target.move()
            else:
                # If target reaches the left edge, calculate time score and save to file
                time_end = time.time()
                time_c = round(time_end-self.time_start,3)
                t = str(time_c)

                if level == 1:
                    with open ('savedata1.txt','a+') as file:
                        if file.tell()==0:
                            file.write(t)
                        else:
                            file.write(","+t)
                    messagebox.showinfo('GAME OVER','Your score is '+t)
                    self.root.destroy()

                elif level == 2:
                    with open ('savedata2.txt','a+') as file:
                        if file.tell()==0:
                            file.write(t)
                        else:
                            file.write(","+t)
                    messagebox.showinfo('GAME OVER','Your score is '+t)
                    self.root.destroy()

                elif level == 3:
                    with open ('savedata3.txt','a+') as file:
                        if file.tell()==0:
                            file.write(t)
                        else:
                            file.write(","+t)
                    messagebox.showinfo('GAME OVER','Your score is '+t)
                    self.root.destroy()

        # Check for collisions between bullets and targets
        for bullet in self.bullets.copy():
            for target in self.targets.copy():
                try:
                    # If a bullet hits a target, destroy both and play a sound
                    if abs(self.canvas.coords(bullet.bullet)[0] - self.canvas.coords(target.target)[0]) < 20 and abs(self.canvas.coords(bullet.bullet)[1] - self.canvas.coords(target.target)[1] -10) < 15:
                        self.sound1.play_sound()
                        self.canvas.delete(bullet.bullet)
                        self.bullets.remove(bullet)
                        self.canvas.delete(target.target)
                        self.targets.remove(target)

                except IndexError:
                    pass

        # Increment the counter and create new targets at certain intervals
        self.count +=1
        if self.count == 40 - level*10:
            self.targets.append(Target(self.canvas, 450, random.randint(50, 350), level))
            self.count =0

        # Repeat the game loop every 100 milliseconds
        self.root.after(100, self.game_loop, level)
