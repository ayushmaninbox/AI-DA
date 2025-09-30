import heapq

def manhattan_distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

def greedy_best_first_search(grid, start, goal):
    rows, cols = len(grid), len(grid[0])

    priority_queue = [(manhattan_distance(start, goal), start[0], start[1], [start])]
    visited = set()

    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    while priority_queue:
        h, row, col, path = heapq.heappop(priority_queue)

        if (row, col) in visited:
            continue
        visited.add((row, col))

        if (row, col) == goal:
            return path

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if (0 <= new_row < rows and 0 <= new_col < cols 
                and grid[new_row][new_col] != '#' 
                and (new_row, new_col) not in visited):
                
                new_h = manhattan_distance((new_row, new_col), goal)
                new_path = path + [(new_row, new_col)]
                heapq.heappush(priority_queue, (new_h, new_row, new_col, new_path))

    return None 

def run_test_case():
    print("Choose a test case:")
    print("1. Simple 5x5 grid")
    print("2. Grid with obstacles")
    print("3. Custom input")

    choice = input("Enter choice (1-3): ").strip()

    if choice == "1":
        grid_data = [
            "S....",
            ".....",
            "..#..",
            ".....",
            "....G"
        ]
        rows, cols = 5, 5

    elif choice == "2":
        grid_data = [
            "S.#...",
            "..#.#.",
            "..#...",
            "...#.G"
        ]
        rows, cols = 4, 6

    else: 
        print("Enter grid dimensions:")
        rows, cols = map(int, input("Rows Columns: ").split())
        print(f"Enter {rows} rows of the grid:")
        grid_data = []
        for i in range(rows):
            grid_data.append(input(f"Row {i+1}: ").strip())

    grid = grid_data
    start = goal = None
    for i in range(rows):
        for j in range(len(grid[i])):
            if grid[i][j] == 'S':
                start = (i, j)
            elif grid[i][j] == 'G':
                goal = (i, j)

    print(f"\nGrid ({rows}x{cols}):")
    for row in grid:
        print(row)

    print(f"Start: {start}, Goal: {goal}")

    path = greedy_best_first_search(grid, start, goal)

    if path:
        print(f"\nPath found with {len(path)} steps:")
        for i, (row, col) in enumerate(path):
            h = manhattan_distance((row, col), goal)
            label = "Start" if i == 0 else "Goal" if i == len(path)-1 else f"Step {i}"
            print(f"{label}: ({row}, {col}) h={h}")

        print("\nPath visualization (* = path):")
        result_grid = [list(row) for row in grid]
        for (row, col) in path[1:-1]: 
            if result_grid[row][col] == '.':
                result_grid[row][col] = '*'
        for row in result_grid:
            print(''.join(row))
    else:
        print("No path found!")

print("\n\n=== Warehouse Robot - Greedy Best-First Search ===")
print("Legend: S=Start, G=Goal, #=Obstacle, .=Free cell")

while True:
    run_test_case()
    again = input("\nRun another test? (y/n): ").strip().lower()
    if again != 'y':
        print("Goodbye!")
        break
    print("\n" + "="*50)
