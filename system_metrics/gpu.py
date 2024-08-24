from py3nvml.py3nvml import nvmlInit, nvmlDeviceGetHandleByIndex, nvmlDeviceGetUtilizationRates, nvmlShutdown
import pyadl
import threading
import time

# Function to retrieve GPU usage for NVIDIA


def _get_nvidia_gpu_usage():
    nvmlInit()
    handle = nvmlDeviceGetHandleByIndex(0)  # Assuming a single GPU
    utilization = nvmlDeviceGetUtilizationRates(handle)
    nvmlShutdown()
    return utilization.gpu

# Function to retrieve GPU usage for AMD using rocm-smi


def _get_amd_gpu_usage():
    devices = pyadl.ADLManager.getInstance().getDevices()
    device = devices[0]  # Assuming a single GPU
    result = device.getCurrentUsage()
    return result


def _get_gpu_usage():
    try:
        return _get_nvidia_gpu_usage()
    except:
        return _get_amd_gpu_usage()


# new thread to get gpu usage every 0.1 seconds and store it in a list
async def setup_get_gpu_usage_async():
    global gpu_usage_list
    gpu_usage_list = []
    threading.Thread(target=_get_gpu_usage_async).start()


GPU_USAGE_POLL_INTERVAL = 0.1  # Seconds

# Multiplied by GPU_USAGE_POLL_INTERVAL to get the total time window
GPU_USAGE_LIST_MAX_LENGTH = 100


# used to stop the thread
stop_event = threading.Event()


def _get_gpu_usage_async():
    while not stop_event.is_set():
        if len(gpu_usage_list) > GPU_USAGE_LIST_MAX_LENGTH:
            gpu_usage_list.pop(0)
        gpu_usage_list.append(_get_gpu_usage())
        time.sleep(GPU_USAGE_POLL_INTERVAL)


# make synchronous function to get average gpu usage from the list
def get_gpu_usage():
    return sum(gpu_usage_list) / len(gpu_usage_list) if len(gpu_usage_list) > 0 else 0


def stop_get_gpu_usage():
    stop_event.set()
