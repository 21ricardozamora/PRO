def run():
    complete_name = input('¿Su nombre? ')
    complete_name = complete_name.title()
    while complete_name:
        if complete_name != complete_name.title():
            print('Error. Debe escribirlo correctamente')
            continue
        else:
            break


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
