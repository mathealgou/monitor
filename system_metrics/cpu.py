import wmi

c = wmi.WMI()


def get_cpu_usage():
    cpu_usage = c.Win32_PerfFormattedData_PerfOS_Processor(name="_Total")[
        0].PercentProcessorTime
    return float(cpu_usage)
