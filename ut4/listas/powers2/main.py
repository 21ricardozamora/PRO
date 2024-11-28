def run(n: int) -> list:
    num = 2
    powers2 = [num**i for i in range(n + 1)]
    return powers2


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
