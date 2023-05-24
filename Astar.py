def print_board(elements):
    for i in range(9):
        if i % 3 == 0:
            print()
        if elements[i] == -1:
            print("_", end=" ")
        else:
            print(elements[i], end=" ")
    print()


def solvable(start):
    inv = 0
    for i in range(9):
        if start[i] <= 1:
            continue
        for j in range(i + 1, 9):
            if start[j] == -1:
                continue
            if start[i] > start[j]:
                inv += 1
    return inv % 2 == 0


def heuristic(start, goal):
    h = 0
    goal_set = set(goal)
    for i in range(9):
        if start[i] != -1 and start[i] in goal_set:
            j = goal.index(start[i])
            h += abs(j - i) // 3 + abs(j - i) % 3
    return h


def move_left(start, position):
    start[position], start[position - 1] = start[position - 1], start[position]


def move_right(start, position):
    start[position], start[position + 1] = start[position + 1], start[position]


def move_up(start, position):
    start[position], start[position - 3] = start[position - 3], start[position]


def move_down(start, position):
    start[position], start[position + 3] = start[position + 3], start[position]


def move_tile(start, goal):
    empty_at = start.index(-1)
    row, col = divmod(empty_at, 3)
    t1, t2, t3, t4 = start[:], start[:], start[:], start[:]
    f1, f2, f3, f4 = float('inf'), float('inf'), float('inf'), float('inf')

    if col - 1 >= 0:
        move_left(t1, empty_at)
        f1 = heuristic(t1, goal)
    if col + 1 < 3:
        move_right(t2, empty_at)
        f2 = heuristic(t2, goal)
    if row + 1 < 3:
        move_down(t3, empty_at)
        f3 = heuristic(t3, goal)
    if row - 1 >= 0:
        move_up(t4, empty_at)
        f4 = heuristic(t4, goal)

    min_heuristic = min(f1, f2, f3, f4)

    if f1 == min_heuristic:
        move_left(start, empty_at)
    elif f2 == min_heuristic:
        move_right(start, empty_at)
    elif f3 == min_heuristic:
        move_down(start, empty_at)
    elif f4 == min_heuristic:
        move_up(start, empty_at)


def solve_eight(start, goal):
    moves = 0
    print_board(start)
    f = heuristic(start, goal)

    while f > 0:
        move_tile(start, goal)
        print_board(start)
        f = heuristic(start, goal)
        moves += 1

    print("\nSolved in {} moves".format(moves))


def main():
    start = []
    goal = []

    print("\nEnter the start state (Enter -1 for empty, space-separated values):")
    for _ in range(3):
        row = list(map(int, input().split()))
        start.extend(row)

    print("\nEnter the goal state (Enter -1 for empty, space-separated values):")
    for _ in range(3):
        row = list(map(int, input().split()))
        goal.extend(row)

    print("\nStart State:")
    print_board(start)

    if solvable(start):
        print("\nSolving...")
        solve_eight(start, goal)
    else:
        print("Not possible to solve")


if __name__ == '__main__':
    main()
