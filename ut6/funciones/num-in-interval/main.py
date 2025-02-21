def in_range(number, upper_limit, lower_limit, /):
    valid_number = True
    if number > lower_limit or number < upper_limit:
        valid_number = False
    return valid_number


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(in_range)
