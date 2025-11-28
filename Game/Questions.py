questions = [

    # 1
    [
        "What is the output?\n\nx = {0: 'zero', False: 'false'}\nprint(len(x))",
        "1",
        "2",
        "0",
        "Error",
        "1",
    ],

    # 2
    [
        "What happens?\n\nx = [1, 2, 3]\ny = x\ny += [4]\nprint(x)",
        "[1, 2, 3]",
        "[1, 2, 3, 4]",
        "[4]",
        "Error",
        "[1, 2, 3, 4]",
    ],

    # 3
    [
        "Predict the output:\n\nx = ([],)\nx[0].append(5)\nprint(x)",
        "([],)",
        "([5],)",
        "(5,)",
        "Error",
        "([5],)",
    ],

    # 4
    [
        "What is printed?\n\na = {1,2,3}\nb = {3,4,5}\nprint(a & b)",
        "{3}",
        "{1,2,3,4,5}",
        "{ }",
        "Error",
        "{3}",
    ],

    # 5
    [
        "Evaluate:\n\nprint(bool('False'))",
        "False",
        "True",
        "None",
        "Error",
        "True",
    ],

    # 6
    [
        "What is the output?\n\nx = 'abc'\nx += 'd'\nprint(x)",
        "abc",
        "abcd",
        "['a','b','c','d']",
        "Error",
        "abcd",
    ],

    # 7
    [
        "What happens?\n\nx = [1,2,3]\nprint(x * 0)",
        "[]",
        "[1,2,3,1,2,3]",
        "0",
        "Error",
        "[]",
    ],

    # 8
    [
        "Predict result:\n\nx = {1,2,3}\nx.add(3)\nprint(x)",
        "{1,2}",
        "{3}",
        "{1,2,3}",
        "Error",
        "{1,2,3}",
    ],

    # 9
    [
        "What is printed?\n\ndef foo(a, b): return a is b\nprint(foo(256, 256))",
        "True",
        "False",
        "Error",
        "None",
        "True",
    ],

    # 10
    [
        "Output?\n\ndef bar(): pass\nprint(bar())",
        "None",
        "pass",
        "Error",
        "''",
        "None",
    ],

    # 11
    [
        "What happens?\n\nx = [1]; y = [1]\nprint(x == y, x is y)",
        "True True",
        "True False",
        "False False",
        "False True",
        "True False",
    ],

    # 12
    [
        "Output?\n\nx = (1,)\ny = (1)\nprint(type(x), type(y))",
        "<class 'tuple'> <class 'tuple'>",
        "<class 'tuple'> <class 'int'>",
        "<class 'int'> <class 'tuple'>",
        "Error",
        "<class 'tuple'> <class 'int'>",
    ],

    # 13
    [
        "Predict:\n\nprint([i for i in range(3) if i])",
        "[1,2]",
        "[0,1,2]",
        "[ ]",
        "Error",
        "[1,2]",
    ],

    # 14
    [
        "Output?\n\nx = '1'\nprint(x * 3)",
        "3",
        "'111'",
        "'3'",
        "Error",
        "'111'",
    ],

    # 15
    [
        "What prints?\n\nx = [1,2,3]\nprint(x[::-1])",
        "[3,2,1]",
        "[1,2,3]",
        "Error",
        "None",
        "[3,2,1]",
    ],

    # 16
    [
        "Result?\n\nx = {1:'a', 2:'b'}\nprint(x.get(3, 'default'))",
        "None",
        "default",
        "Error",
        "3",
        "default",
    ],

    # 17
    [
        "What is printed?\n\nprint(True + True + False)",
        "2",
        "1",
        "3",
        "Error",
        "2",
    ],

    # 18
    [
        "What happens?\n\nx = [0,1,2,3]\ndel x[1:3]\nprint(x)",
        "[0,3]",
        "[1,2]",
        "[0,1,2,3]",
        "Error",
        "[0,3]",
    ],

    # 19
    [
        "Output?\n\ndef f(a, b): return a // b\nprint(f(-3,2))",
        "-1",
        "-2",
        "1",
        "Error",
        "-2",
    ],

    # 20
    [
        "What prints?\n\nx = [1,2,3]\nprint(list(map(lambda a: a*0, x)))",
        "[0,0,0]",
        "[1,2,3]",
        "Error",
        "[ ]",
        "[0,0,0]",
    ],

    # 21
    [
        "Predict result:\n\nx = {1,2,3}\nprint(2 in x)",
        "True",
        "False",
        "Error",
        "None",
        "True",
    ],

    # 22
    [
        "What is printed?\n\nprint(len({True:1, 1:2}))",
        "1",
        "2",
        "Error",
        "0",
        "1",
    ],

    # 23
    [
        "Output?\n\nx = 'abc'\nprint(x[1:10])",
        "'bc'",
        "'abc'",
        "''",
        "Error",
        "'bc'",
    ],

    # 24
    [
        "What prints?\n\nx = [1, [2,3]]\ny = x[:]\ny[1].append(4)\nprint(x)",
        "[1,[2,3]]",
        "[1,[2,3,4]]",
        "[1,2,3,4]",
        "Error",
        "[1,[2,3,4]]",
    ],

    # 25
    [
        "Predict the output:\n\nprint(10 > 9 > 8)",
        "True",
        "False",
        "Error",
        "None",
        "True",
    ],

    # 26
    [
        "What is printed?\n\nprint([0] * 5)",
        "[0,0,0,0,0]",
        "[0]",
        "[5]",
        "Error",
        "[0,0,0,0,0]",
    ],

    # 27
    [
        "Output?\n\ndef foo(a=[]): a.append(1); return a\nprint(foo(), foo())",
        "[1], [1]",
        "[1], [1,1]",
        "[1,1], [1,1]",
        "Error",
        "[1], [1,1]",
    ],

    # 28
    [
        "What prints?\n\nprint({i:i*i for i in range(3)})",
        "{0:0,1:1,2:4}",
        "{1:1,2:4}",
        "{}",
        "Error",
        "{0:0,1:1,2:4}",
    ],

    # 29
    [
        "Predict:\n\nx = [1,2,3]\nprint(sum(x, 10))",
        "6",
        "16",
        "Error",
        "[1,2,3,10]",
        "16",
    ],

    # 30
    [
        "Final one — what's the output?\n\ndef f(a,b,c): return a if a>b and a>c else (b if b>c else c)\nprint(f(3,7,5))",
        "3",
        "5",
        "7",
        "Error",
        "7",
    ],
    
    # 31
    [
        "What is the output?\n\nx = {1: 'a', True: 'b'}\nprint(x[1])",
        "'a'",
        "'b'",
        "KeyError",
        "None",
        "'b'",
    ],
    
    # 32
    [
        "What happens?\n\nx = [[], []]\nx[0].append(1)\nprint(x)",
        "[[1], []]",
        "[[1], [1]]",
        "[1, []]",
        "Error",
        "[[1], []]",
    ],
    
    # 33
    [
        "What is the output?\n\ndef foo(a, b=[]): b.append(a); return b\nprint(foo(1)); print(foo(2))",
        "[1], [2]",
        "[1], [1, 2]",
        "[1, 2], [1, 2]",
        "Error",
        "[1], [1, 2]",
    ],
    
    # 34
    [
        "Which statement about @staticmethod is true?",
        "It receives the instance as first argument",
        "It receives the class as first argument",
        "It receives neither class nor instance",
        "It cannot be called from the class",
        "It receives neither class nor instance",
    ],

    # 35
    [
        "What is the output?\n\nprint({i: i*i for i in range(3)}.get(5, -1))",
        "KeyError",
        "None",
        "-1",
        "5",
        "-1",
    ],

    # 36
    [
        "Which file mode truncates the file on opening?",
        "'r'",
        "'a'",
        "'w'",
        "'x'",
        "'w'",
    ],

    # 37
    [
        "What is the output?\n\nprint(list(map(lambda x: x+1, (i for i in range(3)))))",
        "[1, 2, 3]",
        "[0, 1, 2, 3]",
        "generator object",
        "Error",
        "[1, 2, 3]",
    ],

    # 38
    [
        "What does json.dumps() return?",
        "A Python dict",
        "A file object",
        "A string",
        "A list",
        "A string",
    ],

    # 39
    [
        "What is the output?\n\nx = (i for i in range(3))\nprint(sum(x)); print(sum(x))",
        "3, 3",
        "3, 0",
        "0, 0",
        "Error",
        "3, 0",
    ],

    # 40
    [
        "Which of the following correctly checks file existence using os?",
        "os.exists('file.txt')",
        "os.isfile('file.txt')",
        "os.path.exists('file.txt')",
        "os.file('file.txt')",
        "os.path.exists('file.txt')",
    ],

    # 41
    [
        "What is the output?\n\nx = [1,2,3]\nprint(x is x[:])",
        "True",
        "False",
        "None",
        "Error",
        "False",
    ],

    # 42
    [
        "Which statement is true for Python decorators?",
        "They must return None",
        "They modify the function's bytecode",
        "They wrap a function and return another function",
        "They are executed at runtime only when function is called",
        "They wrap a function and return another function",
    ],

    # 43
    [
        "What is the output?\n\nprint(type({i for i in 'abca'}))",
        "<class 'list'>",
        "<class 'set'>",
        "<class 'dict'>",
        "<class 'tuple'>",
        "<class 'set'>",
    ],

    # 44
    [
        "What happens?\n\ntry:\n    1/0\nexcept ZeroDivisionError as e:\n    print(type(e).__name__)",
        "ZeroDivisionError",
        "Exception",
        "Error",
        "TypeError",
        "ZeroDivisionError",
    ],

    # 45
    [
        "What is the output?\n\nprint({}.setdefault('x', 5))",
        "None",
        "KeyError",
        "5",
        "[]",
        "5",
    ],

    # 46
    [
        "Which of the following is TRUE about Python sets?",
        "They allow duplicate values",
        "They preserve insertion order always",
        "They support O(1) average lookup time",
        "They are mutable only at creation",
        "They support O(1) average lookup time",
    ],

    # 47
    [
        "What is the output?\n\nx = [1,2,3]\ny = x\nx = x + [4]\nprint(y)",
        "[1, 2, 3]",
        "[1, 2, 3, 4]",
        "[4]",
        "Error",
        "[1, 2, 3]",
    ],

    # 48
    [
        "Which statement about __str__() is true?",
        "It must return bytes",
        "It is called by print()",
        "It is the same as __repr__",
        "It runs on object creation",
        "It is called by print()",
    ],

    # 49
    [
        "What is the output?\n\nprint(bool([]) == False)",
        "True",
        "False",
        "None",
        "Error",
        "True",
    ],

    # 50
    [
        "Which of the following creates a shallow copy of a list?",
        "x.copy()",
        "x.clone()",
        "copy(x, deep=True)",
        "list.deepcopy(x)",
        "x.copy()",
    ],

    # 51
    [
        "What is the output?\n\ndef foo():\n    try:\n        return 'A'\n    finally:\n        return 'B'\nprint(foo())",
        "'A'",
        "'B'",
        "None",
        "Error",
        "'B'",
    ],

    # 52
    [
        "Which method reads an entire file into a list of lines?",
        "file.readlines()",
        "file.read()",
        "file.readlist()",
        "file.line()",
        "file.readlines()",
    ],

    # 53
    [
        "What is the output?\n\nprint(type((i for i in range(5))))",
        "<class 'tuple'>",
        "<class 'generator'>",
        "<class 'list'>",
        "<class 'range'>",
        "<class 'generator'>",
    ],

    # 54
    [
        "Which is NOT a valid dictionary operation?",
        "x['a'] = 10",
        "x.get('a')",
        "x.add('a')",
        "x.pop('a')",
        "x.add('a')",
    ],

    # 55
    [
        "What is the output?\n\nx = {'a':1}\ny = x\nx.update({'b':2})\nprint(y)",
        "{'a': 1}",
        "{'a': 1, 'b': 2}",
        "{}",
        "Error",
        "{'a': 1, 'b': 2}",
    ],

    # 56
    [
        "What does enumerate() return?",
        "A list of index-value pairs",
        "A tuple",
        "An iterator generating (index, value)",
        "A generator expression",
        "An iterator generating (index, value)",
    ],

    # 57
    [
        "What is the output?\n\nprint(all(i < 5 for i in [1,2,3,7]))",
        "True",
        "False",
        "Error",
        "None",
        "False",
    ],

    # 58
    [
        "Which statement is true about Python classes?",
        "Methods are stored per instance",
        "Attributes are always private",
        "Class attributes are shared across instances",
        "Instances cannot override class attributes",
        "Class attributes are shared across instances",
    ],

    # 59
    [
        "What is the output?\n\nx = [i*i for i in range(3)]\ny = (i*i for i in range(3))\nprint(sum(x), sum(y), sum(y))",
        "5 5 5",
        "5 5 0",
        "5 0 0",
        "Error",
        "5 5 0",
    ],

    # 60
    [
        "What is the output?\n\nx = {'a':1, 'b':2}\nprint(list(x.keys()))",
        "['b', 'a']",
        "['a', 'b']",
        "KeysView",
        "dict_items",
        "['a', 'b']",
    ]
]

levels = [
    "1,000",
    "2,000",
    "3,000",
    "5,000",
    "10,000",
    "20,000",
    "40,000",
    "80,000",
    "1,60,000",
    "3,20,000",
    "6,40,000",
    "12,50,000",
    "25,00,000",
    "50,00,000",
    "1,00,00,000",
    "3,00,00,000",
    "7,00,00,000",
]

Comments = [
    "🧠 You're about to unlock your brain's full power...",
    "🤯 Did you just level up mentally?",
    "🎓 Loading genius mode...",
    "🥸  Was that a big brain moment?",
    "💵 This might be your million-dollar answer!",
    "😱 Feeling the pressure yet?",
    "😈 Careful... one wrong move and it's game over!",
    "❓ Still confident?",
    "🐍 Time to flex those Python muscles...",
    "🧪 Got that logic flowing?",
    "😵 Think twice. This one's spicy!",
    "🔥 Did you feel the heat?",
    "🫥  You're dancing with danger now...",
    "😬 Still on fire or slightly crispy?",
    "😇 The code gods are watching you now...",
    "❓ Did you impress them?",
    "🤔 This question is hiding something...",
    "❓ Did you catch the trick?",
    "😲 You're one step closer to greatness...",
    "🫨  Can you taste victory yet?",
    "🤔 What you are thinking...",
    "❓ Did you guessed it right?",
    "⚠️  Warning: Brain overclocking in progress...",
    "❓ Did your neurons survive that?",
    "😷 You just entered the logic maze...",
    "❓ Did you find the exit or hit a wall?",
    "🤔 This one's trickier than it looks...",
    "🫵  Were you fooled or focused?",
    "😤 Breathe in, breathe out... and answer!",
    "🔓 Still calm or totally cracked?",
    "🫨  Python whisperers know this one...",
    "❓ Are you one of them?",
    "🤫 Okay Let's See!",
]

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