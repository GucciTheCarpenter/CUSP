

def solveOnlyLists(inputList):
    uniqueList = []
    
    for i in inputList:
		if not i in uniqueList:
			uniqueList.append(i)
    
    return uniqueList

def solveDict(inputList):
    uniqueList = []
    uniqueDict = {}
    
    for i in inputList:
		if not i in uniqueDict:
			uniqueDict[i] = i
			uniqueList.append(i)

    return uniqueList

def solveSorted(sortedInputList):
	uniqueList = []
	
	comp = sortedInputList[0] - 1
	
	for i in sortedInputList:
		if i > comp:
			uniqueList.append(i)
			comp = i
	
	return uniqueList


if __name__ == '__main__':
	
	l1 = [4, 5, 3, 3, 45, -12, 5, 0, 5, 3, 8, 7, 5]
	l2 = sorted(l1)
	
	print solveOnlyLists(l1)
	print solveDict(l1)
	print solveSorted(l2)
	
	
