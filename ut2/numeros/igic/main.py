def run(price_with_igic: float, igic: float) -> float:
    percentage_igic = 1 + (igic / 100)  # tengo que sumar 1 al número obtenido
    clean_price = round(price_with_igic / percentage_igic, 2)
    return clean_price


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
