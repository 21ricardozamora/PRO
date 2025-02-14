def gen_sq(n: int):
    for i in range(n):
        num = i**2
        yield num


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(gen_sq)
