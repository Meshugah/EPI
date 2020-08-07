#  Graphs, the geometry of positions
#  Concerning these bridges, it was asked whether anyone could arrange a route in such a way that he would cross each bride once and only once
#  Graphs
import collections

# ADT
MatchResult = collections.namedTuple('MatchResult', ('winning_team', 'losing_team'))


# okay so what do my inputs look like: matches
def can_team_a_beat_team_b(matches, team_a, team_b):
    def build_graph():
        graph = collections.defaultdict(set)
        for match in matches:  # Create Adjacency list
            graph[match.winning_team].add(match.losing_team)  # use add here instead of = because this adds an element to the set if it's not present
        return graph

    def is_reachable_dfs(graph, curr, dest, visited=set()):
        if curr == dest:  #
            return True
        if curr not in graph or curr in visited:  # if curr not
            return False
        visited.add(curr)
        return any(is_reachable_dfs(graph, team, dest) for team in graph[curr])  # useful to understand graph[curr], the structure of graph https://www.educative.io/edpresso/how-to-implement-depth-first-search-in-python. Also any is useful for stopping once it finds a true case, I think. Graph[curr] are the neighboring nodes in the adjacency matrix.

    is_reachable_dfs(build_graph(), team_a, team_b)


# fascinating theory behind using DFS or BFS:
# So we got options mane:
# 1) To evaluate all possible paths but this shit is astronomical (play travis)
# 2) To only go to white pixels, but then you'd be repeating white pixels( think of a loop, if there was a loop and you chose to not repeat pixels. you're solution would have to start again.)
# 3) bruh, keeping track of pixels is exactly what BFS and DFS are for. Just make a graph of all the WHITE pixels in the maze and then BFS or DFS( i think it's BFS for shortest path, makes sense cause you aren't exhausting depth in the wrong path, ah but that was wrong. DFS is what you want because the recursive calls leading up to the call of the final node would just straight up give you the right path. BFS instead is the fastest way to tell if a node is in a graph but is harder to implement than DFS. If it's not asking for shortest path you want to use DFS, cause BFS is harder )

WHITE, BLACK = range

Coordinate = collections.namedtuple("coordinate", ("x", "y"))

# black makes the path
def search_maze(maze, s, e):
    # DFS
    def search_maze_helper(cur):
        # checks if the pixel given is NOT in the maze and if it is white, return false
        if not (0 <= cur.x < len(maze) and 0 <= cur.y < len(maze[cur.x])  # base condition 1
                # above: 0 <= x < 3 and 0 <= y < 2 for
                # 2: 2,3  <-> y
                # 1: 1,7    ^ x
                # 4: 3,9    |
                and maze[cur.x][cur.y] == WHITE):
            return False
        path.append(cur)  # adds the current pixel to 'path'
        maze[cur.x][cur.y] = BLACK  # classifies the pixel as black
        if cur == e:  # if it meets the end pixel         # base condition 2
            return True  # returns true.

        if any(  # map passes each of the following into the search maze helper, that returns false 1) if the coordinate is not inside of the map and 2) if the pixel is white. or adds the pixel to the path.
                map(search_maze_helper, (
                        Coordinate(cur.x - 1, cur.y),
                        Coordinate(cur.x + 1, cur.y),
                        Coordinate(cur.x, cur.y + 1),
                        Coordinate(cur.x, cur.y - 1)
                ))):
            return True
        # Cannot find a path, remove the entry added in path.append(cur.
        del path[-1]  # removes the top of the path stack. path[-1] is cur in this stack scope.
        return False  # False for cur is not in the maze.

    path = []  # this is okay
    if not search_maze_helper(s):  # why do i even need this. the helper is to build the path, and this is to return an empty path if it is completely filled with false. this is useful because it fragments the responsibility of the recursive step. The recursive step is allowed to continue working on building what is required in the path by operating at the coordinate level rather than at the path level.
        return []
    return path
