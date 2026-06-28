import time


def spin():
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        return