size = 6
players = [{"name": x, "rest": False} for x in input().split(", ")]

maze = [input().split() for _ in range(size)]

while True:
    curr_row, cur_col = [int(x) for x in input()[1:-1].split(", ")]
    player = players.pop(0)
    movement = maze[curr_row][cur_col]

    if player["rest"]:
        player["rest"] = False
    elif movement == "E":
        print(f"{player['name']} found the Exit and wins the game!")
        break
    elif movement == "T":
        print(f"{player['name']} is out of the game! The winner is {players[0]['name']}.")
        break
    elif movement == "W":
        player["rest"] = True
        print(f"{player['name']} hits a wall and needs to rest.")

    players.append(player)
