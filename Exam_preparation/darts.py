from collections import deque

size = 7

players = deque(input().split(", "))
dartboard = [[int(x) if x.isdigit() else x for x in input().split()] for _ in range(size)]

first_player = players[0]
second_player = players[1]
first_player_total_score = 501
second_player_total_score = 501
player_one_trows = 0
player_two_trows = 0

while True:
    data = input().split(", ")
    curr_row, curr_col = int(data[0][1:]), int(data[1][:-1])
    current_player = players.popleft()

    if 0 <= curr_row < size and 0 <= curr_col < size:

        if current_player == first_player:
            player_one_trows += 1

            if dartboard[curr_row][curr_col] == "B":
                print(f"{current_player} won the game with {player_one_trows} throws!")
                break
            elif dartboard[curr_row][curr_col] == "D":
                current_sum = (dartboard[curr_row][0] + dartboard[curr_row][-1] +
                              dartboard[0][curr_col] + dartboard[-1][curr_col]) * 2
                first_player_total_score -= current_sum
            elif dartboard[curr_row][curr_col] == "T":
                current_sum = (dartboard[curr_row][0] + dartboard[curr_row][-1] +
                               dartboard[0][curr_col] + dartboard[-1][curr_col]) * 3
                first_player_total_score -= current_sum
            elif str(dartboard[curr_row][curr_col]).isdigit():
                first_player_total_score -= dartboard[curr_row][curr_col]

            if first_player_total_score <= 0:
                print(f"{current_player} won the game with {player_one_trows} throws!")
                break
        elif current_player == second_player:
            player_two_trows += 1

            if dartboard[curr_row][curr_col] == "B":
                print(f"{current_player} won the game with {player_two_trows} throws!")
                break
            elif dartboard[curr_row][curr_col] == "D":
                current_sum = (dartboard[curr_row][0] + dartboard[curr_row][6] +
                              dartboard[0][curr_col] + dartboard[6][curr_col]) * 2
                second_player_total_score -= current_sum
            elif dartboard[curr_row][curr_col] == "T":
                current_sum = (dartboard[curr_row][0] + dartboard[curr_row][6] +
                               dartboard[0][curr_col] + dartboard[6][curr_col]) * 3
                second_player_total_score -= current_sum
            elif str(dartboard[curr_row][curr_col]).isdigit():
                second_player_total_score -= dartboard[curr_row][curr_col]

            if second_player_total_score <= 0:
                print(f"{current_player} won the game with {player_two_trows} throws!")
                break

    players.append(current_player)
