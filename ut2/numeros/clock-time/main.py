def run(hours: int, minutes: int, seconds: int) -> float:
    _1HOUR_TO_MINUTES = 60
    _1MINUTE_TO_SECONDS = 60
    _1SECOND_TO_MILISECONDS = 1000
    minutes_left = hours * _1HOUR_TO_MINUTES
    seconds_left = (minutes + minutes_left) * _1MINUTE_TO_SECONDS
    time_since_midnight = (seconds_left + seconds) * _1SECOND_TO_MILISECONDS
    return time_since_midnight


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
