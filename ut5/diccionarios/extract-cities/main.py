def run(cinfo: str) -> dict:
    cinfo_split = cinfo.split(';')
    cities = {}
    city = ''
    population = 0
    for item in cinfo_split:
        index_city = item.split(':')
        city = index_city[0]
        population = int(index_city[1])
        cities[city] = population

    return cities


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
