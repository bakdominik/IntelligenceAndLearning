import queue


def create_maze():
    maze = []
    maze.append(["#", "O", "#", "#", "#", "#", "#"])
    maze.append(["#", " ", " ", " ", "#", " ", "#"])
    maze.append(["#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#", " ", "#", " ", " ", " ", "#"])
    maze.append(["#", " ", "#", "#", "#", " ", "#"])
    maze.append(["#", " ", " ", " ", "#", " ", "#"])
    maze.append(["#", "#", "#", "#", "#", "X", "#"])

    return maze


def create_maze2():
    maze = []
    maze.append(["#", "#", "#", "#", "#", "O", "#", "#", "#"])
    maze.append(["#", " ", " ", " ", " ", " ", " ", " ", "#"])
    maze.append(["#", " ", "#", "#", " ", "#", "#", " ", "#"])
    maze.append(["#", " ", "#", " ", " ", " ", "#", " ", "#"])
    maze.append(["#", " ", "#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#", " ", "#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#", " ", "#", " ", "#", " ", "#", "#", "#"])
    maze.append(["#", " ", " ", " ", " ", " ", " ", " ", "#"])
    maze.append(["#", "#", "#", "#", "#", "#", "#", "X", "#"])

    return maze



def validate_path(maze, moves):
    for x, pos in enumerate(maze[0]):
        if pos == "O":
            start = x

    i = start
    j = 0
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1

        if not(0 <= i < len(maze[0]) and 0 <= j < len(maze)):
            return False
        elif (maze[j][i] == "#"):
            return False

    return True

def find_end(maze, moves):
    for x, pos in enumerate(maze[0]):
        if pos == "O":
            start = x

    i = start
    j = 0
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1

    if maze[j][i] == "X":
        print("Found: " + moves)
        return True

    return False
q = queue.Queue()
q.put("")
maze = create_maze2()
path = ""
    
while not find_end(maze, path):
    path = q.get()
    for i in ["L","R","U","D"]:
        put = path + i
        if validate_path(maze,put):
            q.put(put)
