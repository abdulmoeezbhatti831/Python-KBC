import random
import time
import customtkinter as ctk
import Questions
from Rules import RuleScreen


# ------------- WELCOME SCREEN SETTINGS -------------       
class WelcomeScreen:
    def __init__(self, root, game, play_again):
        self.root = root
        self.game = game
        
        if play_again:
            # ------------- RESTARTING THE WHOLE GAME IF PLAY AGAIN IS 'TRUE' --------------------
            self.game.questions = Questions.questions.copy()
            random.shuffle(self.game.questions)
            self.game.Comments = Questions.Comments.copy()
            random.shuffle(self.game.Comments)
            self.game.levels = Questions.levels.copy()
            
            self.game.question_generator = self.game.call_question()
            self.game.player = None 
            self.game.won_money = "0"
            self.game.quit_money = "0"
            self.game.prize_money = "0"
            self.game.level_no = 1
            
            self.game.use_50_50 = True
            self.game.use_flip = True
            
        self.welcome_screen()
        
    def welcome_screen(self):
        self.welcome_frame = ctk.CTkFrame(self.root, corner_radius=5, width=700, height=600)
        self.welcome_frame.pack(pady=50)
        self.welcome_frame.pack_propagate(False)
        
        welcome = "✨ WELCOME TO THE PYTHON KBC GAME ✨"
        
        welcome_text = ctk.CTkLabel(self.welcome_frame, text=welcome, font=ctk.CTkFont(family="Times New Roman", size=40, weight="bold", slant="italic"), text_color="#328FB4", wraplength=600)
        welcome_text.pack(pady=70) 
        self.root.update()
        
        if self.game.welcome_player:
            for i in range(len(welcome) + 1):
                welcome_text.configure(text=welcome[0:i+1])
                self.root.update()
                time.sleep(0.2)
                
            time.sleep(1)
            self.game.welcome_player = False
            
        self.player_name = ctk.CTkEntry(self.welcome_frame, placeholder_text="Player Name...", width=300, height=35, border_width=1, border_color="light blue")
        self.player_name.pack(pady=(0, 20))
        
        ctk.CTkButton(self.welcome_frame, text=" GO! ", font=ctk.CTkFont(family="Segeo UI", size=17, weight="bold", slant="italic"), command=self.go_to_rules_screen).pack()
        
    def go_to_rules_screen(self):
        if self.player_name.get() == "":
            self.player_name.configure(placeholder_text="Enter your name!")
        else:
            self.player_name.configure(placeholder_text_color="blue")
            self.game.player = self.player_name.get()
            self.welcome_frame.destroy()
            RuleScreen(self.root, self.game)