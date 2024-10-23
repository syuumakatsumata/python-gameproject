import pygame

class Sound:
    def __init__(self, sound_file, loop):
        # Initialize the Pygame mixer
        pygame.mixer.init()

        # Set the volume for the music channel
        pygame.mixer.music.set_volume(0.05)

        # Load a sound file
        # If loop is -1, it is background music and will be loaded into the music channel
        if loop == -1:  
            pygame.mixer.music.load(sound_file)
            self.sound_effect = None
        else:  # Otherwise, it is a sound effect and will be loaded into a Sound object
            self.sound_effect = pygame.mixer.Sound(sound_file)
            self.sound_effect.set_volume(0.05)
    
    def play_sound(self):
        # Play the sound
        # If sound_effect is not None, it means this is a sound effect
        if self.sound_effect is not None: 
            self.sound_effect.play()
        else:  # Otherwise, it is background music and will be played on loop
            pygame.mixer.music.play(-1)
