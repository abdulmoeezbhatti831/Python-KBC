# Python-KBC

Author:  Abdul Moeez Bhatti

Python-KBC is a GUI-based Kaun Banega Crorepati (KBC) style quiz game implemented in Python using customtkinter. The game presents multiple-choice Python questions across 17 levels, with increasing prize money, lifelines (50:50 and Flip), timers for early levels, and options to quit and take home winnings.

## Features

- Modern dark-themed GUI built with customtkinter
- 17 progressive levels with realistic KBC-style prize ladder
- Time-limited questions for early/mid levels (30–60s) and unlimited time for final rounds
- Two lifelines: 50:50 (removes two wrong answers) and Flip (replace question)
- Animated welcome/rule/quit screens and level-up messages
- Questions, levels, comments and rules defined in `Game/Questions.py`

## Requirements

- Python 3.8+ recommended
- customtkinter

Install dependencies with pip:

```powershell
pip install customtkinter
```

Note: `customtkinter` ships its own styles and requires a working Tkinter installation (usually included with standard Python installers). On some platforms you may need to install system packages for Tk support.

## Project Structure

- `Game/` — main GUI package
	- `main.py` — entry point (starts the CTk application)
	- `WelcomeScreen.py`, `RuleScreen.py`, `GameScreen.py`, `QuitScreen.py` — UI screens
	- `Questions.py` — question bank, prize levels, comments and rules text
- `README.md` — this file

## How to run (Windows PowerShell)

Open PowerShell in the project root (the folder that contains `Game`) and run:

```powershell
python -m Game.main
```

Alternatively, run the script directly:

```powershell
python Game\main.py
```

The game opens a window. Enter your name on the welcome screen and click START GAME.

## Gameplay summary

- Answer the question by clicking an option.
- Correct answers advance you to the next level and update prize/won money.
- A wrong answer or a timer expiry ends the game and you take the last won amount.
- Use lifelines once per game: 50:50 disables two wrong options; Flip replaces the current question.
- You can Quit during the game to take the current quit money.

## Customizing questions

Edit `Game/Questions.py` to add, remove or change questions, updating the `questions` list. Each question entry follows the format:

```python
# [question text, optionA, optionB, optionC, optionD, correct_answer]
```

Be careful to keep the number of levels consistent with the `levels` list if you change total questions.

## Contribution

PRs are welcome. Small improvements that help usability (packaging, installer, tests, more questions) are especially appreciated.

## License

Include your preferred license here.
