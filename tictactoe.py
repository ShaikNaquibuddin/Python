# ======================================================================================================
# win function

def win_game(game):

    def same_all(l):
        if l.count(l[0]) == len(l) and l[0] != 0:
            return True, l[0]
        
        return False, 0

    # horizontally
    for row in game:
        won, pno = same_all(row)
        if won:
            print(f"Player {pno} won the game horizontally")
            return True

    # vertically
    for i in range(len(game)):
        check  = []
        for j in range(len(game)):
            check.append(game[j][i])

        won, pno = same_all(check)
        if won:
            print(f"Player {pno} won the game vertically")
            return True

    # diagonally
    ld, rd = [], []
    n = len(game)-1
    for i in range(n+1):
        ld.append(game[i][n-i])
        rd.append(game[i][i])

    won, pno = same_all(ld)
    if won:
        print(f"Player {pno} won the game diagonally")
        return True
    won1, pno1 = same_all(rd)
    if won1:
        print(f"Player {pno1} won the game diagonally")
        return True

    return False
# ======================================================================================================
def board(game_map, player = 0, row = 0, column = 0,just_display = False):
    try:
        if game_map[row][column] != 0:
            print("Choose another position")
            return game_map, False
    
        if not just_display:
            game_map[row][column] = player

        s = "".join(["  "+str(i) for i in range(len(game_map))])
        print(" "+s)
        for count, row in enumerate(game_map):
            print(count, row)
        return game_map, True
    
    except IndexError as e:
        print("Error : Did you enter row/column as 0, 1 or 2\n",e )
        return game_map,False
    
    except Exception as e:
        print(e)
        return game_map,False
# ==================================================================

# main code
from itertools import cycle

play = True
players = [1, 2]
while play:

    game_size = int(input("Enter the grid size for the game :- "))
    game = [[0 for j in range(game_size)] for i in range(game_size)]
    game_won = False
    player_choice  = cycle(players)
    
    game, _ = board(game, just_display = True)

    while not game_won:
        print("\n")
        current_player = next(player_choice)
        print("Player :-", current_player)
        played = False

        while not played:
            column_choice = int(input("Enter column number(0, 1, 2) :- "))
            row_choice = int(input("Enter row number(0, 1, 2) :- "))
            game, played = board(game, player = current_player, row = row_choice, column = column_choice)

        if win_game(game):
            game_won = True

            again = input("Want to play again(y/Y) or (n/N)")
            if again in ['Y', 'y']:
                print("Restarting")
            elif again in ['n', 'N']:
                print("Exiting")
                play = False
            else:
                print("Not Correct Input...Exiting")
                play = False

        
