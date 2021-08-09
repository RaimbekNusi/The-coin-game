"Raimbek Nussipkhozhin, NFU892, 11313819, Jeffrey Long"
player1Wins = 0
player2Wins = 0
n = 1
while player1Wins != 3 and player2Wins != 3:
    for round in range(0,n):
        round = round + 1
    print("Round " + str(round))
    n = n + 1
    player1 = input("In which hand to hide the coin? (l or r): ")
    player2 = input("In which hand is the coin? (l or r): ")
    if player2 == player1:
        print("You guessed right!")
        player2Wins = player2Wins + 1
    else:
        print("You guessed wrong :(")
        player1Wins = player1Wins + 1
if player1Wins == 3:
    print("Player 1 WINS!")
elif player2Wins == 3:
    print("Player 2 WINS!")
