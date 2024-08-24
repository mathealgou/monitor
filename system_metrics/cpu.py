import wmi
import threading
import time
import pythoncom

stop_event = threading.Event()


async def setup_get_cpu_usage_async():
    # _get_cpu_usage_async()
    global cpu_usage
    cpu_usage = 0
    threading.Thread(target=_get_cpu_usage_async).start()


def _get_cpu_usage_async():
    global cpu_usage
    pythoncom.CoInitialize()
    c = wmi.WMI()
    while not stop_event.is_set():
        cpu_usage = c.Win32_PerfFormattedData_PerfOS_Processor(name="_Total")[
            0].PercentProcessorTime
        time.sleep(0.1)


def get_cpu_usage():
    return float(cpu_usage)


def stop_get_cpu_usage():
    stop_event.set()
