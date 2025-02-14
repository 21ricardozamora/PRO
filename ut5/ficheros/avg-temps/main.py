def run(input_path: str, output_path: str) -> None:
    with open(input_path) as f:
        avg_temps = open(output_path, 'w')
        for month in f:
            temps = [int(temp) for temp in month.strip().split(',')]
            size = len(temps)
            avg = sum(temps) / size
            avg_temps.write(f'{avg:.2f}\n')
        avg_temps.close()


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
