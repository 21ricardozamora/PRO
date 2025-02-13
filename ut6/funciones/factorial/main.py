def factorial(n):
    if n == 0:
        return 1
    if n < 0:
        return None
    for num in range(n, 1, -1):
        x = n * (num + 1)
    return x


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(factorial)
