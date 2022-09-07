import time

def countdown(seconds):
    while seconds:
        print(seconds)
        seconds -= 1
        time.sleep(1)

    print('Countdown is finished')


countdown(int(input('Countdown (in seconds): ')))