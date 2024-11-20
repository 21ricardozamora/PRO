def run(x1: int, x2: int) -> tuple:
    fmin = 1
    x1 = abs(x1)
    x2 = abs(x2)
    if x1 > x2:
        xbigger = x1
    else:
        xbigger = x2
    for num in range(1, xbigger):
        if x1 * num == x2 * num:
            result = (x1 * num) or (x2 * num)
            xmin = result
            break
    fmin = xmin**2 - (6 * xmin) + 6
    return xmin, fmin


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
