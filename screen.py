import os
import tkinter as tk
import signal

# add description to functions


class Data():
    def __init__(self, cpu_usage: float, memory_usage: float, gpu_usage: float):
        self.cpu_usage = cpu_usage
        self.memory_usage = memory_usage
        self.gpu_usage = gpu_usage


cpu_text = None

memory_text = None

gpu_text = None


def setup_screen():
    root = tk.Tk()
    root.title("System Metrics")
    root.geometry("300x200")
    root.resizable(False, False)
    global cpu_text, memory_text, gpu_text
    cpu_text = tk.StringVar()
    memory_text = tk.StringVar()
    gpu_text = tk.StringVar()

    cpu_label = tk.Label(root, textvariable=cpu_text)
    cpu_label.pack()
    memory_label = tk.Label(root, textvariable=memory_text)
    memory_label.pack()
    gpu_label = tk.Label(root, textvariable=gpu_text)
    gpu_label.pack()
    # make the window appear on top of all other windows
    root.attributes("-topmost", True)

    # emmit a signal when the window is closed, so the program can stop
    # (this is listened in the main.py file)
    root.protocol("WM_DELETE_WINDOW",
                  lambda: signal.raise_signal(signal.SIGINT))

    return root


def draw(data: Data, root: tk.Tk):
    """
        Draw the system metrics on the screen
    """
    cpu_text.set(f"CPU: {data.cpu_usage:.2f}%")
    memory_text.set(f"Memory: {data.memory_usage:.2f}%")
    gpu_text.set(f"GPU: {data.gpu_usage:.2f}%")
    root.update()
    root.update_idletasks()
