def gen_sq(n: int):
    nums = (num**2 for num in range(n))
    return nums


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(gen_sq)
