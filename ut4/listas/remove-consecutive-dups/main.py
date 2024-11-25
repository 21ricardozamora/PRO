def run(items: list) -> list:
    result = []
    index = 0
    for item in items:
        if item not in result:
            result.append(item)
            index += 1

    return result


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
