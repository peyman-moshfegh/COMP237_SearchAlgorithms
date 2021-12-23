# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 21:32:01 2021

@author: Peyman
"""

from Graph import Graph as Graph
from collections import deque

class Node:
    def __init__(self, name):
        self.name = name
        self.parent = None

def BFS_Peyman(Graph, startStudent, goalStudent):
    if startStudent not in Graph or goalStudent not in Graph:
        print("At least one of the students is not in the Graph")
        return
    queue = deque([])
    visited = {startStudent}
    queue.append(Node(startStudent))
    while len(queue):
        currentNode = queue.popleft()
        if currentNode.name == goalStudent:
            path = []
            while currentNode.parent:
                path.append(currentNode.name)
                currentNode = currentNode.parent
            path.append(startStudent)
            path.reverse()
            for i in range(len(path) - 1):
                print(path[i], end = " ==> ")
            print(path[-1])
            return
        for child in Graph[currentNode.name]:
            if child not in visited:
                visited.add(child)
                queue.append(Node(child))
                queue[-1].parent = currentNode
    print("Relationship cannot be established")
                
BFS_Peyman(Graph, "Dolly", "Peyman")
BFS_Peyman(Graph, "George", "Bob")
