# Maze_Solver_BFSapplication
served as a quick and easy review of BFS. Logic is a bit messy as I was implementing trees in python and accessing the keys in python is not the most straightforward thing ever :( ; However, it basically uses queues and trees to traverse back and forth and to find the minimum path. (Normally, one does not need trees to implement BFS; however, since I wanted to get the full shortest path, I needed to use trees to backtrack.)

Basically finds the shortest path of any maze given that the start and end positions are defined.
- Design the test case in test.py (Can be of any dimensions)
- Pygame will visualize any test case
- Algorithm will work as long as one "S" and "E" are defined in test.py
- Must use "#" for walls and " " for empty space
- There needs to exist a path between S and E, it will return an error otherwise.
- To run, type "python3 visualize.py" on terminal or run visualize.py on any editor you wish to use.

## Example of a test case (can be of any dimensions/design/Visualized in terminal):
<img src = "https://github.com/yvielcastillejos/Maze_Solver_BFSapplication/blob/master/Screen%20Shot%202020-10-16%20at%203.54.04%20AM.png" height = "250" width = "250">
 
 ## Visualization of testcase using pygame:
<img src = "https://github.com/yvielcastillejos/Maze_Solver_BFSapplication/blob/master/BFS.png" height = "550" width = "350">


## The result (In the terminal):
<img src = "https://github.com/yvielcastillejos/Maze_Solver_BFSapplication/blob/master/Screen%20Shot%202020-10-16%20at%203.55.29%20AM.png" height = "250" width = "250">

## We can visualize this with pygame

<img src = "https://github.com/yvielcastillejos/Maze_Solver_BFSapplication/blob/master/BFS.gif" height = "550" width = "350">

Another Test Case                                              
<img src = "https://github.com/yvielcastillejos/Maze_Solver_BFSapplication/blob/master/BFS2.gif" height = "550" width = "425">


## Next step
- Visualize how BFS really works by showing the visited blocks and how head position "looks" for the end or "E"
