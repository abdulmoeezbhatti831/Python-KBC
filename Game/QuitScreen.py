import customtkinter as ctk
import time

# Configure customtkinter appearance
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


# ------------------ QUIT SCREEN SETTINGS ------------------
class QuitScreen:
    def __init__(self, root, game, text, wrong_reply_and_timer_over, self_quit):
        self.root = root
        self.game = game
        self.quit_screen(text, wrong_reply_and_timer_over, self_quit)
        
    def quit_screen(self, text, wrong_reply_and_timer_over, self_quit):
        self.quit_frame = ctk.CTkFrame(self.root, corner_radius=20, fg_color=("#2B2B2B", "#1E1E1E"), width=900, height=650)
        self.quit_frame.pack(pady=25, padx=50, fill="both", expand=True)
        self.quit_frame.pack_propagate(False)
        
        # Result display
        result_content = ctk.CTkFrame(self.quit_frame, fg_color="transparent")
        result_content.pack(expand=True, fill="both", pady=80)
            
        if self.game.level_no > 1:
            # Animated ending text
            ending = text
            ending_text = ctk.CTkLabel(result_content, text="", 
                                      font=ctk.CTkFont(family="Segoe UI", size=36, weight="bold"),
                                      text_color="#FFD700")
            ending_text.pack(pady=(40, 20))
            
            # Animate text appearance
            for i in range(len(ending) + 1):
                ending_text.configure(text=ending[0:i+1])
                self.root.update()
                time.sleep(0.1)
            time.sleep(0.5)
            
            # Determine prize money
            if wrong_reply_and_timer_over:
                money = self.game.won_money
            else:  # self_quit
                money = self.game.quit_money
                
            # Prize display
            prize_label = ctk.CTkLabel(result_content, 
                                      text=f"🎉 {self.game.player}, you won Rs.{money}! 🎉",
                                      font=ctk.CTkFont(family="Segoe UI", size=24, weight="bold"),
                                      text_color="#4CAF50")
            prize_label.pack(pady=20)
            
            # Performance message
            performance_msg = self.get_performance_message(self.game.level_no)
            performance_label = ctk.CTkLabel(result_content, text=performance_msg,
                                           font=ctk.CTkFont(family="Segoe UI", size=16),
                                           text_color="#CCCCCC")
            performance_label.pack(pady=10)
        else:
            # Game ended at level 1
            ctk.CTkLabel(result_content, text="Game Over", 
                        font=ctk.CTkFont(family="Segoe UI", size=36, weight="bold"),
                        text_color="#F44336").pack(pady=(40, 20))
            
            ctk.CTkLabel(result_content, text="Better luck next time!",
                        font=ctk.CTkFont(family="Segoe UI", size=18),
                        text_color="#CCCCCC").pack(pady=10)

        # Action buttons
        action_frame = ctk.CTkFrame(self.quit_frame, fg_color="transparent")
        action_frame.pack(side="bottom", pady=40)
        
        play_again_btn = ctk.CTkButton(action_frame, text="🔄 Play Again", 
                                      font=ctk.CTkFont(family="Segoe UI", size=16, weight="bold"),
                                      width=180, height=45,
                                      fg_color="#4CAF50", hover_color="#45A049",
                                      corner_radius=10, command=self.play_again)
        play_again_btn.grid(row=0, column=0, padx=20)
        
        exit_btn = ctk.CTkButton(action_frame, text="🚪 Exit", 
                                font=ctk.CTkFont(family="Segoe UI", size=16, weight="bold"),
                                width=120, height=45,
                                fg_color="#6C757D", hover_color="#5A6268",
                                corner_radius=10, command=self.root.destroy)
        exit_btn.grid(row=0, column=1, padx=20)
        
    def get_performance_message(self, level):
        if level >= 16:
            return "🏆 Outstanding! You're a Python expert!"
        elif level >= 11:
            return "🎯 Excellent performance! Great Python skills!"
        elif level >= 6:
            return "👍 Good job! You know your Python well!"
        else:
            return "💪 Nice try! Keep learning Python!"
        
    def play_again(self):
        from WelcomeScreen import WelcomeScreen
        self.quit_frame.destroy()
        WelcomeScreen(self.root, self.game, True)