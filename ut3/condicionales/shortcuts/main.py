def run(key1: str, key2: str, key3: str) -> str:
    SHORTCUTS = (
        'open terminal',
        'lock screen',
        'show desktop',
        'run console',
        'close window',
        'log out',
    )
    KEYS = 'CTRL', 'ALT', 'DEL', 'T', 'L', 'D', 'Q', 'F2'
    match SHORTCUTS.lower():
        case 'open terminal':
            if key1 == 'CTRL' and key2 == 'ALT' and key3 == 'T':
                action = 'Open Terminal'
    return action


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
