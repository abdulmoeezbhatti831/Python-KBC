import customtkinter as ctk
import time


# ------------------ QUITING SCREEN SETTINGS ------------------
class QuitScreen:
    def __init__(self, root, game, text, wrong_reply_and_timer_over, self_quit):
        self.root = root
        self.game = game
        
        self.quit_screen(text, wrong_reply_and_timer_over, self_quit)
        
    def quit_screen(self, text, wrong_reply_and_timer_over, self_quit):
        self.quit_frame = ctk.CTkFrame(self.root, corner_radius=5, width=700, height=400)
        self.quit_frame.pack(pady=(50, 0))
        self.quit_frame.pack_propagate(False)
            
        if not self.game.level_no == 1:
            ending = text
            ending_text = ctk.CTkLabel(self.quit_frame, text="", font=ctk.CTkFont(family="Times New Roman", size=40, weight="bold", slant="italic"), text_color="#328FB4", wraplength=600)
            ending_text.pack(pady=70)
            self.root.update()
            
            for i in range(len(ending) + 1):
                ending_text.configure(text=ending[0:i+1])
                self.root.update()
                time.sleep(0.2)
            time.sleep(1)
            
            if wrong_reply_and_timer_over:
                money = self.game.won_money
            if self_quit:
                money = self.game.quit_money
                
            ctk.CTkLabel(self.quit_frame, text=f"{self.game.player}, you are taking 💸Rs.{money} with you!", font=ctk.CTkFont(family="Helvetica", size=18)).pack()

        quit_frame_footer = ctk.CTkFrame(self.quit_frame)
        quit_frame_footer.pack(pady=(50, 0))
        
        ctk.CTkButton(quit_frame_footer, text=" Play Again ", command=self.play_again).grid(row=0, column=0, padx=8)
        ctk.CTkButton(quit_frame_footer, text=" Exit ", command=self.root.destroy).grid(row=0, column=1, padx=8)
        
    def play_again(self):
        from Welcome import WelcomeScreen
        self.quit_frame.destroy()
        WelcomeScreen(self.root, self.game, True)