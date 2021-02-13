from turtle import Turtle
import time

FONT = ("Courier", 24, "normal")
FONT_PROMPT = ("Courier", 14, "normal")
ALIGNMENT = "Center"

class Typewriter(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(x=0, y=0)
        self.script = ""
        self.word_count = 0
        self.show_word_count()

    def record_keypress(self, char):
        try:
            self.script += str(char)
        except:
            pass
        # Determine word count
        current_word_count = len(self.script.strip().split(sep=" "))
        if current_word_count > self.word_count:
            self.word_count = current_word_count
            self.show_word_count()

    def show_word_count(self):
        self.clear()
        self.write(arg=f"Word Count: {self.word_count}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.clear()
        self.write(f"GAME OVER. Final Word Count: {self.word_count}", align=ALIGNMENT, font=FONT)

class Prompt(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(x=0, y=100)
        self.clear()
        self.write("Start Typing! Type as fast as you can!!!", align=ALIGNMENT, font=FONT_PROMPT)
    def clear_prompt(self):
        self.clear()