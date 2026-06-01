from typing import Dict, Tuple

class LanguageRules:
	def __init__(self):
		self.merge_extremities: Dict[tuple[str, str], str] = {}
		self.hundreds: Tuple[str, str] = ()
		self.milestones: Dict[int, tuple[str, str]] = {}
		self.numbers: Dict[int, str] = {}

	def __repr__(self):
		return f"""
MERGING RULES: {self.merge_extremities.__repr__()}
LAST CONJUNCTION: {self.last_conjunction.__repr__()}
HUNDREDS: {self.hundreds.__repr__()}
MILESTONES: {self.milestones.__repr__()}
NUMBERS: {self.numbers.__repr__()}
		"""

