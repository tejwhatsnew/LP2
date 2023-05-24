def issafe(arr, x, y, n):
    # Checking if there is a Queen in the same column
    for row in range(x):
        if arr[row][y] == 1:
            return False

    row = x
    col = y

    # Checking the upper left diagonal for any Queen
    while row >= 0 and col >= 0:
        if arr[row][col] == 1:
            return False
        row -= 1
        col -= 1

    row = x
    col = y

    # Checking the upper right diagonal for any Queen
    while row >= 0 and col < n:
        if arr[row][col] == 1:
            return False
        row -= 1
        col += 1

    return True


def nQueen(arr, x, n):
    # Base case: if all Queens are placed, return True
    if x >= n:
        return True

    for col in range(n):
        # Check if it is safe to place a Queen at position (x, col)
        if issafe(arr, x, col, n):
            # Place the Queen at (x, col)
            arr[x][col] = 1
            # Recursively place Queens in the next row
            if nQueen(arr, x + 1, n):
                return True
            # If placing Queen at (x, col) leads to failure, backtrack and try another column
            arr[x][col] = 0

    return False


def main():
    flag = 1
    while flag == 1:

        n = int(input("Enter number of squares: "))
        if n < 4:
            print("Error! Please enter a value greater than 3!!!")
        else:
            arr = [[0] * n for _ in range(n)]

            if nQueen(arr, 0, n):
                # Printing the board with Queens placed
                for i in range(n):
                    for j in range(n):
                        print(arr[i][j], end=" ")
                    print()
        flag = int(input("Do you want to continue (1/0)?: "))


if __name__ == '__main__':
    main()
