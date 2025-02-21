def extract_evens(values: list[int]) -> list:
    evens = []
    for num in values:
        if num % 2 == 0:
            evens.append(num)
    return evens


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(extract_evens)
