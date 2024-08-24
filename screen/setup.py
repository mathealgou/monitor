import tkinter as tk
import signal
from .utils import get_geometry
from .custom_widgets import Clock
from .consts import BG_COLOR, TEXT_COLOR, FONT
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

    audio_bars = tk.Canvas(root, bg=BG_COLOR, highlightthickness=0)
    audio_bars.pack()

    # make the window appear on top of all other windows
    root.attributes("-topmost", True)

    # emmit a signal when the window is closed, so the program can stop
    # (this is listened in the main.py file)
    root.protocol("WM_DELETE_WINDOW",
                  lambda: signal.raise_signal(signal.SIGINT))

    return root


# add description to functions


class Data():
    def __init__(self, cpu_usage: float, memory_usage: float, gpu_usage: float, audio_levels: np.array = None):
        self.cpu_usage = cpu_usage
        self.memory_usage = memory_usage
        self.gpu_usage = gpu_usage
        self.audio_levels = audio_levels


def draw(data: Data, root: tk.Tk):
    """
        Draw the system metrics on the screen
    """
    cpu_text.set(f"CPU: {data.cpu_usage:.2f}%")
    memory_text.set(f"Memory: {data.memory_usage:.2f}%")
    gpu_text.set(f"GPU: {data.gpu_usage:.2f}%")

    audio_bars.delete("all")
    for i, level in enumerate(data.audio_levels):
        x0 = 10
        y0 = 10 + i * 20
        x1 = 10 + level * 200
        y1 = 20 + i * 20
        audio_bars.create_rectangle(x0, y0, x1, y1, fill=TEXT_COLOR)

    root.update()
    root.update_idletasks()
