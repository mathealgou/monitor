import tkinter as tk
import time
from .consts import BG_COLOR, TEXT_COLOR,  FONT_SMALL, FONT_VERY_SMALL


class Clock(tk.Label):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self.config(bg=BG_COLOR, fg=TEXT_COLOR, font=FONT_SMALL)
        self.after(1000, self.update_time)

    def get_time(self):
        return time.strftime("%H:%M:%S")

    def update_time(self):
        self.config(text=self.get_time())
        self.after(1000, self.update_time)


class Menu(tk.Frame):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self.open = False
        self.config(bg=BG_COLOR)
        self.place(x=0, y=0)

        self.menu_button = tk.Button(
            self, text="Menu", command=self.toggle_menu, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT_SMALL, anchor="nw")
        self.menu_button.pack(anchor="nw")
        self.config(width=self.menu_button.winfo_width())

        self.menu_frame = tk.Frame(self, bg=BG_COLOR)
        self.menu_frame.pack()
        self.menu_frame.pack_forget()

        self.create_menu_items()

    def toggle_menu(self):
        if self.open:
            self.menu_frame.pack_forget()
            self.open = False
        else:
            self.menu_frame.config(bg=BG_COLOR)
            self.menu_frame.pack()
            self.open = True

    def quit(self):
        try:
            self.master.destroy()
        except:
            pass

    def create_menu_items(self):
        menu_items = [
            ("Quit", self.quit),
        ]

        for text, command in menu_items:
            button = tk.Button(
                self.menu_frame, text=text, command=command, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT_VERY_SMALL, )
            button.pack(pady=5, anchor="w")
