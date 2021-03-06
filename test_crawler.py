import unittest
from crawler import Crawler

class CrawlerTests(unittest.TestCase):

	def setUp(self):
		self.maze = [ "000000",
									"0  0 0 ",
									"0 00 0",
									"  0000"
									]

		self.crawler = Crawler(3, 2, self.maze)
	
	# Test 'perform' method
	def test_turns_left_when_facing_wall(self):
		self.crawler.perform()
		self.assertEqual(self.crawler.x, 2)
		self.assertEqual(self.crawler.y, 2)
		

	# Test 'movements_to_try' method
	def test_list_rotator_lambda(self):
		self.assertEqual(self.crawler.movements_to_try(), ["left", "up", "right", "down"])
		self.crawler.pointing = "left"
		self.assertEqual(self.crawler.movements_to_try(), ["down", "left", "up", "right"])
		self.crawler.pointing = "down"
		self.assertEqual(self.crawler.movements_to_try(), ["right", "down", "left", "up"])
		self.crawler.pointing = "right"
		self.assertEqual(self.crawler.movements_to_try(), ["up", "right", "down", "left"])


	# Test 'move_in_order' method
	def test_crawler_turns_180_degrees_when_facing_dead_end(self):
		self.crawler.x = 5
		self.crawler.y = 2
		self.crawler.move_in_order(["left", "up", "right", "down"])
		self.assertEqual(self.crawler.x, 5)
		self.assertEqual(self.crawler.y, 3)


	# Test 'shift' method
	def test_shift_left_moves_in_right_direction(self):
		self.crawler.shift("left")
		self.assertEqual(self.crawler.x, 2)
		self.assertEqual(self.crawler.y, 2)
		self.assertEqual(self.crawler.pointing, 'left')

	def test_shift_up_moves_in_right_direction(self):
		self.crawler.shift("up")
		self.assertEqual(self.crawler.x, 3)
		self.assertEqual(self.crawler.y, 1)
		self.assertEqual(self.crawler.pointing, 'up')

	def test_shift_right_moves_in_right_direction(self):
		self.crawler.shift("right")
		self.assertEqual(self.crawler.x, 4)
		self.assertEqual(self.crawler.y, 2)
		self.assertEqual(self.crawler.pointing, 'right')

	def test_shift_down_moves_in_right_direction(self):
		self.crawler.shift("down")
		self.assertEqual(self.crawler.x, 3)
		self.assertEqual(self.crawler.y, 3)
		self.assertEqual(self.crawler.pointing, 'down')


	# Test 'is_space' method
	def test_is_space_detects_space(self):
		self.assertTrue(self.crawler.is_space("left"))

	def test_is_space_detects_wall(self):
		self.assertFalse(self.crawler.is_space("right"))

	def test_is_space_detects_edge_of_maze(self):
		self.crawler.x = 1
		self.crawler.y = 4
		self.assertFalse(self.crawler.is_space("left"))
