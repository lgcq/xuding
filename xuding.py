import time

def pomodoro_timer(minutes):
    """Starts a timer for the specified number of minutes"""
    seconds = minutes * 60
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = "{:02d}:{:02d}".format(mins, secs)
        print("Remaining time:", timer, end="\r")
        time.sleep(1)
        seconds -= 1
    print("Time's up!")

if __name__ == "__main__":
    pomodoro_timer(25)  # Set timer for 25 minutes
