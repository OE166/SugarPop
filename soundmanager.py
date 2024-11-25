#############################################################
# Module Name: Sound Manager
# Project: Sugar Pop Program
# Date: Nov 17, 2024
# By: Owen Hofman
# Description: The sound manager for Sugar Pop game.
#############################################################
import pygame as pg

class soundmanager:
    def __init__(self):
        pg.mixer.init()
        #make dictionary
        self.sounds = {
            "exploding_bucket" : pg.mixer.Sound("sounds/casino_notification.wav"),
            "add_sugar" : pg.mixer.Sound("sounds/ball_tap.wav"),
            "completion" : pg.mixer.Sound("sounds/casino_achievment.wav"),
            "loading" : pg.mixer.Sound("sounds/loading.wav")
        }
        
    
    def play_sound(self, event):
        pg.mixer.Sound.play(self.sounds[event])


