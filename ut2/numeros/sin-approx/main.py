def run(x: float) -> float:
    OPERATION = 180 - x
    numerator = 4 * x * OPERATION
    denominator = 40500 - x * OPERATION
    sin = numerator / denominator
    return sin


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
