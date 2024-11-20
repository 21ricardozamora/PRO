def run(limit: int) -> None:
    mult_3_sum = 0
    for num in range(limit):
        if num % 3 == 0:
            mult_3_sum += num
            print(num, end=' ')
        if mult_3_sum >= limit:
            break


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
