#!python3

BLOCKS = ["8:00-9:40", "9:50-11:30", "11:40-13:20", "13:30-15:10", "15:20-17:00", "17:10-18:50"]
class Subject:
	def __init__(self, sbj:str, section:int, block:int):
		# Would be nice to add professors attr.
		self.subject:str = sbj
		self.section:int = section
		self.block:int = block
		self.time:str = BLOCKS[block]

	def __repr__(self):
		return self.subject + ", " + str(self.section) + ", " + self.time 

	def __eq__(self, other):
		return self.subject == other.subject and self.block == other.block