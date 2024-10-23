class Startingpage:
    def __init__(self):
        import tkinter as tk
        from random import choice

        # Initialize tkinter window
        self.window = tk.Tk()
        
        # Set initial game level to 1
        self.level = 1

        # Load or create the save data for level 1
        while True:
            try:
                with open('savedata1.txt', 'r+') as file:
                    scoreplayer_lv1=file.readline()
                    break
            except FileNotFoundError:
                file=open('savedata1.txt', 'w+')
                file.write('000')
                scoreplayer_lv1=file.readline
                file.close()

        # Repeat for levels 2 and 3
        while True:
            try:
                with open('savedata2.txt', 'r+') as file:
                    scoreplayer_lv2=file.readline()
                    break
            except FileNotFoundError:
                file=open('savedata2.txt', 'w+')
                file.write('000')
                scoreplayer_lv2=file.readline
                file.close()

        while True:
            try:
                with open('savedata3.txt', 'r+') as file:
                    scoreplayer_lv3=file.readline()
                    break
            except FileNotFoundError:
                file=open('savedata3.txt', 'w+')
                file.write('000')
                scoreplayer_lv3=file.readline
                file.close()
 
        # Set the title of the window
        self.window.title('shooting game')

        # Function to print the game rules when the help button is clicked
     
        def help_button():
            try:
                with open('rule.txt', 'r') as file:
                    rules = file.read()
                    print(rules)
            except FileNotFoundError:
                print("Rules file not found. Please make sure 'rule.txt' is in the correct location.")

        # Function to change the color of the label every 500 milliseconds
        def change_color():
            colors=['red','blue','black','green','orange']
            label1.configure(bg=choice(colors))
            self.window.after(500,change_color)

        
        # Create and grid all the labels and buttons for the starting page
        label1= tk.Label(self.window, text='SHOOTING GAME', width=20
                         , height=5, bg='red', fg='white', font='Times 30')
        label1.grid(row=0, column=0, columnspan=2)
        self.window.after(500,change_color)

        label2=tk.Label(self.window,
                        text='Score List\n level1: \n level2:\n level3:',
                        width=10, height=5,font='Times 20')
        label2.grid(row=0, column=2)

        label3=tk.Label(self.window,
                        text=' \n'+scoreplayer_lv1+'\n'+scoreplayer_lv2+'\n'+scoreplayer_lv3,
                        font='Times 20')
        label3.grid(row=0, column=3)

        button1=tk.Button(self.window, text='LEVEL 1', width=15, height=5, command=self.level1)
        button1.grid(row=1,column=0,columnspan=2)
        
        button2=tk.Button(self.window, text='LEVEL 2', width=15, height=5, command=self.level2)
        button2.grid(row=2,column=0,columnspan=2)

        button3=tk.Button(self.window, text='LEVEL 3', width=15, height=5,command=self.level3)
        button3.grid(row=3,column=0,columnspan=2)

        button4=tk.Button(self.window, text='help', width=15, height=5, command=help_button)
        button4.grid(row=4,column=0,columnspan=2)

        # Run the tkinter main loop
        self.window.mainloop()

    # Functions to set the level and close the window when a level button is clicked
    def level1(self):
        print('level1')
        self.level = 1
        self.window.destroy()

    def level2(self):
        print('level2')
        self.level = 2
        self.window.destroy()

    def level3(self):
        print('level3')
        self.level = 3
        self.window.destroy()



