def run(year: int) -> bool:
    if year % 4 == 0:
        is_leap_year = True
    elif year % 100 != 0:
        is_leap_year = False
    else:
        if year % 400 == 0:
            is_leap_year = True

    return is_leap_year


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
