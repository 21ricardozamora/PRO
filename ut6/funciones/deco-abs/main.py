def fabs(func):
    def wrapper(value1, value2):
        value1 = abs(value1)
        value2 = abs(value2)
        result = func(value1, value2)
        return result

    return wrapper


@fabs
def run(a, b):
    return (a, b)


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
