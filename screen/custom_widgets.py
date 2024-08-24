import tkinter as tk
from tkinter import filedialog
import time
import math
from .consts import BG_COLOR, TEXT_COLOR,  FONT_SMALL, FONT_VERY_SMALL
from configs import load_config, save_config, DEFAULT_CONFIG


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
            self.master.update()
            self.master.update_idletasks()
            self.master.quit()
            self.master.destroy()
        except:
            pass

    def change_background(self):
        print("Change background")
        dialog = filedialog.askopenfilename(
            initialdir="/", title="Select file", filetypes=(("png files", "*.png"), ("all files", "*.*")))
        if dialog:
            # get the sibling widgets
            siblings = self.master.winfo_children()
            background = None
            for sibling in siblings:
                if isinstance(sibling, BackgroundImage):
                    background = sibling
                    break
            if background:
                background.set_image(tk.PhotoImage(file=dialog))

    def create_menu_items(self):
        menu_items = [
            ("Change Background", self.change_background),
            ("Quit", self.quit),
        ]

        for text, command in menu_items:
            button = tk.Button(
                self.menu_frame, text=text, command=command, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT_VERY_SMALL, )
            button.pack(pady=5, anchor="w")


class BackgroundImage(tk.Label):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        image = kw.get("image")
        if not image:
            config = load_config()
            image = config.get("background_image")
            if image:
                image = tk.PhotoImage(file=image)
            else:
                image = None
        self.image = image
        if self.image:
            self.set_image(self.image)
        self.config(bg=BG_COLOR)

        self.place(x=0, y=0, relwidth=1, relheight=1)
        self.lower()

    def set_image(self, image: tk.PhotoImage):
        # set the image to be the same size as the window
        window_width = self.master.winfo_width()
        window_height = self.master.winfo_height()
        image_width = image.width()
        image_height = image.height()
        self.image = image
        if image_width < window_width:
            self.image = self.image.zoom(
                math.ceil(window_width / image_width), math.ceil(window_height / image_height))
        if image_height < window_height:
            self.image = self.image.zoom(
                math.ceil(window_width / image_width), math.ceil(window_height / image_height))

        print("🐍 File: screen/custom_widgets.py | Line: 120 | set_image ~ self.image", self.image)
        self.config(image=self.image)

        # print the file path to the console
        print("name\n\n", self.image.name)
        print("🐍 File: screen/custom_widgets.py | Line: 125 | set_image ~ image.cget",
              image.cget("file"))
        save_config("background_image", image.cget("file"))
