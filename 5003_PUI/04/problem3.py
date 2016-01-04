import numpy as np
import time

naive = []
def buildNaive(points, n):
	global naive
	del naive[:]
	
	min_x = 1
	min_y = 1
	max_x = 0
	max_y = 0
	
	for x,y in points:
		if x < min_x:
			min_x = x
		if x > max_x:
			max_x = x
		if y < min_y:
			min_y = y
		if y > max_y:
			max_y = y
	
	naive = [min_x, min_y, max_x, max_y]
	
	return naive


onedim = []
indexes = []
split1 = 0
def buildOneDim(points,n):
	
	global indexes
	global onedim
	global split1
	
	del onedim[:]
	
	split1 = 1.0/n
	onedim = [[] for x in range(n)]
	indexes = range(n)
	
	for x,y in points:
		part_index = int(x/split1)
		onedim[part_index].append((x,y))
		

twodim = []
split2 = 0
def buildTwoDim(points,n):
	
	global twodim
	global split2
	
	del twodim[:]
	
	split2 = 1.0/n
	
	twodim = [[] for x in range(n)]
	for i in range(n):
		twodim[i] = [[] for x in range(n)]
		
	for x,y in points:
		x_index = int(x/split2)
		y_index = int(y/split2)
		twodim[x_index][y_index].append((x,y))
		
	return twodim


def queryNaive(x0, y0, x1, y1):
	
    count = 0
    
    for x,y in points:
		if x >= x0 and x < x1 and y >= y0 and y < y1:
			count += 1

    return count

def queryOneDim(x0, y0, x1, y1):
	global onedim
	global indexes
	global split1
	
	count = 0
	
	min_x = x0
	max_x = x1
	min_part = int(min_x/split1)
	max_part = int(max_x/split1)
	
	if max_part - min_part >= 2:
		for i in range(min_part + 1, max_part):
			for x,y in onedim[i]:
				if y0 <= y <= y1:
					count += 1
		for x,y in onedim[min_part]:
			if x0 <= x <= x1 and y0 <= y <= y1:
				count += 1
		for x,y in onedim[max_part]:
			if x0 <= x <= x1 and y0 <= y <= y1:
				count += 1
	else:
		for i in range(min_part, max_part + 1):
			for x,y in onedim[i]:
				if x0 <= x <= x1 and y0 <= y <=y1:
					count += 1
		
	return count

def queryTwoDim(x0, y0, x1, y1):
	global twodim
	global split2
	
	count = 0
	min_x = int(x0/split2)
	max_x = int(x1/split2)
	min_y = int(y0/split2)
	max_y = int(y1/split2)
	
	# print min_x, max_x, min_y, max_y
	if max_x - min_x >= 2 and max_y - min_y >=2:
		for i in range(min_x + 1, max_x):
			for j in range(min_y + 1, max_y):
				count += len(twodim[i][j])
		for x,y in twodim[min_x][min_y]:
			if x0 <= x <= x1 and y0 <= y <= y1:
					count += 1
		for x,y in twodim[min_x][max_y]:
			if x0 <= x <= x1 and y0 <= y <= y1:
					count += 1
		for x,y in twodim[max_x][min_y]:
			if x0 <= x <= x1 and y0 <= y <= y1:
					count += 1					
		for x,y in twodim[max_x][max_y]:
			if x0 <= x <= x1 and y0 <= y <= y1:
					count += 1	
		for i in range(min_y + 1, max_y):
			for x,y in twodim[min_x][i]:
				if x0 <= x <= x1:
					count += 1
			for x,y in twodim[max_x][i]:
				if x0 <= x <= x1:
					count += 1
		for i in range(min_x + 1, max_x):
			for x,y in twodim[i][min_y]:
				if y0 <= y <= y1:
					count += 1
			for x,y in twodim[i][max_y]:
				if y0 <= y <= y1:
					count += 1			
	else:
		for i in range(min_x, max_x + 1):
			for j in range(min_y, max_y + 1):
				for x,y in twodim[i][j]:
					if x0 <= x <= x1 and y0 <= y <= y1:
						count += 1
	
	return count

x = np.random.random(1000000)
y = np.random.random(1000000)
	
points = zip(x,y)
		

buildNaive(points, 1)

t0 = time.time()
print queryNaive(.3, .3, .5, .5)
t1 = time.time()
tNaive = t1 - t0
print 'Naive query: ' + str(tNaive) + '\n'

t2 = time.time()
buildOneDim(points, 1000)
t3 = time.time()
tBuildOneDim = t3 - t2
print 'Build One Dim: ' + str(tBuildOneDim)

t4 = time.time()
print queryOneDim(.3, .3, .5, .5)
t5 = time.time()
tQueryOneDim = t5 - t4
print 'Query One Dim: ' + str(tQueryOneDim) + '\n'

t6 = time.time()
buildTwoDim(points, 1000)
t7 = time.time()
print 'Build Two Dim: ' + str(t7 - t6)

t8 = time.time()
print queryTwoDim(.3, .3, .5, .5)
t9 = time.time()
print 'Query Two Dim: ' + str(t9 - t8)

#print onedim
