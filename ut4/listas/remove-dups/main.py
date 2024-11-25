def run(nums_dups: list) -> list:
    nums_unique = []
    for char in nums_dups:
        if char not in nums_unique:
            nums_unique.append(char)
    return nums_unique


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
