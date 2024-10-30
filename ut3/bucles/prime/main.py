def run(n: int) -> bool:
    is_prime = False
    while is_prime is False:
        if n > 1 and n / n == 1 and n / 1 == n:
            is_prime = True
        else:
            is_prime = False
    return is_prime


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
