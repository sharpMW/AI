import copy
print("SARIM MOIN WARSI 21BCB0261")
def manhattan_distance(state, goal_state):
    goal_positions = {
        value: (i, j) for i, row in enumerate(goal_state) for j, value in enumerate(row)
    }
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                goal_i, goal_j = goal_positions[state[i][j]]
                distance += abs(goal_i - i) + abs(goal_j - j)
    return distance


def get_possible_moves(state):
    zero_pos = [
        (i, j)
        for i, row in enumerate(state)
        for j, value in enumerate(row)
        if value == 0
    ][0]
    moves = []
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for dx, dy in directions:
        x, y = zero_pos[0] + dx, zero_pos[1] + dy
        if 0 <= x < 3 and 0 <= y < 3:
            new_state = copy.deepcopy(state)
            new_state[zero_pos[0]][zero_pos[1]], new_state[x][y] = (
                new_state[x][y],
                new_state[zero_pos[0]][zero_pos[1]],
            )
            moves.append(new_state)
    return moves


def hill_climbing(initial_state, goal_state):
    current_state = initial_state
    current_heuristic = manhattan_distance(current_state, goal_state)
    path = [current_state]

    while True:
        neighbors = get_possible_moves(current_state)

        next_state = None
        next_heuristic = current_heuristic

        for neighbor in neighbors:
            heuristic = manhattan_distance(neighbor, goal_state)
            if heuristic < next_heuristic:
                next_state = neighbor
                next_heuristic = heuristic

        if next_heuristic >= current_heuristic:
            break

        current_state = next_state
        current_heuristic = next_heuristic
        path.append(current_state)

        if current_heuristic == 0:
            break

    return path, current_heuristic


if __name__ == "__main__":
    initial_state = [[1, 2, 3], [4, 8, 0], [7, 6, 5]]
    goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    path, heuristic = hill_climbing(initial_state, goal_state)

    print("\nInitial State\t\tGoal state")
    for i in range(3):
        print(initial_state[i],"\t\t", goal_state[i])
    print()

    print("Path Taken:")
    for step, state in enumerate(path):
        print(f"Step {step}:")
        for row in state:
            print(row)
        print()

    print("Final State:")
    for row in path[-1]:
        print(row)
    print("\nHeuristic Value:", heuristic)

    if heuristic != 0:
        print(
            "\nAnalysis: The algorithm failed to find the solution due to a local maximum or plateau."
        )
    else:
        print("\nSuccess: Goal state reached.")

print("SARIM MOIN WARSI 21BCB0261")
