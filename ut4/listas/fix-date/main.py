def run(input_date: str, base_year: int) -> str:
    date_separator = input_date.split('/')
    day = date_separator[1]
    month = date_separator[0]
    year = int(date_separator[2]) + base_year
    output_date = f'{day:0>2s}-{month:0>2s}-{str(year):0>4s}'
    return output_date


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
