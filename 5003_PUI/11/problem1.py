import sys
import time
import csv
from math import sqrt
from scipy import spatial
import matplotlib.pyplot as plt


def loadRoadNetworkIntersections(filename):
    #bbox around Manhattan
    latBounds = [40.6,40.9]
    lngBounds = [-74.05,-73.90]
    #
    listWithIntersectionCoordinates = []
    f = open(filename)
    reader = csv.reader(f, delimiter=' ')
    for l in reader:
        try:
            point = [float(l[0]),float(l[1])]
            if latBounds[0] <= point[0] <= latBounds[1] and lngBounds[0] <= point[1] <= lngBounds[1]:
                listWithIntersectionCoordinates.append(point)
        except:
            print l

    return listWithIntersectionCoordinates

def loadTaxiTrips(filename):
    #load pickup positions
    loadPickup = True
    #bbox around Manhattan
    latBounds = [40.6,40.9]
    lngBounds = [-74.05,-73.90]
    #
    f = open(filename)
    reader = csv.reader(f)
    header = reader.next()
    #
    if loadPickup:        
        lngIndex = header.index(' pickup_longitude')
        latIndex = header.index(' pickup_latitude')
    else:
        latIndex = header.index(' dropoff_latitude')
        lngIndex = header.index(' dropoff_longitude')
    result = []
    for l in reader:
        try:
            point = [float(l[latIndex]),float(l[lngIndex])]
            if latBounds[0] <= point[0] <= latBounds[1] and lngBounds[0] <= point[1] <= lngBounds[1]:
                result.append(point)

        except:
            print l
    return result
    
def naiveApproach(intersections, tripLocations):
    #counts is a dictionary that has as keys the intersection index in the intersections list
    #and as values the number of trips in the tripLocation list which has the key as the closest
    #intersection.
    counts = {}
    startTime = time.time()

    #TODO: insert your code here. You should implement the naive approach, i.e., loop 
    #      through all the trips and find the closest intersection by looping through
    #      all of them
    for x in range(len(intersections)):
		counts[x] = 0
    
    for p in tripLocations:			# pickups
		x_idx = 0					# intersection index
		least_dist = 10000			# dummy distance
		best_idx = 'na'
		for x in intersections:
			dist = sqrt((x[0] - p[0])**2 + (x[1] - p[1])**2)
			if dist < least_dist:
				least_dist = dist
				best_idx = x_idx
			x_idx += 1
		counts[best_idx] += 1

    #
    endTime = time.time()
    print 'The naive computation took', (endTime - startTime), 'seconds'
    return counts

def kdtreeApproach(intersections, tripLocations):
    #counts is a dictionary that has as keys the intersection index in the intersections list
    #and as values the number of trips in the tripLocation list which has the key as the closest
    #intersection.
    counts = {}
    startTime = time.time()

    #TODO: insert your code here. You should build the kdtree and use it to query the closest
    #      intersection for each trip
    for x in range(len(intersections)):
		counts[x] = 0
		
    tree = spatial.KDTree(intersections)
    
    pts = tripLocations
    
    for i in tree.query(pts)[1]:
		counts[i] += 1

    #
    endTime = time.time()
    print 'The kdtree computation took', (endTime - startTime), 'seconds'
    return counts

def plotResults(intersections, counts):
    #TODO: intersect the code to plot here
    
    intersectCount = {'lat': [], 'lng': [], 'count': []}
    
    for k in counts:
		intersectCount['lat'].append(intersections[k][0])
		intersectCount['lng'].append(intersections[k][1])
		intersectCount['count'].append(counts[k] * 1.5)
		
    # print intersectCount    

    plt.scatter(intersectCount['lng'], intersectCount['lat'], s=intersectCount['count'], alpha=0.3)
    plt.title('Busiest Intersections - Manhattan Pickups')
    plt.ylabel('Latitude')
    plt.xlabel('Longitude')
    plt.show()
    print 'TODO'

if __name__ == '__main__':
    #these functions are provided and they already load the data for you
    roadIntersections = loadRoadNetworkIntersections(sys.argv[1])
    # print len(roadIntersections)
    tripPickups       = loadTaxiTrips(sys.argv[2])

    #You need to implement this one. You need to make sure that the counts are correct
    naiveCounts = naiveApproach(roadIntersections,tripPickups)
    # print len(naiveCounts)
    
    '''tripCounts = 0
    
    for k in naiveCounts:
		tripCounts += naiveCounts[k]
		
    print tripCounts'''

    #You need to implement this one. You need to make sure that the counts are correct
    kdtreeCounts = kdtreeApproach(roadIntersections,tripPickups)
    # json.dump(kdtreeCounts, open('kdtree.txt', 'w'))

    #
    plotResults(roadIntersections,kdtreeCounts)
