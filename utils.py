from time import sleep


def get_average_over_time(func, n=5, time: int = 500) -> float:
    """
    Function to get the average of a function over a certain time period
    :param func: Function to get the average of
    :param n: Number of times to call the function
    :param time: Time period in milliseconds
    """
    total = 0
    for _ in range(n):
        total += func()
        sleep(time / 1000)
    return total / n
