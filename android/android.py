def createMaze(fp):
    maze = []
    for i in range(200):
        column = []
        for j in range(200):
            column.append('X')
        maze.append(column)

    startPoint = ()
    for i, row in enumerate(fp):
        if ' ' in row:
            coordsTemp, strandTemp = row.split(' ')
            coords = [int(m) for m in coordsTemp.split(',')]
            strand = strandTemp.split(',')
            print(coords)
            print(strand)
            for x in strand:
                if x == "U":
                    maze[coords[0]][coords[1]] = "O"
                    coords[1] = coords[1] - 1
                if x == "D":
                    maze[coords[0]][coords[1]] = "O"
                    coords[1] = coords[1] + 1
                if x == "L":
                    maze[coords[0]][coords[1]] = "O"
                    coords[0] = coords[0] - 1
                if x == "R":
                    maze[coords[0]][coords[1]] = "O"
                    coords[0] = coords[0] + 1
                if x.startswith("X"):
                    maze[coords[0]][coords[1]] = "X"
                if x.startswith("F"):
                    maze[coords[0]][coords[1]] = "F"
                if x.startswith("S"):
                    startPoint = [coords[0], coords[1]]
                    maze[coords[0]][coords[1]] = "S"
        
    return startPoint, maze

def getAdjacent(maze, node, visited):
    adjacent = []
    if maze[node[0] - 1][node[1]] in ['O', 'F', 'S'] and [node[0] - 1, node[1]] not in visited:
        adjacent.append([node[0] - 1, node[1]])
    if maze[node[0] + 1][node[1]] in ['O', 'F', 'S'] and [node[0] + 1, node[1]] not in visited:
        adjacent.append([node[0] + 1, node[1]])
    if maze[node[0]][node[1] - 1] in ['O', 'F', 'S'] and [node[0], node[1] - 1] not in visited:
        adjacent.append([node[0], node[1] - 1])
    if maze[node[0]][node[1] + 1] in ['O', 'F', 'S'] and [node[0], node[1] + 1] not in visited:
        adjacent.append([node[0], node[1] + 1])
    return adjacent

def solve(maze, start):
    visited = []
    queue = []
    queue.append([start])
    while queue:
        path = queue.pop(0)
        node = path[-1]
        #print(path)
        if(node not in visited):
            visited.append(node)
            #print(visited)
        #print(visited)
        if maze[node[0]][node[1]] == "F":
            return path
        for adjacent in getAdjacent(maze, node, visited):
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)

filename = input("Input filename to be parsed:\n")

with open(filename, 'r') as fp:
    start, maze = createMaze(fp)
    result = solve(maze, start)
    print(result)
    #print(maze)
    """
    with open('result', 'w') as fp2:
        for x in range(len(maze)):
            for y in range(len(maze[x])):
                fp2.write(maze[x][y])
            fp2.write("\n")
    """