class Gen():

	def __init__(self, initial):
		'''initializer takes the initial genome list and sets all scores to 0'''
		self.genomeList = initial
		self.rawScore = 0
		self.normScore = 0
		self.accumulatedScore = 0

	def __radd__(self, other):
		'''allows genomes to be summed based on their scores'''
		return other + self.rawScore
		
	def __repr__(self):
		'''prints itself as its list followed by its rawScore'''
		return str(self.genomeList) +' '+ str(self.rawScore)

	def __eq__(self, other):
		""" Compares one chromosome with another """
		return self.genomeList == other.genomeList


	def __getslice__(self, a, b):
		""" Return the sliced part of genome """
		return self.genomeList[a:b]

	def __getitem__(self, key):
		""" Return the specified gene of List """
		return self.genomeList[key]

	def __setitem__(self, key, value):
		""" Set the specified value for an gene of List """
		self.genomeList[key] = value

	def __iter__(self):
		""" Iterator support to the list """
		return iter(self.genomeList)
   
	def __len__(self):
		""" Returns the size of the List """
		return len(self.genomeList)
