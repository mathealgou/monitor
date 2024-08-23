import tkinter as tk
import signal
from .utils import get_geometry
from .custom_widgets import Clock
from .consts import BG_COLOR, TEXT_COLOR, FONT

cpu_text = None

memory_text = None

gpu_text = None


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
    global cpu_text, memory_text, gpu_text
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
    # make the window appear on top of all other windows
    root.attributes("-topmost", True)

    # emmit a signal when the window is closed, so the program can stop
    # (this is listened in the main.py file)
    root.protocol("WM_DELETE_WINDOW",
                  lambda: signal.raise_signal(signal.SIGINT))

    return root


# add description to functions


class Data():
    def __init__(self, cpu_usage: float, memory_usage: float, gpu_usage: float):
        self.cpu_usage = cpu_usage
        self.memory_usage = memory_usage
        self.gpu_usage = gpu_usage


def draw(data: Data, root: tk.Tk):
    """
        Draw the system metrics on the screen
    """
    cpu_text.set(f"CPU: {data.cpu_usage:.2f}%")
    memory_text.set(f"Memory: {data.memory_usage:.2f}%")
    gpu_text.set(f"GPU: {data.gpu_usage:.2f}%")
    root.update()
    root.update_idletasks()
