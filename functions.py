from tkinter import messagebox
import maliang as ml
import maliang.animation as animation
import random
import sys
import os

from data import *

__all__ = [
    "get_exit_ask",
    "get_pick",
    "get_pick_people",
    "get_pick_card",
    "resource_path",
]


def resource_path(relative_path):
    """Get the path to the resource file"""
    if hasattr(sys, '_MEIPASS'):
        # Temporary catalogue after packing
        base_path = sys._MEIPASS
    else:
        # Project root directory of the development environment
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def get_exit_ask(root_window):
    root_win = root_window

    def exit_ask():
        if messagebox.askyesno("退出", "您确定要退出软件吗？"):
            root_win.destroy()

    return exit_ask


side_left = True
running = False


def get_pick(root_window, sub_cav_1: ml.Canvas, sub_cav_2: ml.Canvas):
    sub_cavs = [sub_cav_1, sub_cav_2]

    def end():
        global running
        running = False

    def pick_people(i):
        global side_left, running
        if not running:
            if i == 0 and not side_left:
                running = True
                side_left = True
                animation.MoveTkWidget(sub_cavs[0], (720, 0), 250, controller=animation.smooth, fps=120,
                                       end=end).start()
                animation.MoveTkWidget(sub_cavs[1], (720, 0), 250, controller=animation.smooth, fps=120,
                                       end=end).start()
            elif i == 1 and side_left:
                running = True
                side_left = False
                animation.MoveTkWidget(sub_cavs[0], (-720, 0), 250, controller=animation.smooth, fps=120,
                                       end=end).start()
                animation.MoveTkWidget(sub_cavs[1], (-720, 0), 250, controller=animation.smooth, fps=120,
                                       end=end).start()

    return pick_people


def get_pick_people(root_window, sub_cav, text):
    root_win = root_window
    sub_cav = sub_cav
    text = text

    def pick_people():
        text.set(random.choice(people_list))

    return pick_people


def get_pick_card(root_window, sub_cav, text, time):
    root_win = root_window
    sub_cav = sub_cav
    text = text
    time = time

    def random_card(s, a, b):
        lst = s * 5 + a * 100 + b * 895
        return random.choice(lst)

    def pick_card():
        if time == 0:
            text.set(random_card(s_char, a_char, b_char))

    return pick_card
