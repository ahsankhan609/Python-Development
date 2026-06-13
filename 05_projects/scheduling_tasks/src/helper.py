# https://youtu.be/FCPBG6NqMmQ
# https://youtu.be/4n2fC97MNac

import time

import helper
import schedule


def task() -> None:
    """this function will print the current time."""
    print(f'Doing task ... {helper.get_time()}')


schedule.every(5).seconds.do(task())
schedule.every(5).minutes.do(task())
schedule.every(5).hours.do(task())
schedule.every(5).days.do(task())
schedule.every(5).weeks.do(task())

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(1)
