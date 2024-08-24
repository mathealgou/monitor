import tkinter as tk
import signal
from .utils import get_geometry
from .custom_widgets import Clock, Menu
from .consts import BG_COLOR, TEXT_COLOR, FONT, FONT_SMALL, ACCENT_COLOR
import numpy as np

cpu_text = None

memory_text = None

gpu_text = None

audio_bars = None


class Label(tk.Label):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self.config(bg=BG_COLOR, fg=TEXT_COLOR, font=FONT)


def setup_screen():
    root = tk.Tk()
    root.title("System Metrics")
    root.overrideredirect(True)
    root.geometry(get_geometry())
    root.update_idletasks()

    # make full screen
    root.config(bg=BG_COLOR)
    root.resizable(False, False)

    menu = Menu(root)
    root.config(menu=menu)

    clock = Clock(root)
    clock.pack(anchor="ne")

    global cpu_text, memory_text, gpu_text, audio_bars
    cpu_text = tk.StringVar()
    memory_text = tk.StringVar()
    gpu_text = tk.StringVar()

    cpu_label = Label(root, textvariable=cpu_text,
                      bg=BG_COLOR, fg=TEXT_COLOR)
    cpu_label.pack()
    memory_label = Label(
        root, textvariable=memory_text, bg=BG_COLOR, fg=TEXT_COLOR)
    memory_label.pack()
    gpu_label = Label(root, textvariable=gpu_text,
                      bg=BG_COLOR, fg=TEXT_COLOR)
    gpu_label.pack()
    audio_bars = tk.Canvas(
        root,
        bg=BG_COLOR,  width=400, height=200,
        highlightbackground="white",  # Set the border color to white
        highlightthickness=2, bd=20)
    audio_bars.pack(pady=100)

    # make the window appear on top of all other windows
    root.attributes("-topmost", True)

    # emmit a signal when the window is closed, so the program can stop
    # (this is listened in the main.py file)
    root.protocol("WM_DELETE_WINDOW",
                  lambda: signal.raise_signal(signal.SIGINT))

    root.update()
    return root


# add description to functions


class Data():
    def __init__(self, cpu_usage: float = None, memory_usage: float = None, gpu_usage: float = None, audio_levels: np.array = None):
        self.cpu_usage = cpu_usage
        self.memory_usage = memory_usage
        self.gpu_usage = gpu_usage
        self.audio_levels = audio_levels


def draw(data: Data, root: tk.Tk):
    """
        Draw the system metrics on the screen
    """
    if data.cpu_usage is None:
        data.cpu_usage = 0
    if data.memory_usage is None:
        data.memory_usage = 0
    if data.gpu_usage is None:
        data.gpu_usage = 0
    cpu_text.set(f"CPU: {data.cpu_usage:.2f}%")
    memory_text.set(f"Memory: {data.memory_usage:.2f}%")
    gpu_text.set(f"GPU: {data.gpu_usage:.2f}%")

    audio_bars.delete("all")
    if data.audio_levels is None:
        return

    for i, level in enumerate(data.audio_levels):
        top_pad = 40
        multiplier = 100
        height = 20
        middle = audio_bars.winfo_width() / 2
        x0 = (middle - level * multiplier)
        y0 = (10 + i * height) + top_pad
        x1 = (middle + level * multiplier)
        y1 = (height + i * height) + top_pad

        outline = None if level < 0.5 else ACCENT_COLOR

        audio_bars.create_rectangle(
            x0, y0, x1, y1, fill=TEXT_COLOR, outline=outline)

    average = np.mean(data.audio_levels)
    audio_db = 20 * np.log10(average)

    audio_bars_text_color = ACCENT_COLOR if audio_db > 0 else TEXT_COLOR
    audio_bars.create_text(
        20, 20, text=f"{audio_db:.2f} dB", fill=audio_bars_text_color, font=FONT_SMALL, anchor="nw", justify="left")
    root.update()
    root.update_idletasks()
