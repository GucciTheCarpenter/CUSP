
# Performs search in unsorted L.
# L might not be sorted. Can't use sorting to solve this.
def searchGreaterNotSorted(L, v):
	greater = 0
	
	for i in L:
		if i > v:
			greater += 1
			
	return greater


# Performs search in sorted L (ascending order).
# L is sorted.
def searchGreaterSorted(L, v):
	greater = 0
	
	for i,val in enumerate(L):
		if val > v:
			greater = len(L[i:])
			break
	return greater

# Performs binary search in sorted L (ascending order).
def searchGreaterBinSearch(L, v):
	greater = 0
	
	lo = 0					
	hi = len(L)					
	
	while hi - lo != 1:
		mid = int(lo + (hi - lo)/2)	# include 'floor'?
		if L[mid] < v:
			lo = mid			# lo = mid + 1? why not?
		if L[mid] > v:
			greater += len(L[mid:hi])
			hi = mid			
		if L[mid] == v:
			lo = mid			# lo = mid + 1? why not?
					
	return greater


# Performs range search in sorted L (ascending order).
def searchInRange(L, v1, v2):
	val1 = searchGreaterBinSearch(L, v1)
	val2 = searchGreaterBinSearch(L, v2)
	
	return val1 - val2
	
	

if __name__ == '__main__':
	
	l1 = [4, 5, 3, 3, 45, -12, 5, 0, 5, 3, 8, 7, 5]
	v1 = 3
	l2 = sorted(l1)
	v2 = 9
	
	print searchGreaterNotSorted(l1, v1)
	print searchGreaterSorted(l2, v1)
	print l2
	print searchGreaterBinSearch(l2, v1)
	print searchInRange(l2, v1, v2)
	
