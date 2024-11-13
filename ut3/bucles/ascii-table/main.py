def run(start_code: int, end_code: int) -> None:
    counter = 0
    for char in range(start_code, end_code + 1):
        if len(str(char)) < 3:
            print(f'0{char} {chr(char)}', end='   ')
        else:
            print(f'{char} {chr(char)}', end='   ')
        counter += 1
        if counter == 5:
            print()
            counter = 0


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
