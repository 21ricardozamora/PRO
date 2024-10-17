def run(can_fly: bool, is_human: bool, has_mask: bool) -> str:
    if can_fly:
        if is_human:
            if has_mask:
                character = 'Ironman'
            else:
                character = 'Captain Marvel'
        elif has_mask:
            character = 'Ronan Accuser'
        else:
            character = 'Vision'
    else:
        if is_human:
            if has_mask:
                character = 'Spiderman'
            else:
                character = 'Hulk'
        elif has_mask:
            character = 'Black Bolt'
        else:
            character = 'Thanos'

    return character


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
