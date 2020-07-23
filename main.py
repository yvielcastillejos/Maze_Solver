from queue import queue
from tree import tree

class maze_game:
	def __init__(self, Board):
		self.Board = Board
		self.dimensions = [len(self.Board)-1, len(Board[0])-1]
		self.start, self.end = find_start_end(self.Board)

def main(Board):
		shortest = solver(Board)
		for move in shortest:
			Board.Board[move[0]][move[1]] = "@"
		for i in range(len(Board.Board)):
			print(str(Board.Board[i]) + "\n")
		return

def solver(Board):
	visited, shortest, end_game = [], [], False
	line, qtree, A = queue(), queue(), tree(Board.start, [])
	moves = get_possible_move_positions(Board.Board, Board.start, Board.dimensions)
	while end_game == False:
		for i in range(len(moves)):
			if moves[i] not in visited:
				visited.append(moves[i])
				line.enqueue(moves[i])
				qtree.enqueue(A.key[1][A.add_child(moves[i])])
				if moves[i] == Board.end:
					end_game = True
					break
		A, moves = qtree.dequeue(), get_possible_move_positions(Board.Board, line.dequeue(), Board.dimensions)
	while A.key[0] != Board.end:
		A = qtree.dequeue() 
	while A.key[0] != Board.start:
		shortest.append(A.key[0])
		A = A.parent
	return shortest

def get_possible_moves(Board, current_position, dimensions):
	all_moves, possible_moves = [-1,1,1,-1], [0,0,0,0]
	column_index, row_index, dimn = current_position[0], current_position[1], dimensions
	if (((column_index-1) >= 0) and ((Board[column_index-1][row_index] == " ") or (Board[column_index-1][row_index] == "E"))):
		possible_moves[0] += all_moves[0]
	if (((column_index+1) <= dimn[0]) and ((Board[column_index+1][row_index] == " ") or (Board[column_index+1][row_index] == "E"))):
        	possible_moves[1] += all_moves[1]
	if (((row_index-1) >= 0) and ((Board[column_index][row_index+1] == " ") or (Board[column_index][row_index+1] == "E"))):
        	possible_moves[2] += all_moves[2]
	if (((row_index+1) <= dimn[1]) and ((Board[column_index][row_index-1] == " ") or (Board[column_index][row_index-1] == "E"))):
        	possible_moves[3] += all_moves[3]
	return possible_moves

def get_possible_move_positions(Board, current_position, dimensions):
	move_pos, position = [], [current_position[0],current_position[0],current_position[1],current_position[1]]
	possible_moves = get_possible_moves(Board, current_position, dimensions)
	for i in range(len(possible_moves)):
		if possible_moves[i] != 0:
			if ((i==0) or (i==1)):
				move_pos.append([possible_moves[i] +  position[i], current_position[1]])
			else:
				move_pos.append([current_position[0], possible_moves[i] +  position[i]])
	return move_pos

def find_start_end(Board):
    start_index, end_index = [], []
    for i in range(len(Board)):
        for j in range(len(Board[0])):
             if Board[i][j] == "S":
                start_index.append(i)
                start_index.append(j)
             if Board[i][j] == "E":
                end_index.append(i)
                end_index.append(j)
    return start_index, end_index
