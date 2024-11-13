def run(target_number: int) -> None:
    attepms = 0
    your_number = int(input('Introduzca número: '))
    while target_number:
        if your_number < target_number:
            print('Mayor')
            your_number = int(input('Introduzca número: '))
            attepms += 1
            continue
        elif your_number > target_number:
            print('Menor')
            your_number = int(input('Introduzca número: '))
            attepms += 1
            continue
        else:
            attepms += 1
            print(f'Enhorabuena has encontrado el número en {attepms} intentos')
            break


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
