def sort(asc=True):
    def decorator(func):
        def wrapper(*args):
            return sorted(func(*args), reverse=not asc)

        return wrapper

    return decorator


@sort(asc=False)
def run(values: list) -> list:
    return [v for v in values if v % 2 == 0]


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
