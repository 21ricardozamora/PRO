def run(pdata: dict) -> dict:
    total_population = sum(pdata.values())
    division = 100 / total_population
    avg_data = {}
    for city in pdata:
        population_percentage = pdata.get(city) * division
        avg_data[city] = round(population_percentage, 3)
    return avg_data


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
