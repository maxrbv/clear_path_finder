from collections import deque


def shortest_clear_path(grid: list[list[int]]) -> int:
    # Check if the grid is empty or has no rows, return -1 if true
    if not grid or not grid[0]:
        return -1

    # Determine the size of the grid
    n = len(grid)

    # Check if the grid is square
    if any(len(row) != n for row in grid):
        return -1

    # Check if all values in the grid are either 0 or 1
    for row in grid:
        for cell in row:
            if cell not in [0, 1]:
                return -1

    # Check if start and end is valid
    if grid[0][0] == 1 or grid[n-1][n-1] == 1:
        return -1

    # Define all possible movement directions
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]

    # Initialize a queue with starting cell coordinates (0, 0) and distance 1
    queue = deque([(0, 0, 1)])
    # Initialize a set to keep track of visited cells
    visited = set([(0, 0)])

    # Perform BFS(Breadth-first search) until the queue is empty(BFS)
    while queue:
        x, y, dist = queue.popleft()  # Pop the cell coordinates and distance from the queue

        # Check if reached the bottom-right cell
        if (x, y) == (n - 1, n - 1):
            return dist  # Return the distance to reach the destination

        # Explore all possible directions from the current cell
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            # Check if the next cell is within the grid boundaries, not visited, and clear
            if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited and grid[nx][ny] == 0:
                visited.add((nx, ny))  # Mark the next cell as visited
                queue.append((nx, ny, dist + 1))  # Add the next cell to the queue with incremented distance

    return -1  # Return -1 if no clear path is found


def main_test():
    # Example test data
    grid_valid = [
        [0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 0],
        [1, 1, 1, 1, 0],
        [1, 1, 1, 1, 0]
    ]

    grid_invalid = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ]

    grid_invalid_empty = []

    grid_invalid_not_square = [
        [0, 1, 0],
        [0, 0, 0],
        [1, 1, 0],
        [1, 1, 1],
        [1, 1, 1]
    ]

    grid_invalid_values = [
        [0, 1, 0, 0, 0],
        [0, 2, 0, 1, 0],
        [1, 1, 0, 1, 0],
        [1, 1, 1, 1, 0],
        [1, 1, 1, 1, 0]
    ]

    grid_invalid_start_end = [
        [1, 0, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 0],
        [1, 1, 1, 1, 0],
        [1, 1, 1, 1, 0]
    ]

    # Check on valid data
    assert shortest_clear_path(grid_valid) == 8

    # Check on invalid data
    assert shortest_clear_path(grid_invalid) == -1

    # Check on empty matrix
    assert shortest_clear_path(grid_invalid_empty) == -1

    # Check on non-square matrix
    assert shortest_clear_path(grid_invalid_not_square) == -1

    # Check on matrix with invalid values
    assert shortest_clear_path(grid_invalid_values) == -1

    # Check on matrix with invalid start or end value
    assert shortest_clear_path(grid_invalid_start_end) == -1

    print("All tests passed successfully!")


if __name__ == "__main__":
    main_test()
