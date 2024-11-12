def run(target_x: int, target_y: int) -> int:
    horse_x = 0
    horse_y = 0
    movements = 0
    incorrect_possition = -1
    for move_x in range(target_x):
        if horse_y >= target_y:
            movements = incorrect_possition
            break
        horse_x += 2
        horse_y += 1
        movements += 1
        if horse_x >= target_x:
            break
        else:
            for move_y in range(target_y):
                horse_y += 2
                horse_x += 1
                movements += 1
                if horse_y <= target_y:
                    break
                else:
                    movements = incorrect_possition
                    break
    return movements


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
