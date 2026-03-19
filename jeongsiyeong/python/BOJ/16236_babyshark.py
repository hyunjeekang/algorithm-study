import sys
from collections import deque

# Read input (using sys.stdin.readline for faster I/O)
input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# Direction vectors: Up, Left, Down, Right
dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

# 1. Find the initial position of the baby shark
shark_r, shark_c = 0, 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            shark_r, shark_c = i, j
            arr[i][j] = 0 # Remove the shark from the grid to treat it as empty space

# Shark stats
shark_size = 2
eaten = 0
time = 0

def bfs(start_r, start_c, size):
    visited = [[-1] * N for _ in range(N)]
    visited[start_r][start_c] = 0
    queue = deque([(start_r, start_c)]) # Use deque for O(1) pops
    fishes = []
    
    while queue:
        r, c = queue.popleft()
        
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            
            # Check bounds and if the space is unvisited
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == -1:
                # The shark can only pass through spaces <= its size
                if arr[nr][nc] <= size:
                    visited[nr][nc] = visited[r][c] + 1
                    queue.append((nr, nc))
                    
                    # The shark can only EAT fishes strictly < its size (and > 0)
                    if 0 < arr[nr][nc] < size:
                        fishes.append((visited[nr][nc], nr, nc))
                        
    # Sort automatically handles: 1. shortest distance, 2. top-most (r), 3. left-most (c)
    fishes.sort()
    return fishes

# Main simulation loop
while True:
    # Find all reachable, edible fishes from current position
    edible_fishes = bfs(shark_r, shark_c, shark_size)
    
    # If no fishes can be eaten, the simulation ends
    if not edible_fishes:
        break
        
    # Get the best fish to eat based on the problem's criteria
    dist, next_r, next_c = edible_fishes[0]
    
    # Update time and move the shark
    time += dist
    shark_r, shark_c = next_r, next_c
    arr[next_r][next_c] = 0 # The fish is eaten, space becomes empty
    
    # Handle shark growth
    eaten += 1
    if eaten == shark_size:
        shark_size += 1
        eaten = 0

print(time)