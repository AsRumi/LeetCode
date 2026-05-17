"""
Not a LeetCode problem, practicing Graphs.
"""

class Graph:
    def __init__(self, routes):
        self.routes = routes
        self.graph = {}
        for start, end in self.routes:
            if start in self.graph:
                self.graph[start].append(end)
            else:
                self.graph[start] = [end]
        print(f"Graph created: {self.graph}")
    
    def get_paths(self, start, end):
        paths, current_path = [], []
        # If start is not found, return false; else if end found in start, append to paths, else travel further locations that you can reach from start.
        def move(start, end):
            if start not in self.graph:
                return
            else:
                if end in self.graph[start]:
                    current_path.append(start)
                    current_path.append(end)
                    paths.append(current_path[:])
                    current_path.pop()
                    current_path.pop()
                    moveFurther(start, end)
                    return
                else:
                    moveFurther(start, end)
        
        def moveFurther(start, end):
            for further_dest in self.graph[start]:
                current_path.append(start)
                move(further_dest, end)
                current_path.pop()

        move(start, end)
        return paths

    def getShortestPath(self, start, end, path):
        # Assumption: Path from start to end definitely exists.
        path = path + [start]
        if end in self.graph[start]:
            return path + [end]
        if start not in self.graph:
            return 
        for further_dest in self.graph[start]:
            return min(len(self.getShortestPath(further_dest, end, path)))
        
        return

routes = [
    ("Mumbai", "Paris"),
    ("Mumbai", "Dubai"),
    ("Paris", "New York"),
    ("Paris", "Dubai"),
    ("Dubai", "New York"),
    ("New York", "Toronto")
]
my_graph = Graph(routes)
dest = "Toronto"
path_to_dest = my_graph.get_paths("Mumbai", dest)
print(f"Paths to {dest}: {path_to_dest}")