# Speed typing test

import tkinter as tk
from turtle import Screen
from functools import partial
from timer import CountdownTimer
from typer import Typewriter, Prompt
import time


def _onkeypress(self, fun, key=None):
    if fun is None:
        if key is None:
            self.cv.unbind("<KeyPress>", None)
        else:
            self.cv.unbind("<KeyPress-%s>" % key, None)
    elif key is None:
        def eventfun(event):
            fun(event.char)
        self.cv.bind("<KeyPress>", eventfun)
    else:
        def eventfun(event):
            fun()
        self.cv.bind("<KeyPress-%s>" % key, eventfun)

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Speed Typing Test")
screen.tracer(0)

screen.listen()

typewriter = Typewriter()
prompt = Prompt()

screen._onkeypress = partial(_onkeypress, screen)
screen.onkeypress(typewriter.record_keypress)

countdown_timer = CountdownTimer(5)

speed_test_on = True
while speed_test_on:
    screen.update()

    # Update countdown timer
    countdown_timer.increment_time()

    # Detect whether timer elapsed
    if countdown_timer.timer_over:
        prompt.clear_prompt()
        typewriter.game_over()
        speed_test_on = False

screen.exitonclick()