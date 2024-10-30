def run(size: int) -> None:
    for i in range(5):
        for j in range(5):
            print('X', end=' ')
        print()


# bloque de 5x5, construir a partir de aquí

run(5)


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
