import customtkinter as ctk
import tkinter.messagebox as msgbox
import textwrap
import time
from QuitScreen import QuitScreen

# Configure customtkinter appearance
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


# ------------- GAME SCREEN SETTINGS ---------------
class GameScreen:
    def __init__(self, root, game):
        self.root = root
        self.game = game
        self.timer_job = None
        self.game_screen()
        
    def game_screen(self):
        self.game_frame = ctk.CTkFrame(self.root, corner_radius=20, fg_color=("#2B2B2B", "#1E1E1E"), width=950, height=650)
        self.game_frame.pack(pady=25, padx=25, fill="both", expand=True)
        self.game_frame.pack_propagate(False)

        # --------------- HEADER SETTINGS -------------------
        self.header = ctk.CTkFrame(self.game_frame, height=70, fg_color=("#3A3A3A", "#2A2A2A"), corner_radius=15)
        self.header.pack(fill="x", padx=20, pady=15)
        self.header.grid_propagate(False)
        
        for i in range(3):
            self.header.columnconfigure(i, weight=1)
            
        header_font = ctk.CTkFont(family="Segoe UI", size=16, weight="bold")
        ctk.CTkLabel(self.header, text=f"👤 Player: {self.game.player}", 
                    font=header_font, text_color="#FFD700").grid(row=0, column=0, pady=20)
        ctk.CTkLabel(self.header, text=f"🎯 Level: {self.game.level_no}", 
                    font=header_font, text_color="#4FC3F7").grid(row=0, column=1, pady=20)
        self.won_money_label = ctk.CTkLabel(self.header, text=f"💰 Won: Rs.{self.game.won_money}", 
                                          font=header_font, text_color="#4CAF50")
        self.won_money_label.grid(row=0, column=2, pady=20)

        # --------------- GAME CONTENT ---------------------
        content_frame = ctk.CTkFrame(self.game_frame, fg_color="transparent")
        content_frame.pack(fill="both", expand=True, padx=20, pady=(10, 5))
        
        # Initializing Question, Prize Money and Comments
        self.question, self.game.prize_money, self.comments = next(self.game.question_generator)
        
        # Money info with better styling
        self.money_info = ctk.CTkLabel(content_frame, 
                                      text=f"🎁 Prize Money: Rs.{self.game.prize_money}",
                                      font=ctk.CTkFont(family="Segoe UI", size=20, weight="bold"),
                                      text_color="#FF9800")
        self.money_info.pack(pady=(0, 15))
        
        # Timer display
        self.timer_label = ctk.CTkLabel(content_frame, text="",
                                       font=ctk.CTkFont(family="Segoe UI", size=18, weight="bold"),
                                       text_color="#FF6B6B")
        self.timer_label.pack(pady=(0, 10))

        # Question frame with modern styling
        self.question_frame = ctk.CTkFrame(content_frame, corner_radius=15, 
                                          fg_color=("#3A3A3A", "#2A2A2A"),
                                          width=850, height=180)
        self.question_frame.pack(fill="x", pady=(0, 15))
        self.question_frame.pack_propagate(False)
        
        self.show_question = ctk.CTkLabel(self.question_frame, text="", 
                                         font=ctk.CTkFont(family="Segoe UI", size=16),
                                         text_color="#E0E0E0", wraplength=800,
                                         justify="center")
        self.show_question.pack(pady=20, padx=25)
        
        # Options frame
        self.options_frame = ctk.CTkFrame(content_frame, corner_radius=15,
                                         fg_color=("#3A3A3A", "#2A2A2A"),
                                         width=850, height=200)
        self.options_frame.pack(fill="x", pady=(0, 15))
        self.options_frame.grid_propagate(False)
        
        for i in range(2):
            self.options_frame.grid_columnconfigure(i, weight=1)
            self.options_frame.grid_rowconfigure(i, weight=1)
                
        # Create question and options
        self.show_question.configure(text=self.question[0])
        self.create_options()
        
        # Result label
        self.result_label = ctk.CTkLabel(content_frame, text="", 
                                        font=ctk.CTkFont(family="Segoe UI", size=16, weight="bold"),
                                        text_color="#FFFFFF")
        self.result_label.pack(pady=10)
        
        # Start timer based on level
        if self.game.level_no <= 5:
            self.start_timer(30)
        elif 6 <= self.game.level_no <= 10:
            self.start_timer(45)
        elif 11 <= self.game.level_no <= 15:
            self.start_timer(60)
        
        # --------------- FOOTER SETTINGS --------------
        self.footer = ctk.CTkFrame(self.game_frame, height=80, 
                                  fg_color=("#3A3A3A", "#2A2A2A"), 
                                  corner_radius=15)
        self.footer.pack(fill="x", padx=20, pady=5)
        self.footer.grid_propagate(False)
        
        self.footer.grid_columnconfigure(0, weight=1)
        self.footer.grid_columnconfigure(1, weight=1)
        self.footer.grid_columnconfigure(2, weight=1)
        
        # Lifeline buttons with icons
        self.btn_50_50 = ctk.CTkButton(self.footer, text="🔍 50:50", 
                                      font=ctk.CTkFont(family="Segoe UI", size=14, weight="bold"),
                                      width=120, height=35,
                                      fg_color="#FF9800" if self.game.use_50_50 else "#666666", hover_color="#F57C00" if self.game.use_50_50 else None,
                                      corner_radius=8, command=self.lifeline_50_50,
                                      state="normal" if self.game.use_50_50 else "disabled")
        self.btn_50_50.grid(row=0, column=0, padx=10, pady=20)
        
        self.btn_flip = ctk.CTkButton(self.footer, text="🔄 Flip", 
                                     font=ctk.CTkFont(family="Segoe UI", size=14, weight="bold"),
                                     width=120, height=35,
                                     fg_color="#9C27B0" if self.game.use_flip else "#666666", hover_color="#7B1FA2" if self.game.use_flip else None,
                                     corner_radius=8, command=self.lifeline_flip,
                                     state="normal" if self.game.use_flip else "disabled")
        self.btn_flip.grid(row=0, column=1, padx=10, pady=20)
        
        self.btn_quit = ctk.CTkButton(self.footer, text=f"🏃 Quit (Rs.{self.game.quit_money})", 
                                     font=ctk.CTkFont(family="Segoe UI", size=14, weight="bold"),
                                     width=140, height=35,
                                     fg_color="#F44336", hover_color="#D32F2F",
                                     corner_radius=8, 
                                     command=lambda: self.quit_game("✨ CONGRATULATIONS ✨", False, True))
        self.btn_quit.grid(row=0, column=2, padx=10, pady=20)
            
    def create_options(self):
        # Clear existing options
        for widget in self.options_frame.winfo_children():
            widget.destroy()
            
        btn_font = ctk.CTkFont(family="Segoe UI", size=14)
        row, column = 0, 0
        self.opts_50_50 = []
        
        for i, o in zip(range(1, 5), ["A", "B", "C", "D"]):
            if i == 3: 
                row, column = 1, 0
            opt_text = f"{o})  {self.question[i]}"
            wrap_text = textwrap.fill(opt_text, width=35)
            
            if self.question[i] == self.question[-1]:
                # Correct answer button
                btn = ctk.CTkButton(self.options_frame, text=wrap_text, 
                                   font=btn_font, cursor="hand2",
                                   height=45, corner_radius=10,
                                   command=self.correct_reply)
            else:
                # Wrong answer button
                btn = ctk.CTkButton(self.options_frame, text=wrap_text, 
                                   font=btn_font, cursor="hand2",
                                   height=45, corner_radius=10,
                                   command=lambda answer=self.question[-1]: self.wrong_reply(answer))
                self.opts_50_50.append(btn)
                
            btn.grid(row=row, column=column, padx=15, pady=10, sticky="ew")
            column += 1
        
    # ------------------ TIMER SETTINGS ---------------------------- 
    def start_timer(self, seconds):
        if seconds == -1: 
            self.root.after_cancel(self.timer_job)
            self.time_up()
            return
            
        self.timer_label.configure(text=f"⏰ {seconds:02d}s")
        self.timer_job = self.root.after(1000, self.start_timer, seconds - 1)
        
    def time_up(self):
        self.timer_label.configure(text="⌛ Time's Up!", text_color="#F44336")
        self.root.update()
        self.quit_game("✨ CONGRATULATIONS ✨", True, False)
            
    # ------------------ CHECK REPLY ---------------------------- 
    def correct_reply(self):
        if self.timer_job:
            self.root.after_cancel(self.timer_job)
        self.option_disable()
        self.result_label_settings("✓ Absolutely Right!", "#4CAF50")
        
        # Update money and level
        if self.game.level_no <= 5:
            self.game.won_money = self.game.prize_money
        elif self.game.level_no == 10:
            self.game.won_money = self.game.prize_money
        elif self.game.level_no == 15:
            self.game.won_money = self.game.prize_money
        elif self.game.level_no == 17:
            self.game.won_money = self.game.prize_money
            self.quit_game("✨ CONGRATULATIONS ✨\nYOU WON THE GAME!!!", True, False)
            return
            
        self.game.quit_money = self.game.prize_money
        self.game.level_no += 1
        
        # Show continue button
        for widget in self.options_frame.winfo_children():
            widget.destroy()
            
        continue_btn = ctk.CTkButton(self.options_frame, text="🎯 Click to Continue...", 
                                    width=300, height=50,
                                    font=ctk.CTkFont(family="Segoe UI", size=18, weight="bold"),
                                    fg_color="#30DB8B", hover_color="#14AB65",
                                    corner_radius=12, command=self.continue_game)
        continue_btn.place(relx=0.5, rely=0.5, anchor="center")
        
        self.won_money_label.configure(text=f"💰 Won: Rs.{self.game.won_money}")
        self.btn_quit.configure(text=f"🏃 Quit (Rs.{self.game.quit_money})", state="normal")
        
        # Show level-up messages
        self.show_level_up_message()
             
    def show_level_up_message(self):
        if self.game.level_no == 6:
            msgbox.showinfo(
                "🎊 Level Up!",
                "Congratulations! You've reached Levels 6–10\n\n"
                "• 45 seconds per question\n"
                "• Winnings locked at Rs. 10,000 until level 10\n"
                "• Use lifelines wisely!"
            )
        elif self.game.level_no == 11:
            msgbox.showinfo(
                "🚀 Advanced Levels!",
                "Welcome to Levels 11–15!\n\n"
                "• 60 seconds per question\n"
                "• Winnings locked at Rs. 3,20,000 until level 15\n"
                "• One wrong answer ends the game!\n"
                "• Stay focused!"
            )
        elif self.game.level_no == 16:
            msgbox.showinfo(
                "🏆 Final Rounds!",
                "Final Levels 16-17 - No Time Limit!\n\n"
                "• No time pressure\n"
                "• Winnings locked at Rs. 1,00,00,000\n"
                "• Grand Prize: Rs. 7,00,00,000!\n\n"
                "Make every answer count!"
            )
            
    def continue_game(self):
        self.game_frame.destroy()
        GameScreen(self.root, self.game)
             
    def wrong_reply(self, correct_answer):
        if self.timer_job:
            self.root.after_cancel(self.timer_job)
        self.option_disable()
        self.result_label_settings(f"✗ Wrong Answer!\nCorrect: '{correct_answer}'", "#F44336")
        self.quit_game("✨ CONGRATULATIONS ✨", True, False)
        
    def result_label_settings(self, text, color):
        # Animation for result display
        for i in range(1, 4):
            self.result_label.configure(text="." * i, text_color="#0A6792")
            self.root.update()
            time.sleep(0.3)
        
        # Show comments
        for comment in self.comments:
            self.result_label.configure(text=comment, text_color="#4FC3F7")
            self.root.update()
            time.sleep(1.7)
            
        time.sleep(1)
        self.result_label.configure(text=text, text_color=color)
        self.root.update()
        time.sleep(2)
        
    def option_disable(self):
        for option in self.options_frame.winfo_children():
            if isinstance(option, ctk.CTkButton):
                option.configure(state="disabled")
        for btn in (self.btn_50_50, self.btn_flip, self.btn_quit):
            btn.configure(state="disabled")
    
    # ------------------ LIFELINES ---------------------------- 
    def lifeline_50_50(self):
        # Disable two wrong options
        disabled_count = 0
        for btn in self.opts_50_50:
            if disabled_count < 2:
                btn.configure(state="disabled")
                disabled_count += 1
        self.btn_50_50.configure(state="disabled", fg_color="#666666")
        self.game.use_50_50 = False
        
    def lifeline_flip(self):
        self.game.use_flip = False
        self.btn_flip.configure(state="disabled", fg_color="#666666")
        
        # Replace with a new question
        self.question = self.game.questions[-1]  # Get last question as replacement
        self.show_question.configure(text=self.question[0])
        self.create_options()
        self.root.update()
        
    # ----------------- QUIT COMMAND --------------------
    def quit_game(self, text: str, wrong_reply_and_timer_over: bool, self_quit: bool):
        if self.timer_job:
            self.root.after_cancel(self.timer_job)
        self.game_frame.destroy()
        QuitScreen(self.root, self.game, text, wrong_reply_and_timer_over, self_quit)