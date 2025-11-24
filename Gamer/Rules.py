import customtkinter as ctk
import Questions
from Game import GameScreen


# ----------- RULES SCREEN SETTINGS -----------------
class RuleScreen:
    def __init__(self, root, game):
        self.root = root
        self.game = game
        
        self.rules_screen()
            
    def rules_screen(self):
        self.rules_frame = ctk.CTkFrame(self.root, corner_radius=5, width=700, height=400)
        self.rules_frame.pack(pady=(50, 0))
        self.rules_frame.pack_propagate(False)
        
        ctk.CTkLabel(self.rules_frame, text="RULES", font=ctk.CTkFont(family="Times New Roman", size=35, weight="bold", slant="italic"), text_color="white", wraplength=600).pack(pady=(40, 20))
        
        RULES = Questions.RULES
        
        rulebox = ctk.CTkTextbox(self.rules_frame, width=600, height=220, font=("Helvetica", 17), corner_radius=10, border_width=1, border_color="sky blue")
        rulebox.pack()
        rulebox.pack_propagate(False)
        rulebox.insert(0.0, RULES)
        rulebox.configure(state="disabled")
        
        btn_frame = ctk.CTkFrame(self.rules_frame)
        btn_frame.pack(pady=(20, 0))
        
        ctk.CTkButton(btn_frame, text=" Back ", command=self.back_to_welcome_screen).grid(row=0, column=0, padx=8)
        ctk.CTkButton(btn_frame, text=" Start Game ", command=self.go_to_game_screen).grid(row=0, column=1, padx=8)
        
    def back_to_welcome_screen(self):
        from Welcome import WelcomeScreen
        self.rules_frame.destroy()
        WelcomeScreen(self.root, self.game, False)

    def go_to_game_screen(self):
        self.rules_frame.destroy()
        GameScreen(self.root, self.game)