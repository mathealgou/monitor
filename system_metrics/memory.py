import wmi

c = wmi.WMI()


def get_memory_usage():
    os_info = c.Win32_OperatingSystem()[0]
    total_memory = float(os_info.TotalVisibleMemorySize)
    free_memory = float(os_info.FreePhysicalMemory)
    memory_usage = (total_memory - free_memory) / total_memory * 100
    return memory_usage
