import customtkinter as ctk
import tkinter.messagebox as msgbox
import Questions
import time
import random
import textwrap

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
        self.won_money = ""
        self.quit_money = ""
        self.level_no = 1
        
        self.use_50_50 = True
        self.use_flip = True
        self.make_flip = False
        
        self.timer_job = None
        
        # ----------- ENABLING FRAMES --------------
        self.welcome_player = True 
        self.welcome_screen()
        
    # ------------- WELCOME SCREEN SETTINGS -------------
    def welcome_screen(self):
        self.welcome_frame = ctk.CTkFrame(self.root, corner_radius=5, width=700, height=600)
        self.welcome_frame.pack(pady=50)
        self.welcome_frame.pack_propagate(False)
        
        welcome = "✨ WELCOME TO THE PYTHON KBC GAME ✨"
        
        welcome_text = ctk.CTkLabel(self.welcome_frame, text=welcome, font=ctk.CTkFont(family="Times New Roman", size=40, weight="bold", slant="italic"), text_color="#328FB4", wraplength=600)
        welcome_text.pack(pady=70) 
        self.root.update()
        
        if self.welcome_player:
            for i in range(len(welcome) + 1):
                welcome_text.configure(text=welcome[0:i+1])
                self.root.update()
                time.sleep(0.2)
                
            time.sleep(1)
            self.welcome_player = False
            
        self.player_name = ctk.CTkEntry(self.welcome_frame, placeholder_text="Player Name...", width=300, height=35, border_width=1, border_color="light blue")
        self.player_name.pack(pady=(0, 20))
        
        ctk.CTkButton(self.welcome_frame, text=" GO! ", font=ctk.CTkFont(family="Segeo UI", size=17, weight="bold", slant="italic"), command=self.go_to_rules_screen).pack()
        
    def go_to_rules_screen(self):
        if self.player_name.get() == "":
            self.player_name.configure(placeholder_text="Enter your name!", placeholder_text_color="red")
        else:
            self.player_name.configure(placeholder_text_color="blue")
            self.player = self.player_name.get()
            self.welcome_frame.destroy()
            self.rules_screen()
            
    # ----------- RULES SCREEN SETTINGS -----------------
    def rules_screen(self):
        self.rules_frame = ctk.CTkFrame(self.root, corner_radius=5, width=700, height=400)
        self.rules_frame.pack(pady=(50, 0))
        self.rules_frame.pack_propagate(False)
        
        ctk.CTkLabel(self.rules_frame, text="RULES", font=ctk.CTkFont(family="Times New Roman", size=35, weight="bold", slant="italic"), text_color="white", wraplength=600).pack(pady=(40, 20))
        
        RULES = """PYTHON KBC — GAME RULES

    1) Objective
       - Answer successive multiple‑choice questions to climb levels and win higher prize money.
       - Reach the top level to win the maximum prize.

    2) Questions & Time Limits
       - Total questions: 17 (one per level).
       - Levels 1–5  : 30 seconds per question.
       - Levels 6–10 : 45 seconds per question.
       - Levels 11–15: 60 seconds per question.
       - Levels 16 & 17: no time limit per question.
       - If the timer runs out on a question, the game ends and you take the last won money.

    3) Lifelines (each usable only once per game)
       - 50:50 : Removes two incorrect options for the current question.
       - Flip  : Replaces the current question with another one.
       - After a lifeline is used it becomes disabled for the remainder of the game.

    4) Answering & Progress
       - Selecting the correct option advances you to the next level and increases your prize.
       - Selecting a wrong option ends the game; you leave with the last won money.
       - The Quit button lets you stop the game voluntarily and take the current quit money.

    5) Navigation
       - Use 'Start Game' to begin, 'Back' to return to the previous screen, and 'Play Again' to restart after finishing.

    6) Notes
       - The timer resets for every new question.
       - Lifelines affect only the current question and cannot be undone.
       - Read on‑screen messages and prompts carefully before proceeding.

    Good luck!
            """
        
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
        self.rules_frame.destroy()
        self.welcome_screen()

    def go_to_game_screen(self):
        self.rules_frame.destroy()
        self.game_screen()
        
    # ------------- GAME SCREEN SETTINGS ---------------
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
        ctk.CTkLabel(self.header, text=f"Player: {self.player}", font=header_font).grid(row=0, column=0, pady=12)
        ctk.CTkLabel(self.header, text=f"Level: {self.level_no}", font=header_font).grid(row=0, column=1, pady=12)
        ctk.CTkLabel(self.header, text=f"Won Money: 💸 Rs.{self.won_money}", font=header_font).grid(row=0, column=2, pady=12)

        # --------------- GAME SCREEN SETTINGS >> BACKEND VARIABLE --------------
        if self.make_flip:
            self.question = self.questions[-1]
        else:
            try:
                self.question, self.prize_money, self.comments = next(self.question_generator)
            except Exception:
                self.quit_game("✨ CONGRATULATIONS ✨\nYOU WON THE GAME!!!", True, False)
        
        # --------------- GAME SCREEN SETTINGS >> MONEY INFO ---------------------
        self.money_info = ctk.CTkLabel(self.game_frame, text=f"For Money >> '💸 Rs.{self.prize_money}'", font=ctk.CTkFont(family="Helvetica", size=20, weight="bold", slant="italic"))
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
        
        if not self.make_flip:
            if self.level_no <= 5:
                self.start_timer(30)
            elif self.level_no >= 6 and self.level_no <= 10:
                self.start_timer(45)
            elif self.level_no >= 11 and self.level_no <= 15:
                self.start_timer(60)
        if self.make_flip:
            self.make_flip = False
            
        # --------------- GAME SCREEN SETTINGS >> FOOTER SETTINGS --------------
        self.footer = ctk.CTkFrame(self.game_frame, corner_radius=5, height=50)
        self.footer.pack(fill="x", side="bottom")
        self.footer.grid_propagate(False)
        
        self.footer.grid_columnconfigure(0, weight=1)
        self.footer.grid_columnconfigure(1, weight=0)
        self.footer.grid_columnconfigure(2, weight=1)
        self.footer.grid_columnconfigure(3, weight=1)
        
        self.btn_50_50 = ctk.CTkButton(self.footer, text=" 50 : 50 ", font=("helvetica", 16), command=self.lifeline_50_50, state="normal" if self.use_50_50 else "disabled")
        self.btn_50_50.grid(row=0, column=0, pady=10)
        self.btn_flip = ctk.CTkButton(self.footer, text=" Flip the Question ", font=("helvetica", 16), command=self.lifeline_flip, state="normal" if self.use_flip else "disabled")
        self.btn_flip.grid(row=0, column=1, pady=10)
        self.btn_quit = ctk.CTkButton(self.footer, text=f" Quit (💸 Rs.{self.quit_money})", font=("helvetica", 16), command=lambda t="✨ CONGRATULATIONS ✨", w_t=False, q=True: self.quit_game(t, w_t, q))
        self.btn_quit.grid(row=0, column=3, pady=10)
        
    # ------------------ GAME SCREEN SETTINGS >> CALL THE QUESTION ---------------------------- 
    def call_question(self):
        for i in range(len(self.levels) + 1):
            yield self.questions[i], self.levels[i], [random.choice(self.Comments), random.choice(self.Comments)]
            
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
        self.root.after_cancel(self.timer_job)
        self.option_disable()
        self.result_label_settings("✅ Absolutely Right!", "green")
        
        if self.level_no <= 5:
            self.won_money = self.prize_money
        elif self.level_no == 10:
            self.won_money = self.prize_money
        elif self.level_no == 15:
            self.won_money = self.prize_money
        elif self.level_no == 17:
            self.won_money = self.prize_money
            
        self.quit_money = self.prize_money
        self.level_no += 1
        
        for widget in self.options_frame.winfo_children():
            widget.destroy()
        self.root.update()
        self.options_frame.pack_propagate(False)
        ctk.CTkButton(self.options_frame, text=" Click to Contiune... ", width=300, font=("Helvetica", 18, "italic"), command=self.continue_game).pack(padx=50, pady=50)
        
        if self.level_no == 6:
            msgbox.showinfo(
            "Levels 6–10",
            "Levels 6–10 — 45 sec per question\n\n"
            "• 45 seconds per question\n"
            "• Winnings locked at Rs. 10,000 until level 10\n"
            "• You may quit to take the previous level's prize\n"
            "• Use lifelines wisely"
            )
        elif self.level_no == 11:
            msgbox.showinfo(
            "Levels 11–15",
            "Levels 11–15 — 60 sec per question\n\n"
            "• 60 seconds per question\n"
            "• Winnings locked at Rs. 3,20,000 until level 15\n"
            "• You may quit to take the previous level's prize\n"
            "• One wrong answer ends the game"
            )
        elif self.level_no == 16:
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
        self.game_screen()
             
    def wrong_reply(self, correct_answer):
        self.root.after_cancel(self.timer_job)
        self.option_disable()
        self.result_label_settings(f"❌ Wrong Answer!\nCorrect Answer : '{correct_answer}'", "red")
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
            
        self.result_label.configure(text=text, text_color=color, font=ctk.CTkFont(family="Helvetica", size=18, weight="bold", slant="italic"))
        self.root.update()
        time.sleep(3)
        
    def option_disable(self):
        for option in self.options_frame.winfo_children():
            if isinstance(option, ctk.CTkButton):
                option.configure(state="disabled")
    
    # ------------------ GAME SCREEN SETTINGS >> LIFELINES ---------------------------- 
    def lifeline_50_50(self):
        for i, btn in enumerate(self.opts_50_50):
            if i == 2: break
            btn.configure(state="disabled")
        self.btn_50_50.configure(state="disabled")
        self.use_50_50 = False
        
    def lifeline_flip(self):
        self.use_flip = False
        self.make_flip = True
        self.game_frame.destroy()
        self.game_screen()
        self.btn_flip.configure(state="disabled")        
        
    # ----------------- GAME SCREEN SETTINGS >> QUIT COMMAND --------------------
    def quit_game(self, text : str, wrong_reply_and_timer_over : bool, self_quit : bool):
        self.game_frame.destroy()
        self.quit_screen(text, wrong_reply_and_timer_over, self_quit)
    
    # ------------------ QUITING SCREEN SETTINGS ------------------
    def quit_screen(self, text : str, wrong_reply_and_timer_over : bool, self_quit : bool):
        self.quit_frame = ctk.CTkFrame(self.root, corner_radius=5, width=700, height=400)
        self.quit_frame.pack(pady=(50, 0))
        self.quit_frame.pack_propagate(False)
        
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
            money = self.won_money
        if self_quit:
            money = self.quit_money
            
        ctk.CTkLabel(self.quit_frame, text=f"{self.player}, you are taking 💸Rs.{money} with you!", font=ctk.CTkFont(family="Helvetica", size=18)).pack()

        quit_frame_footer = ctk.CTkFrame(self.quit_frame)
        quit_frame_footer.pack(pady=(50, 0))
        
        ctk.CTkButton(quit_frame_footer, text=" Play Again ", command=self.play_again).grid(row=0, column=0, padx=8)
        ctk.CTkButton(quit_frame_footer, text=" Exit ", command=self.root.destroy).grid(row=0, column=1, padx=8)
        
    def play_again(self):
        self.quit_frame.destroy()
        self.welcome_screen()

    # -------------- RUN THE GAME ----------------
    def run(self):
        self.root.mainloop()
        
if __name__ == "__main__" :
    try:
        Game = PythonKBC(ctk.CTk())
        Game.run()
    except Exception:
        pass