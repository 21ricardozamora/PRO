def order_by_age(people: list) -> list:
    sorted_people = sorted(people, key=lambda p: p['age'])
    return sorted_people


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(order_by_age)
