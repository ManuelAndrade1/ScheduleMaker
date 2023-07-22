#!python3 

import unittest
from subject import Subject

class TestSubject(unittest.TestCase):
	def test_repr(self):
		test1:Subject = Subject("Matematica II", 6, 0)
		self.assertEqual(str(test1), "Matematica II, 6, 8:00-9:40")


