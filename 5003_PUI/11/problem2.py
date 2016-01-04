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
    
def naiveApproach(intersections, tripLocations, distanceThreshold):
    #counts is a dictionary that has as keys the intersection index in the intersections list
    #and as values the number of trips in the tripLocation list which are within a distance of
    #distanceThreshold from the intersection
    counts = {}
    startTime = time.time()

    #TODO: insert your code here. You should implement the naive approach, i.e., loop 
    #      through all the trips and find the closest intersection by looping through
    #      all of them
    for x in range(len(intersections)):
		counts[x] = 0
		
        
    for x in intersections:			
		global x_idx
		
		for p in tripLocations:			# pickups
			dist = sqrt((x[0] - p[0])**2 + (x[1] - p[1])**2)
			if dist <= distanceThreshold:
				counts[x_idx] += 1
		x_idx += 1

    #
    endTime = time.time()
    print 'The naive computation took', (endTime - startTime), 'seconds'
    return counts

def kdtreeApproach(intersections, tripLocations, distanceThreshold):
    #counts is a dictionary that has as keys the intersection index in the intersections list
    #and as values the number of trips in the tripLocation list which are within a distance of
    #distanceThreshold from the intersection
    counts = {}
    startTime = time.time()

    #TODO: insert your code here. You should build the kdtree and use it to query the closest
    #      intersection for each trip
    for x in range(len(intersections)):
		counts[x] = 0
		
    tree = spatial.KDTree(intersections)
    
    pts = tripLocations
    
    for i in tree.query_ball_point(pts, r=distanceThreshold):
		for j in i:
			counts[j] += 1
	
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
		intersectCount['count'].append(counts[k])
		
    # print intersectCount    

    plt.scatter(intersectCount['lng'], intersectCount['lat'], s=intersectCount['count'], alpha=0.3)
    plt.title('Busiest Intersection Improved - Manhattan Pickups Within: ' + str(sys.argv[3]) + ' Distance')
    plt.ylabel('Latitude')
    plt.xlabel('Longitude')
    plt.show()
    print 'TODO'

def extraCredit(intersections, counts):
    #TODO: intersect the code to plot here
    print 'TODO'

if __name__ == '__main__':
    #these functions are provided and they already load the data for you
    roadIntersections = loadRoadNetworkIntersections(sys.argv[1])
    tripPickups       = loadTaxiTrips(sys.argv[2])
    distanceThreshold = float(sys.argv[3])
    
    # print tripPickups
    
    #You need to implement this one. You need to make sure that the counts are correct
    x_idx = 0				# intersection index
    naiveCounts = naiveApproach(roadIntersections,tripPickups, distanceThreshold)
    # print naiveCounts
    '''tripCounts = 0
    
    for k in naiveCounts:
		tripCounts += naiveCounts[k]
		
    print tripCounts'''
    
    #You need to implement this one. You need to make sure that the counts are correct
    kdtreeCounts = kdtreeApproach(roadIntersections,tripPickups, distanceThreshold)
    # print kdtreeCounts
    '''KDtripCounts = 0
    
    for k in kdtreeCounts:
		KDtripCounts += kdtreeCounts[k]
		
    print KDtripCounts'''

    #
    plotResults(roadIntersections,kdtreeCounts)
