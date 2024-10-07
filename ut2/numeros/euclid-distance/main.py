def run(x1: float, y1: float, x2: float, y2: float) -> float:
    first_point = (x2 - x1) ** 2
    second_point = (y2 - y1) ** 2
    distance = (first_point + second_point) ** (1 / 2)
    return distance


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
