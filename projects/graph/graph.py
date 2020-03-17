"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        res = set()

        for vert_nbr_id in self.vertices[vertex_id]:
            res.add(vert_nbr_id)

        for vert_id in self.vertices:
            vert = self.vertices[vert_id]

            for vert_nbr_id in vert:
                if vert_nbr_id == vertex_id:
                    res.add(vert_id)
                    break

        return res

    def bft(self, start_vert_id):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        vert_ids = Queue()
        vert_ids.enqueue(start_vert_id)
        visited = [start_vert_id]

        while vert_ids.size() > 0:
            vert_id = vert_ids.dequeue()
            print(vert_id)

            for vert_nbr_id in self.vertices[vert_id]:
                if vert_nbr_id not in visited:
                    visited.append(vert_nbr_id)
                    vert_ids.enqueue(vert_nbr_id)


    def dft(self, start_vert_id):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        vert_ids = Stack()
        vert_ids.push(start_vert_id)
        visited = [start_vert_id]

        while vert_ids.size() > 0:
            vert_id = vert_ids.pop()
            print(vert_id)

            for vert_nbr_id in self.vertices[vert_id]:
                if vert_nbr_id not in visited:
                    visited.append(vert_nbr_id)
                    vert_ids.push(vert_nbr_id)

    def dft_recursive(self, vert_id, visited = []):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """

        if len(visited) == 0:
            print(vert_id)
            visited = [vert_id]
        
        for vert_nbr_id in self.vertices[vert_id]:
            if vert_nbr_id not in visited:
                print(vert_nbr_id)
                visited.append(vert_nbr_id)
                self.dft_recursive(vert_nbr_id, visited)


    def bfs(self, start_vert_id, dest_vert_id):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        prev = {}
        vert_ids = Queue()
        vert_ids.enqueue(start_vert_id)
        visited = [start_vert_id]

        while vert_ids.size() > 0:
            vert_id = vert_ids.dequeue()
            
            for vert_nbr_id in self.vertices[vert_id]:
                if vert_nbr_id not in visited:
                    prev[vert_nbr_id] = vert_id
                    vert_ids.enqueue(vert_nbr_id)
                    visited.append(vert_nbr_id)

        path = []
        vert_id = dest_vert_id

        while vert_id in prev:
            path.append(vert_id)
            vert_id = prev[vert_id]

        return [start_vert_id] + [x for x in path[::-1]]

    def dfs(self, start_vert_id, dest_vert_id):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        prev = {}
        vert_ids = Stack()
        vert_ids.push(start_vert_id)
        visited = [start_vert_id]

        while vert_ids.size() > 0:
            vert_id = vert_ids.pop()
            
            for vert_nbr_id in self.vertices[vert_id]:
                if vert_nbr_id not in visited:
                    prev[vert_nbr_id] = vert_id
                    vert_ids.push(vert_nbr_id)
                    visited.append(vert_nbr_id)

        path = []
        vert_id = dest_vert_id

        while vert_id in prev:
            path.append(vert_id)
            vert_id = prev[vert_id]

        return [start_vert_id] + [x for x in path[::-1]]

    def dfs_recursive(self, cur_vert_id, dest_vert_id, path = [], visited = set()):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """

        # add cur_vert_id to visited

        #append cur_vert_id to path

        #if at dest return path

        visited.add(cur_vert_id)
        path = path + [cur_vert_id]
        print(path)

        if cur_vert_id == dest_vert_id:
            return path

        for vert_nbr_id in self.vertices[cur_vert_id]:
            if vert_nbr_id not in visited:
                new_path = self.dfs_recursive(vert_nbr_id, dest_vert_id, path, visited)

                if new_path:
                    return new_path

        return None

    # def dfs_recursive(self, cur_vert_id, dest_vert_id, prev = {}, visited = []):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """


        # for vert_nbr_id in self.vertices[cur_vert_id]:
        #     print(vert_nbr_id)
        #     if vert_nbr_id not in visited:
        #         visited.append(vert_nbr_id)
        #         prev[vert_nbr_id] = cur_vert_id
        #         self.dfs_recursive(vert_nbr_id, dest_vert_id, prev, visited)

        # if cur_vert_id == dest_vert_id:
        #     print("prev = ",prev)
        #     path = []
        #     vert_id = dest_vert_id


        #     while vert_id in prev:
        #         path.append(vert_id)
        #         vert_id = prev[vert_id]
        #         print("path = ", path)

        #     return [cur_vert_id] + [x for x in path[::-1]]
        # else:
        #     return (prev, visited)


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
