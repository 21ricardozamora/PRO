def run(n: int) -> int:
    positive_number = abs(n)
    lenght_n = len(str(positive_number))
    result = n * 5 ** (lenght_n)
    return result


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
