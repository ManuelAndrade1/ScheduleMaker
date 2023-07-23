#!python3

from typing import List, Dict


BLOCKS = ["8:00-9:40", "9:50-11:30", "11:40-13:20", "13:30-15:10", "15:20-17:00", "17:10-18:50"]

class Subject:
	def __init__(self, sbj:str, section:int, sched:Dict[str, List[int]]):
		# Would be nice to add professors attr.
		self.subject:str = sbj
		self.section:int = section
		self.schedule:Dict[str, List[int]] = sched
		self.time_schedule:Dict[str, List[str]] = format_schedule(self.schedule)

	def __repr__(self):
		vr:str = f"""{self.subject}, {str(self.section)}, {str(list((self.schedule.keys())))}"""
		return vr
	def __eq__(self, other):
		return self.subject == other.subject and self.schedule == other.schedule

def format_schedule(schedule:Dict[str, List[int]]) -> Dict[str, List[str]]:
	"""
	Requires: Schedule dictionary with days of the week as keys and list with 
	time-blocks as values (0-5)
	Returns: Dict containing days as keys and list of string time-blocks as values
	"""
	vr:Dict[str, List[str]] = {}

	for k, v in schedule.items():
		vr[k] = time_blocks(v)

	return vr

def time_blocks(block_list:List[int]) -> List[str]:
	"""
	Requires: List of integers from 0-5
	Returns: Equivalent time-blocks in string format
	"""
	vr:List[str] = []
	for i in block_list:
		vr.append(BLOCKS[i])

	return vr