import time
from system_metrics import (get_cpu_usage, get_memory_usage,
                            get_gpu_usage, setup_get_gpu_usage_async, stop_get_gpu_usage)
from screen import draw
import asyncio
import signal

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
    try:
        while not stop_flag:
            cpu_usage = get_cpu_usage()
            memory_usage = get_memory_usage()
            gpu_usage = get_gpu_usage()
            draw(cpu_usage, memory_usage, gpu_usage)
            time.sleep(.1)
    finally:
        stop_get_gpu_usage()


if __name__ == "__main__":
    asyncio.run(main())
