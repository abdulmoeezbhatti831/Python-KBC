from Questions import questions, levels, Commitments
import time, threading, sys, random

class Python_KBC:
    def __init__(self, player):
        random.shuffle(questions)
        random.shuffle(Commitments)
        self.player = player
        self.question = None
        self.reply = ""
        self.money = 0
        self.use_50 = 1
        self.use_flip = 1
        
    def call_question(self, question, level, i):
        if i != 0: input("\n>>> Press Enter to continue <<<\n")
        else: input("\n>>> Press Enter to Start the Game <<<\n")
        time.sleep(1)
        
        print(f"💠 Question No. {i+1} for 💸Rs.{level}\n")
        time.sleep(0.3)
        print(question[0])
        time.sleep(0.3)
        print(f"\nA) {question[1]}          B) {question[2]}")
        print(f"\nC) {question[3]}          D) {question[4]}\n")
        
    def get_reply(self, question, i):
        self.reply = ""
        def rep():
            self.reply = input().lower()
        re = threading.Thread(target=rep)
        if i+1 <= 5:
            re.start()
            for q in range(30):
                if self.reply != "":
                    break
                elif q == 29:
                    self.wrong_reply(question, True)
                else:
                    sys.stdout.write(f"\r⏳ 00 : {str(30-q).zfill(2)}\t> ")
                    sys.stdout.flush()
                    time.sleep(1)
            re.join()
        if i+1 >= 6 and i+1 <= 10:
            print("Ans:\n")
            re.start()
            for q in range(45):
                if self.reply != "":
                    break
                elif q == 44:
                    self.wrong_reply(question, True)
                else:
                    sys.stdout.write(f"\r⏳ 00 : {str(45-q).zfill(2)}\t> ")
                    sys.stdout.flush()
                    time.sleep(1)
            re.join()
        if i+1 >= 11 and i+1 <= 15:
            print("Ans:\n")
            re.start()
            for q in range(60):
                if self.reply != "":
                    break
                elif q == 59:
                    self.wrong_reply(question, True)
                else:
                    sys.stdout.write(f"\r⏳ 00 : {str(60-q).zfill(2)}\t> ")
                    sys.stdout.flush()
                    time.sleep(1)
            re.join()
        if i+1 >= 16:
            self.reply = input("Ans:\n> ").lower()
            
    def comments(self, i):
        print(f"\n{Commitments[i]}")
        time.sleep(2)
        print(f"{Commitments[-(i+1)]}\n")

        for i in range(3):
            time.sleep(1.3)
            sys.stdout.write("\r" + "." * (i + 1))
            sys.stdout.flush()
        print()
        
    def check_reply(self, question, level, i):
        if self.reply == "a":
            self.reply = question[1]
        elif self.reply == "b":
            self.reply = question[2]
        elif self.reply == "c":
            self.reply = question[3]
        elif self.reply == "d":
            self.reply = question[4]
            
        if self.reply == question[-1]:
            time.sleep(0.5)
            print(f"✅ Absolutly Right!")
            time.sleep(0.5)
            
            if i+1 <= 5:
                self.money = level
                print(f"👉 Now, Your Total Money is: 💸Rs.{self.money}\n")
                time.sleep(1.5)
                if i+1 == 5:
                    print(f"✨ Congratulations {self.player}!\nYou have won 💸Rs.{self.money}!\n")
                    time.sleep(1.5)
                    
            elif i+1 > 5 and i+1 < 10:
                self.money = 10000
                print(f"👉 As this is Level {i+1}. So, Your Money remains 💸Rs.{self.money} until you reach the Level 10.")
                time.sleep(0.5)
                print(f"🚫 If You Quit Now, You could take 💸Rs.{level} to Your home!\n")
                time.sleep(1.5)
                
            elif i+1 >= 10 and i+1 < 14:
                self.money = 320000
                if i+1 == 10:
                    print(f"\n✨ Congratulations {self.player}!\nYou have won Rs.{self.money}!\n")
                    time.sleep(0.5)
                print(f"👉 As this is Level {i+1}. So, Your Money remains 💸Rs.{self.money} until you reach the Level 14.")
                time.sleep(0.5)
                print(f"🚫 If You Quit Now, You could take 💸Rs.{level} to Your home!\n")
                time.sleep(1.5)
                
            elif i+1 >= 14 and i+1 <= 16:
                self.money = 5000000
                if i+1 == 14:
                    print(f"\n✨ Congratulations {self.player}!\nYou have won 💸Rs.{self.money}!\n")
                    time.sleep(0.5)
                print(f"👉 As this is Level {i+1}. So, Your Money remains 💸Rs.{self.money} until you reach the Last Level!!!")
                time.sleep(0.5)
                if i+1 == 16:
                    print("😲 YOU HAVE REACHED THE LAST LEVEL!!!")
                print(f"🚫 If You Quit Now, You could take 💸Rs.{level} to Your home!\n")
                time.sleep(1.5)
                
            elif i+1 == 17:
                self.money = 70000000
                print(f"\n✨ Congratulations  {self.player}!!!\nYou have won Rs.{self.money}!!!\n")
                input()
                exit(0)
        
        elif self.reply != question[-1]:
            self.wrong_reply(question, False)
            
    def reply_quit(self, i):
        time.sleep(0.5)
        print(f"\n🙋 As you are quiting the game {self.player}! So, Your Total Money which you taking to your home is Rs.{levels[i-1]}")
        time.sleep(0.3)
        print("🌠 Wishing You Good Luck for next time!")
        exit(0)
        
    def reply_lifeline(self, question, i):
        time.sleep(0.5)
            
        if self.use_50 == 0 and self.use_flip == 0:
            time.sleep(0.5)
            print("\n❌ You used all the life lines!")
            time.sleep(0.3)
            print("So, Which option you want to be should locked 🔒?\nAns:\n")
            self.get_reply(self.question, i = i//2)
            time.sleep(1)

        else:
            time.sleep(0.3)
            print(f"\n1) for 50:50😎 ({self.use_50} left) \t2) for flip the question🔃 ({self.use_flip} left)")
            life_line = int(input("So, Please tell us your choice: "))

            if self.use_50 == 0 and life_line == 1:
                time.sleep(0.5)
                print("\n❌ You used 50:50 life line!")
                life_line = int(input("Please Enter 2) for flip the question🔃: "))

            if self.use_flip == 0 and life_line == 2:
                time.sleep(0.5)
                print("\n❌ You used flip the question life line!")
                life_line = int(input("Please Enter 1) for 50:50😎: "))

            if life_line == 1:
                if self.use_50 == 1:
                    print(f"\n{question[0]}\n")
                    k1 = ""
                    k2 = ""
                    o1 = 0
                    o2 = 0
                    for j in range(1, 5):
                        if question[j] == question[-1]:
                            if j == 1:
                                k1 = "A"
                                o1 = 1
                            if j == 2:
                                k1 = "B"
                                o1 = 2
                            if j == 3:
                                k1 = "C"
                                o1 = 3
                            if j == 4:
                                k1 = "D"
                                o1 = 4
                            if j - 1 == 0:
                                k2 = "D"
                                o2 = 4
                            if j - 1 != 0:
                                if j - 1 == 1:
                                    k2 = "A"
                                    o2 = 1
                                if j - 1 == 2:
                                    k2 = "B"
                                    o2 = 2
                                if j - 1 == 3:
                                    k2 = "C"
                                    o2 = 3
                    time.sleep(0.3)
                    if o1 > o2:
                        print(f"\n{k2}) {question[o2]}          {k1}) {question[o1]}")
                    if o2 > o1:
                        print(f"\n{k1}) {question[o1]}          {k2}) {question[o2]}")
                    time.sleep(0.3)
                    print("\nSo, Which option you want to be should locked 🔒?")
                    self.get_reply(question, i= i//2)
                    time.sleep(1)
                    self.use_50 = 0

            if life_line == 2:
                if self.use_flip == 1:
                    self.question = questions[-1]
                    self.call_question(self.question, levels[i], i)
                    time.sleep(0.3)
                    print("So, Which option you want to be should locked 🔒?")
                    self.get_reply(self.question, i= i//2)
                    time.sleep(1)
                    self.use_flip = 0
            
    def wrong_reply(self, question, time_over):
        if time_over:
            print("\t⌛ Time's Up!")
            time.sleep(0.3)
            print(f"\n✋ But You are taking 💸Rs.{self.money} to your home {self.player}!")
            time.sleep(0.5)
            print(f"⌛ Wait...")
            time.sleep(1.5)
            print(f"☑️  The Right answer was '{question[-1]}'")
            time.sleep(0.3)
            print("🌠 Wishing You Good Luck for next time!")
            input()
            exit(0)
        else:
            time.sleep(0.5)
            print("\n❌ Wrong Answer!")
            time.sleep(0.3)
            print(f"✋ But You are taking 💸Rs.{self.money} to your home {self.player}!")
            time.sleep(0.5)
            print(f"⌛ Wait...")
            time.sleep(1.5)
            print(f"☑️  The Right answer was '{question[-1]}'")
            time.sleep(0.3)
            print("🌠 Wishing You Good Luck for next time!")
            input()
            exit(0)
            
    def main(self):
        print("\n✨ WELCOME TO THE PYTHON KBC GAME ✨\n")
        print('''RULES >>>
        [1] From Question 1 to 5 -> No options of life line and quiting the Game!
        [2] Time for Question 1 to 5 -> 30s, 6 to 10 -> 45s, 11 to 15 -> 60s, 16 and 17 -> No time limit!
        [3] Choicing a life line will cause a decrease time for answering!
        [4] Be careful if choicing life line if there's none, will cause decrease in time limit!
        [5] Must be careful on giving reply if invalid reply given full Game will Shutdown!!!\n''')
        time.sleep(0.5)
        for i in range(17):
            self.question = questions[i]
            time.sleep(0.5)
            self.call_question(self.question, levels[i], i)
            if i+1 > 5:
                time.sleep(1.3)
                print("So, Which option you want to be should locked 🔒?\nDo you want to quit 🚫 (Enter '1')?\nWant to chose a life line 🍀 (Enter '2')?")
                self.get_reply(self.question, i)
                if self.reply not in "abcd12":
                    print("\n❌ Invalid Reply\nExisting...")
                    exit(0)
                if self.reply == "1":
                    self.reply_quit(i)
                if self.reply == "2":
                    self.reply_lifeline(self.question, i)
                    if self.reply not in "abcd":
                        print("\n❌ Invalid Reply\nExisting...")
                        exit(0)
            else:
                time.sleep(1.3)
                print("So, Which option you want to be should locked 🔒?\nAns:\n")
                self.get_reply(self.question, i)
                if self.reply not in "abcd":
                    print("\n❌ Invalid Reply\nExisting...")
                    exit(0)
            self.comments(i)
            self.check_reply(self.question, levels[i], i)
            
                
if __name__ == "__main__":
    Game = Python_KBC(input("Player Name: ").title())
    Game.main()