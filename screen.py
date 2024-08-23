import os

# add description to functions


def draw(cpu_usage: float, memory_usage: float, gpu_usage: float):
    """
        Draw the system metrics on the screen
    """
    clear()
    print(f"CPU Usage: {cpu_usage:.2f}%")
    print(f"Memory Usage: {memory_usage:.2f}%")
    print(f"GPU Usage: {gpu_usage:.2f}%")


def clear():
    """
        Clear the screen
    """
    os.system('cls' if os.name == 'nt' else 'clear')
