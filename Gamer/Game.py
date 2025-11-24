import customtkinter as ctk
import tkinter.messagebox as msgbox
import textwrap
import time
from Quit import QuitScreen


# ------------- GAME SCREEN SETTINGS ---------------
class GameScreen:
    def __init__(self, root, game):
        self.root = root
        self.game = game
        self.timer_job = None # Handles the time in levels
        
        self.game_screen()
        
    def game_screen(self):
        self.game_frame = ctk.CTkFrame(self.root, corner_radius=5, width=self.root.winfo_width(), height=self.root.winfo_height())
        self.game_frame.pack()
        self.game_frame.pack_propagate(False)

        # --------------- GAME SCREEN SETTINGS >> HEADER SETTINGS -------------------
        self.header = ctk.CTkFrame(self.game_frame, corner_radius=5, height=50)
        self.header.pack(fill="x", side="top")
        self.header.grid_propagate(False)
        
        for i in range(3):
            self.header.columnconfigure(i, weight=1)
            
        header_font = ctk.CTkFont(family="helvetica", size=18, weight="bold")
        ctk.CTkLabel(self.header, text=f"Player: {self.game.player}", font=header_font).grid(row=0, column=0, pady=12)
        ctk.CTkLabel(self.header, text=f"Level: {self.game.level_no}", font=header_font).grid(row=0, column=1, pady=12)
        self.won_money_label = ctk.CTkLabel(self.header, text=f"Won Money: 💸 Rs.{self.game.won_money}", font=header_font)
        self.won_money_label.grid(row=0, column=2, pady=12)

        # --------------- GAME SCREEN SETTINGS >> BACKEND VARIABLES --------------
        self.question, self.game.prize_money, self.comments = next(self.game.question_generator)
        
        # --------------- GAME SCREEN SETTINGS >> MONEY INFO ---------------------
        self.money_info = ctk.CTkLabel(self.game_frame, text=f"For Money >> '💸 Rs.{self.game.prize_money}'", font=ctk.CTkFont(family="Helvetica", size=20, weight="bold", slant="italic"))
        self.money_info.pack(pady=10)
        
        # --------------- GAME SCREEN SETTINGS >> QUESTION FRAME ---------------------
        self.question_frame = ctk.CTkFrame(self.game_frame, corner_radius=10, width=(self.root.winfo_width() - 250), height=280)
        self.question_frame.pack()
        self.question_frame.pack_propagate(False)
        
        self.show_question = ctk.CTkLabel(self.question_frame, text=self.question[0], font=ctk.CTkFont(family="Helvetica", size=18))
        self.show_question.pack(pady=5)

        # --------------- GAME SCREEN SETTINGS >> QUESTION FRAME >> OPTIONS FRAME & SETTINGS ---------------------
        self.options_frame = ctk.CTkFrame(self.question_frame, corner_radius=10, width=(self.root.winfo_width() - 350), height=200)
        self.options_frame.pack(pady=5)
        self.options_frame.grid_propagate(False)
        
        for i in range(2):
            self.options_frame.grid_columnconfigure(i, weight=1)
            self.options_frame.grid_rowconfigure(i, weight=1)
                
        btn_font = ctk.CTkFont(family="Helvetica", size=15)
        row, column = 0, 0
        self.opts_50_50 = []
        for i, o in zip(range(1, 5), ["A", "B", "C", "D"]):
            if i == 3: row, column = 1, 0
            opt_text = f"{o})  {self.question[i]}"
            wrap_text = textwrap.fill(opt_text, width=40)
            if self.question[i] == self.question[-1]:
                ctk.CTkButton(self.options_frame, text=wrap_text, command=self.correct_reply, font=btn_font, cursor="hand2").grid(row=row, column=column)
            else:
                btn = ctk.CTkButton(self.options_frame, text=wrap_text, command=lambda answer=self.question[-1]: self.wrong_reply(answer), font=btn_font, cursor="hand2")
                btn.grid(row=row, column=column)
                self.opts_50_50.append(btn)
            column += 1
        
        # --------------- GAME SCREEN SETTINGS >> RESULT LABEL -----------------
        self.result_label = ctk.CTkLabel(self.game_frame, text="", text_color="white", font=ctk.CTkFont(family="Helvetica", size=18, weight="bold", slant="italic"))
        self.result_label.pack(pady=10)
        
        if self.game.level_no <= 5:
            self.start_timer(30)
        elif self.game.level_no >= 6 and self.game.level_no <= 10:
            self.start_timer(45)
        elif self.game.level_no >= 11 and self.game.level_no <= 15:
            self.start_timer(60)
            
        # --------------- GAME SCREEN SETTINGS >> FOOTER SETTINGS --------------
        self.footer = ctk.CTkFrame(self.game_frame, corner_radius=5, height=50)
        self.footer.pack(fill="x", side="bottom")
        self.footer.grid_propagate(False)
        
        self.footer.grid_columnconfigure(0, weight=1)
        self.footer.grid_columnconfigure(1, weight=0)
        self.footer.grid_columnconfigure(2, weight=1)
        self.footer.grid_columnconfigure(3, weight=1)
        
        self.btn_50_50 = ctk.CTkButton(self.footer, text=" 50 : 50 ", font=("helvetica", 16), command=self.lifeline_50_50, state="normal" if self.game.use_50_50 else "disabled")
        self.btn_50_50.grid(row=0, column=0, pady=10)
        self.btn_flip = ctk.CTkButton(self.footer, text=" Flip the Question ", font=("helvetica", 16), command=self.lifeline_flip, state="normal" if self.game.use_flip else "disabled")
        self.btn_flip.grid(row=0, column=1, pady=10)
        self.btn_quit = ctk.CTkButton(self.footer, text=f" Quit (💸 Rs.{self.game.quit_money})", font=("helvetica", 16), command=lambda t="✨ CONGRATULATIONS ✨", w_t=False, q=True: self.quit_game(t, w_t, q))
        self.btn_quit.grid(row=0, column=3, pady=10)
            
    # ------------------ GAME SCREEN SETTINGS >> TIMER SETTINGS ---------------------------- 
    def start_timer(self, seconds):
        if seconds == -1: 
            self.root.after_cancel(self.timer_job)
            self.time_up()
        self.result_label.configure(text=f"⏳ -- {seconds:02}", text_color="white", font=ctk.CTkFont(family="Helvetica", size=18, weight="bold"))
        self.timer_job = self.root.after(1000, self.start_timer, seconds - 1)
        
    def time_up(self):
        self.result_label.configure(text=f"⌛ Time's Up!", text_color="white", font=ctk.CTkFont(family="Helvetica", size=18, weight="bold"))
        self.root.update()
        self.quit_game("✨ CONGRATULATIONS ✨", True, False)
            
    # ------------------ GAME SCREEN SETTINGS >> CHECK REPLY ---------------------------- 
    def correct_reply(self):
        if self.timer_job:
            self.root.after_cancel(self.timer_job)
        self.option_disable()
        self.result_label_settings("✓ Absolutely Right!", "green")
        
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
        
        for widget in self.options_frame.winfo_children():
            widget.destroy()
        self.root.update()
        ctk.CTkButton(self.options_frame, text=" Click to Continue... ", width=300, font=("Helvetica", 18, "italic"), command=self.continue_game).place(relx=0.5, rely=0.5, anchor="center")
        
        self.won_money_label.configure(text=f"Won Money: 💸 Rs.{self.game.won_money}")
        self.btn_quit.configure(text=f" Quit (💸 Rs.{self.game.quit_money})", state="normal")
        self.root.update()
        
        if self.game.level_no == 6:
            msgbox.showinfo(
            "Levels 6–10",
            "Levels 6–10 — 45 sec per question\n\n"
            "• 45 seconds per question\n"
            "• Winnings locked at Rs. 10,000 until level 10\n"
            "• You may quit to take the previous level's prize\n"
            "• Use lifelines wisely"
            )
        elif self.game.level_no == 11:
            msgbox.showinfo(
            "Levels 11–15",
            "Levels 11–15 — 60 sec per question\n\n"
            "• 60 seconds per question\n"
            "• Winnings locked at Rs. 3,20,000 until level 15\n"
            "• You may quit to take the previous level's prize\n"
            "• One wrong answer ends the game"
            )
        elif self.game.level_no == 16:
            msgbox.showinfo(
            "Final Levels (16–17)",
            "Final Levels — No timer\n\n"
            "• No time limit for these questions\n"
            "• Winnings locked at Rs. 1,00,00,000 until final level\n"
            "• You may quit to take the previous level's prize\n\n"
            "Prize highlights:\n"
            "• Level 16: Rs. 3,00,00,000\n"
            "• Level 17 (Grand Prize): Rs. 7,00,00,000\n\n"
            "Good luck!"
            )
            
    def continue_game(self):
        self.game_frame.destroy()
        GameScreen(self.root, self.game)
             
    def wrong_reply(self, correct_answer):
        if self.timer_job:
            self.root.after_cancel(self.timer_job)
        self.option_disable()
        self.result_label_settings(f"✗ Wrong Answer!\nCorrect Answer : '{correct_answer}'", "red")
        self.quit_game("✨ CONGRATULATIONS ✨", True, False)
        
    def result_label_settings(self, text, color):
        for i in range(1, 4):
            self.result_label.configure(text="." * i, text_color="white", font=ctk.CTkFont(family="Helvetica", size=18, weight="bold"))
            self.root.update()
            time.sleep(0.3)
        
        for comment in self.comments:
            self.result_label.configure(text=comment, text_color="light blue", font=ctk.CTkFont(family="Helvetica", size=18, weight="bold"))
            self.root.update()
            time.sleep(1.7)
            
        time.sleep(2)
        self.result_label.configure(text=text, text_color=color, font=ctk.CTkFont(family="Helvetica", size=18, weight="bold", slant="italic"))
        self.root.update()
        time.sleep(3)
        
    def option_disable(self):
        for option in self.options_frame.winfo_children():
            if isinstance(option, ctk.CTkButton):
                option.configure(state="disabled")
        for btn in (self.btn_50_50, self.btn_flip, self.btn_quit):
            btn.configure(state="disabled")
    
    # ------------------ GAME SCREEN SETTINGS >> LIFELINES ---------------------------- 
    def lifeline_50_50(self):
        for i, btn in enumerate(self.opts_50_50):
            if i == 2: break
            btn.configure(state="disabled")
        self.btn_50_50.configure(state="disabled")
        self.game.use_50_50 = False
        
    def lifeline_flip(self):
        self.game.use_flip = False
        self.btn_flip.configure(state="disabled")
        for widget in self.options_frame.winfo_children():
            widget.destroy()
        
        # Question
        self.question = self.game.questions[-1]
        self.show_question.configure(text=self.question[0])
        
        # Options
        btn_font = ctk.CTkFont(family="Helvetica", size=15)
        row, column = 0, 0
        self.opts_50_50 = []
        for i, o in zip(range(1, 5), ["A", "B", "C", "D"]):
            if i == 3: row, column = 1, 0
            opt_text = f"{o})  {self.question[i]}"
            wrap_text = textwrap.fill(opt_text, width=40)
            if self.question[i] == self.question[-1]:
                ctk.CTkButton(self.options_frame, text=wrap_text, command=self.correct_reply, font=btn_font, cursor="hand2").grid(row=row, column=column)
            else:
                btn = ctk.CTkButton(self.options_frame, text=wrap_text, command=lambda answer=self.question[-1]: self.wrong_reply(answer), font=btn_font, cursor="hand2")
                btn.grid(row=row, column=column)
                self.opts_50_50.append(btn)
            column += 1
            
        self.root.update()
    # ----------------- GAME SCREEN SETTINGS >> QUIT COMMAND --------------------
    def quit_game(self, text : str, wrong_reply_and_timer_over : bool, self_quit : bool):
        if self.timer_job:
            self.root.after_cancel(self.timer_job)
        self.game_frame.destroy()
        QuitScreen(self.root, self.game, text, wrong_reply_and_timer_over, self_quit)