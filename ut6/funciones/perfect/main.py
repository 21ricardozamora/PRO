def help_func(values: int):
    div_num = 0
    for value in range(1, values):
        if values % value == 0:
            div_num += value
        if div_num == values:
            break
    return div_num


def is_perfect(num: int):
    if help_func(num) == num:
        return True
    else:
        return False


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(is_perfect)
