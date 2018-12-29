
def move(player_pos, maze, direction):
    """
    player_pos- position of the player define as (0,1)
    maze-
    direction-of the movemnet
        1. if the directiom is "6" the player moves "right"
        1. if the directiom is "4" the player moves "left"
        1. if the directiom is "8" the player moves "up"
        1. if the directiom is "2" the player moves "down"
    """
    if direction==6:
        if maze[player_pos[0] + 1][player_pos[1]] != 1:
            player_pos[0] +=1


    elif direction==4:
        if maze[player_pos[0] - 1][player_pos[1] ] != 1:
            player_pos[0] -=1


    elif direction==8:
        if maze[player_pos[0]][player_pos[1] + 1] != 1:
            player_pos[1] +=1


    else:
        if maze[player_pos[0]][player_pos[1] - 1] != 1:
            player_pos[1] -=1

    endofloop = False
    if maze[player_pos[0]][player_pos[1]]==9: #zabieram ciastka z planszy
        maze[player_pos[0]][player_pos[1]]=0
        player_pos[2] += 1
        for line in maze:
            if 9 in line:
                endofloop = True
        if not endofloop:
            return True



def inputdirection():
    while True:
        dir = input("Which way sir?")
        dictionary = {"E": 8, "W": 2, "N": 4, "S": 6}
        try:
            return dictionary[dir.upper()]
        except:
            continue




while True:
    with open('plansza.txt', 'r') as f:
        maze = []
        for line in f.readlines():
            newline = []
            for letter in line:
                try:
                    newline.append(int(letter))
                except:
                    continue
            maze.append(newline)
    player = [1, 1, 0]  # trzecia zmienna - zebrane ciastka

    # 9=cookie
    # 0=board
    # 1=wall
    # x, y = player[0], player[1]
    x, y = player[0], player[1]
    while True:
        maze[x][y] = 0
        x, y = player[0], player[1]
        maze[x][y] = 'x'
        for line in maze:
            print(*line, end="\n")
        if move(player, maze, inputdirection()):
            print("you won")
            break
