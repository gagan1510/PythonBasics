board = [['.','.','.'],['.','.','.'],['.','.','.']]

for row in board:
    for col in row:
        print(col, end="   ")
    print("\n")

print("And the game starts!")

print("x enter your move: ")
x = int(input('x: '))
y = int(input('y: '))
board[x][y] = 'x'

print()

for row in board:
    for col in row:
        print(col, end="   ")
    print("\n")

print("o enter your move: ")
x = int(input('x: '))
y = int(input('y: '))
board[x][y] = 'o'

for row in board:
    for col in row:
        print(col, end="   ")
    print("\n")

print("x enter your move: ")
x = int(input('x: '))
y = int(input('y: '))
board[x][y] = 'x'

for row in board:
    for col in row:
        print(col, end="   ")
    print("\n")


print("o enter your move: ")
x = int(input('x: '))
y = int(input('y: '))
board[x][y] = 'o'

for row in board:
    for col in row:
        print(col, end="   ")
    print("\n")


print("x enter your move: ")
x = int(input('x: '))
y = int(input('y: '))
board[x][y] = 'x'

for row in board:
    for col in row:
        print(col, end="   ")
    print("\n")