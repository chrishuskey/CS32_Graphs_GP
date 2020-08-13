# Import libraries, packages, modules, classes/functions:
from queue import Queue
from stack import Stack


# Class for a graph object represented as an adjacency list:
class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges (an adjacency list)."""
    def __init__(self):
        # Initiate as empty adjacency list:
        self.vertices = {}

    def add_vertex(self, vertex_id):
        # Check to make sure the provided vertex isn't already in the graph:
        if vertex_id not in self.vertices:
            # Add it:
            self.vertices[vertex_id] = set()
        else:
            raise IndexError(f"Vertex {vertex_id} is already in the graph!")

    def add_edge(self, v1, v2):
        # Make sure both vertices are in the graph before adding the edge that connects them:
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            self.vertices[v2].add(v1)  # Bidirectional
        else:
            raise IndexError("Vertex does not exist in graph!")

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

    def bft(self, starting_vertex_id):
        # Initialize empty queue and set of visited nodes:
        queue = Queue()
        visited = set()

        # Check if provided starting vertex is in our graph:
        if starting_vertex_id in self.vertices.keys():
            # If so, add starting vertex to queue:
            queue.enqueue(starting_vertex_id)
        else:
            return IndexError(f"Provided starting vertex {starting_vertex_id} does not exist in graph!")

        # Process all vertices via BFT:
        while queue.size() > 0:
            # Get next vertex to process as first item in queue:
            current_vertex = queue.dequeue()
            # If the current vertex has not already been visited+processed, process it:
            if current_vertex not in visited:
                # Process current vertex:
                print(current_vertex)
                # Add adjacent vertices to queue for future processing:
                for adjacent_vertex in self.get_neighbors(current_vertex):
                    queue.enqueue(adjacent_vertex)
                # Mark current vertex as "visited" by adding to our set of visited vertices:
                visited.add(current_vertex)

    def dft(self, starting_vertex_id):
        # Initialize empty queue and set of visited nodes:
        s = Stack()
        visited = set()

        # Check if provided starting vertex is in our graph:
        if starting_vertex_id in self.vertices.keys():
            # If so, add starting vertex to stack:
            s.push(starting_vertex_id)
        else:
            return IndexError(f"Provided starting vertex {starting_vertex_id} does not exist in graph!")

        # while the stack is not empty
        while s.size > 0:
            # pop the first vertex
            v = s.pop()

            # if vertex has not been visited
            if v not in visited:
                # print it for debug
                print(v)
                # add all of it's neighbors to the top of the stack
                for next_vertex in self.get_neighbors(v):
                    s.push(next_vertex)
                # mark the vertex as visited
                visited.add(v)
    
    def bfs(self, starting_vertex_id, target_vertex_id):
        # create an empty queue and enqueue PATH To the Starting Vertex ID

        # q.enqueue([starting_vertex_id])
        # create a set to store visited vertices

        # while the queue is not empty
            # dequeue the first PATH
            # grab the last vertex from the Path

            # check if the vertex has not been visited
                # is this vertex the target?
                    # return the path
                # mark it as visited

                # then add A Path to its neighbors to the back of the queue

                # make a copy of the path
                # append the neighbor to the back of the path
                # enqueue out new path

        # return none

        # Initialize empty queue and set of visited nodes:
        queue = Queue()
        visited = set()

        # Initialize path (we will add the rest of the path from starting vertex to target vertex below):
        path = [starting_vertex_id]

        # Check if provided starting vertex is in our graph:
        if starting_vertex_id in self.vertices.keys():
            # If so, add starting vertex to queue:
            queue.enqueue(path)
        else:
            return IndexError(f"Provided starting vertex {starting_vertex_id} does not exist in graph!")

        # Process all vertices via BFT:
        while queue.size() > 0:
            # Get next vertex to process as first item in queue:
            current_path = queue.dequeue()
            current_vertex = current_path[-1]
            # If the current vertex has not already been visited+processed, check and process it:
            if current_vertex not in visited:
                # Check if it is the target --> if so, return its full path:
                if current_vertex == target_vertex_id:
                    return current_path
                # If not, then get its neighbor vertices and add their paths to the queue for future processing:
                for adjacent_vertex in self.get_neighbors(current_vertex):
                    adjacent_vertex_path = current_path + [adjacent_vertex]
                    queue.enqueue(adjacent_vertex_path)
                # Mark current vertex as "visited" by adding to our set of visited vertices:
                visited.add(current_vertex)
        
        # If no path found in entire graph, return None:
        return None

    def dfs(self, starting_vertex_id, target_vertex_id):
        pass
    

# graph = Graph()  # Instantiate your graph
# graph.add_vertex('0')
# graph.add_vertex('1')
# graph.add_vertex('2')
# graph.add_vertex('3')
# graph.add_edge('0', '1')
# graph.add_edge('1', '0')
# graph.add_edge('0', '3')
# graph.add_edge('3', '0')
# print(graph.vertices)
# # graph.add_edge('0', '4')  # Should throw IndexError.
