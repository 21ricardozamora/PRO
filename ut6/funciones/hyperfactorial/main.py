def hyperfactorial(n: int) -> int:
    value = 0
    for num in range(n, 1, -1):
        value += n ** (num + 1)
    return value

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(hyperfactorial)
