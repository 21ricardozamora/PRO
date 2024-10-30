def run(x: int, n: int) -> int:
    mult_count = 0
    p = 1
    while mult_count <= n - 1:
        p = p * x
        mult_count += 1
    return p


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
