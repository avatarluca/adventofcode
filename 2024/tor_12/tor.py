def load_input():
    with open("c:/Users/lucam/OneDrive/Desktop/advent_of_code/adventofcode/2024/tor_12/input.txt", "r") as f:
        return f.read().strip()

def part1(input):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    plants = []
    visited = []
    for line in input.split("\n"):
        plants.append([])
        visited.append([])
        for char in line:
            plants[-1].append(char)
            visited[-1].append(False)
        
    total_cost = 0

    for i in range(len(plants)):
        for j in range(len(plants[0])):
            if not visited[i][j]:
                area = 0
                perimeter = 0

                queue = []
                queue.append((i, j))
                visited[i][j] = True

                while queue:
                    x, y = queue.pop(0)
                    area += 1

                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < len(plants) and 0 <= ny < len(plants[0]):
                            if plants[nx][ny] == plants[x][y] and not visited[nx][ny]: # wenn kein glich pflanze nachbar denn zehl es als perimeter
                                queue.append((nx, ny))
                                visited[nx][ny] = True
                            elif plants[nx][ny] != plants[x][y]:
                                perimeter += 1
                        else:
                            perimeter += 1
                
                total_cost += area * perimeter
                # print(f"- A region of {plants[i][j]} plants with price {area} * {perimeter} = {area * perimeter}")

    return total_cost


def part2(input):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Idee: Mach e map mit allne kante und zehl fortlaufendi horziontal und vertikal
    plants = []
    visited = []
    for line in input.split("\n"):
        plants.append([])
        visited.append([])
        for char in line:
            plants[-1].append(char)
            visited[-1].append(False)

    edge_map = [['.'] * (len(plants[0]) + 2) for _ in range(len(plants) + 2)] # +2 für Rand
   
    total_cost = 0

    for i in range(len(plants)):
        for j in range(len(plants[0])):
            if not visited[i][j]:
                # print("Pflanze:", plants[i][j])
                area = 0
                unique_sides = 0

                queue = []
                queue.append((i, j, 0, 0)) # letschte zwei wert dx, dy vo det chömmemer bzw det ghört i, j als border ane
                visited[i][j] = True
                
                for k, line in enumerate(edge_map):
                    for l, char in enumerate(line):
                        if char != '.':
                            edge_map[k][l] = '.'

                while queue:
                    x, y, dx_last, dy_last = queue.pop(0)
                    area += 1

                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < len(plants) and 0 <= ny < len(plants[0]):
                            if plants[nx][ny] == plants[x][y] and not visited[nx][ny]: # wenn kein glich pflanze nachbar denn zehl es als perimeter
                                queue.append((nx, ny, dx, dy))
                                visited[nx][ny] = True
                            elif plants[nx][ny] != plants[x][y]:

                                if edge_map[nx + 1][ny + 1] == '.':
                                    edge_map[nx + 1][ny + 1] = []

                                edge_map[nx + 1][ny + 1].append((dx, dy, x, y))
                        else:
                            if edge_map[nx + 1][ny + 1] == '.':
                                edge_map[nx + 1][ny + 1] = []

                            edge_map[nx + 1][ny + 1].append((dx, dy, x, y))

                # horizontal
                for l, line in enumerate(edge_map):
                    in_line_top = False
                    in_line_bottom = False
                    for m, char in enumerate(line):
                        if char != '.':
                            top = False # Achtung das flag wird brucht wenn bspw. bottom line witer gaht und top unterbruch het
                            bottom = False
                            for edge in char:
                                dx, dy, x, y = edge

                                if dx == -1 and dy == 0: # top 
                                    top = True
                                    if not in_line_top:
                                        in_line_top = True
                                        unique_sides += 1
                                
                                if dx == 1 and dy == 0: # bottom 
                                    bottom = True
                                    if not in_line_bottom:
                                        in_line_bottom = True
                                        unique_sides += 1
                            
                            if not top:
                                in_line_top = False
                            if not bottom:
                                in_line_bottom = False
                        else:
                            in_line_top = False
                            in_line_bottom = False
                
                # vertikal
                for m in range(len(edge_map[0])):
                    in_line_left = False
                    in_line_right = False
                    for l in range(len(edge_map)):
                        char = edge_map[l][m]
                        if char != '.':
                            left = False
                            right = False
                            for edge in char:
                                dx, dy, x, y = edge

                                if dx == 0 and dy == -1: # left
                                    left = True
                                    if not in_line_left:
                                        in_line_left = True
                                        unique_sides += 1
                                if dx == 0 and dy == 1: # right
                                    right = True
                                    if not in_line_right:
                                        in_line_right = True
                                        unique_sides += 1

                            if not left:
                                in_line_left = False
                            if not right:
                                in_line_right = False
                        else:
                            in_line_left = False
                            in_line_right = False

                total_cost += area * unique_sides
                #print(f"- A region of {plants[i][j]} plants with price {area} * {unique_sides} = {area * unique_sides}")

    return total_cost



def main():
    input = load_input()

    print(part1(input))
    print(part2(input))


if __name__ == "__main__":
    main()