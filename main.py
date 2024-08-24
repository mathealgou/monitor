import time
from system_metrics import (setup_get_cpu_usage_async, stop_get_cpu_usage, get_cpu_usage, get_memory_usage,
                            get_gpu_usage, setup_get_gpu_usage_async, stop_get_gpu_usage)
from screen import draw, Data, setup_screen
import asyncio
import signal
import tkinter as tk
from audio import get_audio_levels

# Things needed to deal with threads and signals
stop_flag = False


def signal_handler(sig, frame):
    global stop_flag
    stop_flag = True
    print("Stopping...")


# Register the signal handler used to capture the stop command (Ctrl+C) in the terminal
signal.signal(signal.SIGINT, signal_handler)


async def main():
    await setup_get_gpu_usage_async()
    await setup_get_cpu_usage_async()
    root = setup_screen()
    try:
        while not stop_flag:
            data = Data(
                get_cpu_usage(),
                get_memory_usage(),
                get_gpu_usage(),
                audio_levels=get_audio_levels(),
            )
            draw(data, root)
    finally:
        stop_get_cpu_usage()
        stop_get_gpu_usage()


if __name__ == "__main__":
    asyncio.run(main())
