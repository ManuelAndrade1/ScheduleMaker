#!python3 

import unittest
from subject import Subject

TEST1:Subject = Subject("Matematica II", 6, {"Lun": [0, 1], "Mierc":[0, 1]})
TEST2:Subject = Subject("Matematica II", 8, {"Mierc":[0, 1], "Lun":[0, 1]})
TEST3:Subject = Subject("Matematica II", 10, {"Mar":[0, 1], "Juev":[0, 1]})

class TestSubject(unittest.TestCase):
	def test_attrs(self):
		self.assertEqual(TEST1.subject, "Matematica II")
		self.assertEqual(TEST1.section, 6)
		self.assertEqual(TEST1.schedule, {"Mierc":[0, 1], "Lun":[0, 1]})
		self.assertEqual(TEST1.time_schedule, 
			{"Mierc":["8:00-9:40", "9:50-11:30"], "Lun":["8:00-9:40", "9:50-11:30"]})

	def test_repr(self):
		exp_text:str = "Matematica II, 6, ['Lun', 'Mierc']"
		exp_text2:str = "Matematica II, 6, ['Mierc', 'Lun']"
		self.assertTrue(str(TEST1) == exp_text or str(TEST1) == exp_text2)

	def test_eq(self):
		self.assertTrue(TEST1 == TEST2)
		self.assertFalse(TEST1 == TEST3)
		
unittest.main()


