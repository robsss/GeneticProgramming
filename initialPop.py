import random

def initialPop(popSize,rangeMin,rangeMax,genLength):
	"""Creates the initial population for evolving"""
	
	pop=[]

	for i in range(popSize):
		genome=[]
		for j in range(genLength):
			param=random.randint(rangeMin,rangeMax)
			genome.append(param)
		pop.append(genome)
				
	return pop


if __name__=='__main__':
	print(initialPop(10,1,12,4))