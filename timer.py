from turtle import Turtle
import time

FONT = ("Courier", 24, "normal")
ALIGNMENT = "Center"


class CountdownTimer(Turtle):
    def __init__(self, timer_set):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(x=200, y=250)
        self.reset_timer(timer_set)

    def increment_time(self):
        self.time_elapsed = time.time() - self.timestart
        self.time_remaining = max(self.timer_set - self.time_elapsed,0)
        if self.time_remaining == 0:
            self.timer_over = True
        self.show_timer()

    def escape_pressed(self):
        self.timer_over = True
        self.show_timer()

    def print_time_to_console(self, level_x):
        print(f"Level {level_x}: Time Remaining {self.strTimer}")

    def reset_timer(self, timer_set):
        self.timer_set = timer_set
        self.timer_over = False
        self.timestart = time.time()
        self.time_elapsed = self.timestart - self.timestart
        print(self.timer_set)
        print(self.time_elapsed)
        self.time_remaining = max(self.timer_set - self.time_elapsed, 0)
        self.show_timer()

    def show_timer(self):
        self.clear()
        self.strTimer = time.strftime('%H:%M:%S', time.gmtime(self.time_remaining))
        #"00:{:.1f}".format(self.time_remaining)
        self.write(arg=self.strTimer, align=ALIGNMENT, font=FONT)
