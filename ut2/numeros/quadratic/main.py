def run(a: int, b: int, c: int) -> tuple:
    square_root = (b**2 - (4 * a * c)) ** 0.5
    denominator = 2 * a
    x1 = (-b + square_root) / denominator
    x2 = (-b - square_root) / denominator
    return x1, x2


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
