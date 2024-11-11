def run(target_x: int, target_y: int) -> int:
    horse_x = 0
    horse_y = 0
    movements = 0
    target_possition = 0
    for move_x in range(target_x):
        horse_x += 2
        horse_y += 1
        if horse_x - target_x == target_possition:
            break
        else:
            for move_y in range(target_y):
                horse_x += 1
                horse_y += 2
                if (horse_y - target_y) == target_possition:
                    break
                else:
                    continue
        movements += 1

    return movements


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
