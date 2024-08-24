from screeninfo import get_monitors


def get_geometry(monitor_index: int = 1):
    monitor = get_monitors()[monitor_index]
    return f"{monitor.width}x{monitor.height}+{monitor.x}+{monitor.y}"
