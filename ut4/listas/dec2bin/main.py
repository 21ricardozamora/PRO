def run(n: int) -> str:
    result = []
    bin_repr = ''
    if n == 0:
        bin_repr = '0'
    else:
        while n > 0:
            result.append(str(n % 2))
            n //= 2
            bin_repr = ''.join(result[::-1])
    return bin_repr


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
