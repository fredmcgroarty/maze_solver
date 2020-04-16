class Crawler:	
	def __init__(self, start_x, start_y, maze):
		self.x = start_x
		self.y = start_y
		self.maze = maze
		self.pointing = "up"

	directions = {"left": 	[0, -1, 0, "<"],
								"up": 		[1, 0, -1, "^"],		# coefficients for use in other methods:
								"right": 	[2, 1, 0, ">"],			# [list rotation index, x shift, y shift, symbol]
								"down": 	[3, 0, 1, "v"]}

	def crawl(self):						# Crawl starting from leftmost available path
		cls = self.__class__
		movements = [key for key in cls.directions.keys()]
		#movements = ['left', 'up', 'right', 'down']
		movement_idx = cls.directions[self.pointing][0]
		list_rotator = lambda lst, n: lst[n:] + lst[:n]
		movements = list_rotator(movements, movement_idx)
		self.move_in_order(movements)

	def move_in_order(self, direction_list):					# Attempts to move crawler in order of preference
		for direction in direction_list:
			if self.is_space(direction):
				self.shift(direction)
				break

	def shift(self, direction):							# Moves crawler into adjacent empty space and updates direction pointer
		cls = self.__class__
		self.x = self.x+cls.directions[direction][1]
		self.y = self.y+cls.directions[direction][2]
		self.pointing = direction
		print(cls.directions[direction][3])

	def is_space(self, direction):				# Checks if adjacent space is a path or wall
		cls = self.__class__
		row = self.x+cls.directions[direction][1] - 1
		column = self.y+cls.directions[direction][2] - 1
		try:
			if self.maze[column][row] == " ":			# Is a path
				return True
			else:
				return False												# Is a wall
		except IndexError:
			return False													# Is edge of maze (first/last index in row or column array)