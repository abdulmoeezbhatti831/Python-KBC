import customtkinter as ctk
import Questions
from GameScreen import GameScreen

# Configure customtkinter appearance
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

# ----------- RULES SCREEN SETTINGS -----------------
class RuleScreen:
    def __init__(self, root, game):
        self.root = root
        self.game = game
        self.rules_screen()
            
    def rules_screen(self):
        self.rules_frame = ctk.CTkFrame(self.root, corner_radius=20, fg_color=("#2B2B2B", "#1E1E1E"), width=900, height=650)
        self.rules_frame.pack(pady=25, padx=50, fill="both", expand=True)
        self.rules_frame.pack_propagate(False)
        
        # Header
        header_frame = ctk.CTkFrame(self.rules_frame, fg_color="transparent")
        header_frame.pack(pady=(30, 20), fill="x")
        
        ctk.CTkLabel(header_frame, text="📋 GAME RULES", 
                    font=ctk.CTkFont(family="Segoe UI", size=32, weight="bold"),
                    text_color="#FFD700").pack(pady=(0, 10))
        
        # Rules content 
        rules_container = ctk.CTkFrame(self.rules_frame, width=800, height=400,
                                                fg_color=("#3A3A3A", "#2A2A2A"), 
                                                corner_radius=15)
        rules_container.pack(pady=20, padx=20, fill="both", expand=True)
        
        rules_text = ctk.CTkTextbox(rules_container, width=750, height=480,
                                   font=ctk.CTkFont(family="Segoe UI", size=15),
                                   fg_color="transparent", border_width=0,
                                   text_color="#E0E0E0")
        rules_text.pack(pady=25, padx=5, fill="both", expand=True)
        
        # Format rules text
        formatted_rules = self.format_rules(Questions.RULES)
        rules_text.insert("1.0", formatted_rules)
        rules_text.configure(state="disabled")
        
        # Navigation buttons
        btn_frame = ctk.CTkFrame(self.rules_frame, fg_color="transparent")
        btn_frame.pack(pady=10)
        
        back_btn = ctk.CTkButton(btn_frame, text="← BACK", 
                                font=ctk.CTkFont(family="Segoe UI", size=14, weight="bold"),
                                width=120, height=40,
                                fg_color="#6C757D", hover_color="#5A6268",
                                corner_radius=8, command=self.back_to_welcome_screen)
        back_btn.grid(row=0, column=0, padx=15)
        
        start_btn = ctk.CTkButton(btn_frame, text="START GAME →", 
                                 font=ctk.CTkFont(family="Segoe UI", size=14, weight="bold"),
                                 width=150, height=40,
                                 fg_color="#28A745", hover_color="#218838",
                                 corner_radius=8, command=self.go_to_game_screen)
        start_btn.grid(row=0, column=1, padx=15)
        
    def format_rules(self, rules_text):
        """Format rules text with better readability"""
        lines = rules_text.split('\n')
        formatted_lines = []
        
        for line in lines:
            if line.strip().startswith('•'):
                formatted_lines.append(f"    {line.strip()}")
            elif any(line.strip().startswith(word) for word in ['1)', '2)', '3)', '4)', '5)', '6)']):
                formatted_lines.append(f"\n{line.strip()}")
            elif line.strip() and not line.isspace():
                formatted_lines.append(f"\n{line.strip()}")
            else:
                formatted_lines.append(line)
                
        return '\n'.join(formatted_lines)
        
    def back_to_welcome_screen(self):
        from WelcomeScreen import WelcomeScreen
        self.rules_frame.destroy()
        WelcomeScreen(self.root, self.game, False)

    def go_to_game_screen(self):
        self.rules_frame.destroy()
        GameScreen(self.root, self.game)