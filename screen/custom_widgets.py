import tkinter as tk
import time
from .consts import BG_COLOR, TEXT_COLOR, FONT


class Clock(tk.Label):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self.config(bg=BG_COLOR, fg=TEXT_COLOR, font=FONT)
        self.after(1000, self.update_time)

    def get_time(self):
        return time.strftime("%H:%M:%S")

    def update_time(self):
        self.config(text=self.get_time())
        self.after(1000, self.update_time)
