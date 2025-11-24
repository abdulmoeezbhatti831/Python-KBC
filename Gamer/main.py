import customtkinter as ctk
import random
import Questions
from Welcome import WelcomeScreen


class PythonKBC:
    def __init__(self, root):
        # ----------- ROOT SETTINGS ---------------
        self.root = root
        self.root.geometry("800x500")
        self.root.title("Python KBC (Kaun Banega Crorepati)")
        self.root.resizable(False, False)
        
        # ----------- GAME VARIABLES -------------
        self.questions = Questions.questions.copy()
        random.shuffle(self.questions)
        self.Comments = Questions.Comments.copy()
        random.shuffle(self.Comments)
        self.levels = Questions.levels.copy()
        
        self.question_generator = self.call_question()
        self.player = None 
        self.won_money = "0"
        self.quit_money = "0"
        self.prize_money = "0"
        self.level_no = 1
        
        self.use_50_50 = True
        self.use_flip = True
        
        # ----------- ENABLING FRAMES --------------
        self.welcome_player = True 
        WelcomeScreen(self.root, self, False)
        
    # -------------- RUN THE GAME ----------------
    def run(self):
        self.root.mainloop()
        
    # ------------------ GAME SCREEN SETTINGS >> CALL THE QUESTION ---------------------------- 
    def call_question(self):
        for i in range(len(self.levels) + 1):
            yield self.questions[i], self.levels[i], [random.choice(self.Comments), random.choice(self.Comments)]
            
if __name__ == "__main__":
    Game = PythonKBC(ctk.CTk())
    Game.run()