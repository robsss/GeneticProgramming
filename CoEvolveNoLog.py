from selector import nextpop
from initialPop import initialPop
from fitSim import fitFunc,testrun
from operator import attrgetter
from TestFitnessFunctions import testFitFunc2
import math

def averageScore(pop):
	total = sum(pop)
	return float(total)/float(len(pop))
	
def bestScore(pop,minmax='max'):
	if minmax == 'max':
		return sorted(pop,key=attrgetter('rawScore'))[len(pop)-1]
	else:
		return sorted(pop,key=attrgetter('rawScore'))[0]

lower = -math.pi
upper = math.pi
rpop = initialPop(20,lower,upper,128)
ypop = initialPop(20,lower,upper,128)

for i in range(500):
	print(i)
	fitFunc(rpop,ypop)
	print('r',averageScore(rpop),bestScore(rpop,'min'))
	print('y',averageScore(ypop),bestScore(ypop))
	rpop = nextpop(rpop,.05,lower,upper,'min')
	ypop = nextpop(ypop,.05,lower,upper,'max')

fitFunc(rpop,ypop)
testrun(bestScore(rpop,'min'),bestScore(ypop,'min'),True)
