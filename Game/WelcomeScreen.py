import random
import time
import customtkinter as ctk
import Questions
from RuleScreen import RuleScreen

# Configure customtkinter appearance
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


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
        # Main container with gradient background effect
        self.welcome_frame = ctk.CTkFrame(self.root, corner_radius=20, fg_color=("#2B2B2B", "#1E1E1E"), width=900, height=650)
        self.welcome_frame.pack(pady=25, padx=50, fill="both", expand=True)
        self.welcome_frame.pack_propagate(False)
        
        # Header with logo effect
        header_frame = ctk.CTkFrame(self.welcome_frame, fg_color="transparent", height=120)
        header_frame.pack(pady=(40, 20), fill="x")
        header_frame.pack_propagate(False)
        
        welcome = "🎯 PYTHON KBC 🎯"
        subtitle = "Kaun Banega Crorepati"
        
        welcome_text = ctk.CTkLabel(header_frame, text=welcome, 
                                   font=ctk.CTkFont(family="Segoe UI", size=42, weight="bold"), 
                                   text_color="#FFD700")
        welcome_text.pack(pady=(10, 5))
        
        subtitle_text = ctk.CTkLabel(header_frame, text=subtitle, 
                                    font=ctk.CTkFont(family="Segoe UI", size=20, weight="normal"), 
                                    text_color="#CCCCCC")
        subtitle_text.pack(pady=(0, 20))
        
        # Animated welcome text
        self.root.update()
        if self.game.welcome_player:
            original_text = welcome
            welcome_text.configure(text="")
            for i in range(len(original_text) + 1):
                welcome_text.configure(text=original_text[0:i])
                self.root.update()
                time.sleep(0.1)
                
            time.sleep(0.5)
            self.game.welcome_player = False
        
        # Input section
        input_frame = ctk.CTkFrame(self.welcome_frame, fg_color="transparent", height=100)
        input_frame.pack(pady=40)
        input_frame.pack_propagate(False)
        
        name_label = ctk.CTkLabel(input_frame, text="Enter Your Name", 
                                 font=ctk.CTkFont(family="Segoe UI", size=18, weight="bold"),
                                 text_color="#FFFFFF")
        name_label.pack(pady=(0, 15))
        
        self.player_name = ctk.CTkEntry(input_frame, placeholder_text="Player Name...", 
                                       width=350, height=45, 
                                       font=ctk.CTkFont(family="Segoe UI", size=16),
                                       border_width=2, border_color="#FFD700",
                                       corner_radius=10)
        self.player_name.pack(pady=(0, 25))
        
        # Action buttons
        button_frame = ctk.CTkFrame(self.welcome_frame, fg_color="transparent")
        button_frame.pack(pady=20)
        
        go_btn = ctk.CTkButton(button_frame, text="START GAME", 
                              font=ctk.CTkFont(family="Segoe UI", size=16, weight="bold"),
                              width=200, height=45,
                              fg_color="#FF6B00", hover_color="#E55A00",
                              corner_radius=10, command=self.go_to_rules_screen)
        go_btn.pack(pady=10)
        
        # Footer
        footer_label = ctk.CTkLabel(self.welcome_frame, 
                                   text="Test your Python knowledge and win virtual millions!",
                                   font=ctk.CTkFont(family="Segoe UI", size=14),
                                   text_color="#888888")
        footer_label.pack(side="bottom", pady=20)
        
    def go_to_rules_screen(self):
        if not self.player_name.get().strip():
            self.player_name.configure(placeholder_text="Please enter your name!", placeholder_text_color="#FF6B6B")
            return
            
        self.game.player = self.player_name.get().strip()
        self.welcome_frame.destroy()
        RuleScreen(self.root, self.game)