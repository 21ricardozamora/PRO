def run(player1: str, player2: str) -> int:
    player1 = player1.lower()
    player2 = player2.lower()
    if player1 == 'rock' and player2 == 'scissors':
        winner = 1
    elif player1 == 'rock' and player2 == 'rock':
        winner = 0
    else:
        player1 == 'scissors' and player2 == 'rock'
        winner = 2
    if player1 == 'paper' and player2 == 'rock':
        winner = 1
    elif player1 == 'paper' and player2 == 'paper':
        winner = 0
    else:
        player1 == 'rock' and player2 == 'paper'
        winner = 2

    if player1 == 'scissors' and player2 == 'paper':
        winner = 1
    elif player1 == 'scissors' and player2 == 'scissors':
        winner = 0
    else:
        if player1 == 'paper' and player2 == 'scissors':
            winner = 2

    return winner


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
