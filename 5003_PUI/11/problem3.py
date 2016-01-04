import sys
import time
import csv
from math import sqrt
from scipy import spatial

def loadTaxiTripsPickupAndDropoffs(filename):
    #bbox around Manhattan
    latBounds = [40.6,40.9]
    lngBounds = [-74.05,-73.90]
    #
    f = open(filename)
    reader = csv.reader(f)
    header = reader.next()
    #
    lngIndex0 = header.index(' pickup_longitude')
    latIndex0 = header.index(' pickup_latitude')
    latIndex1 = header.index(' dropoff_latitude')
    lngIndex1 = header.index(' dropoff_longitude')
    result = []
    for l in reader:
        try:
            point0 = [float(l[latIndex0]),float(l[lngIndex0])]
            point1 = [float(l[latIndex1]),float(l[lngIndex1])]
            if latBounds[0] <= point0[0] <= latBounds[1] and lngBounds[0] <= point0[1] <= lngBounds[1] and latBounds[0] <= point1[0] <= latBounds[1] and lngBounds[0] <= point1[1] <= lngBounds[1]:
                result.append([point0[0],point0[1],point1[0],point1[1]])
        except:
            print l
    return result
    
def naiveApproach(tripLocations, startRectangle, endRectangle):
    #indices is a list that should contain the indices of the trips in the tripLocations list
    #which start in the startRectangle region and end in the endRectangle region
    indices = []
    startTime = time.time()

    #TODO: insert your code here. You should implement the naive approach, i.e., loop 
    #      through all the trips and find the closest intersection by looping through
    #      all of them
    startRect_minLat = startRectangle[0][0]
    startRect_maxLat = startRectangle[0][1]
    startRect_minLng = startRectangle[1][0]
    startRect_maxLng = startRectangle[1][1]
    
    endRect_minLat = endRectangle[0][0]
    endRect_maxLat = endRectangle[0][1]
    endRect_minLng = endRectangle[1][0]
    endRect_maxLng = endRectangle[1][1]
    
    for p in tripLocations:
		global p_idx
		if startRect_minLat <= p[0] <= startRect_maxLat and startRect_minLng <= p[1] <= startRect_maxLng and endRect_minLat <= p[2] <= endRect_maxLat and endRect_minLng <= p[3] <= endRect_maxLng:
			indices.append(p_idx)
		p_idx += 1

    #
    endTime = time.time()
    print 'The naive computation took', (endTime - startTime), 'seconds'
    return indices

def kdtreeApproach(tripLocations, startRectangle, endRectangle):
    #indices is a list that should contain the indices of the trips in the tripLocations list
    #which start in the startRectangle region and end in the endRectangle region
    indices = []
    indices_temp = []
    
    startRect_minLat = startRectangle[0][0]
    startRect_maxLat = startRectangle[0][1]
    startRect_minLng = startRectangle[1][0]
    startRect_maxLng = startRectangle[1][1]
    
    endRect_minLat = endRectangle[0][0]
    endRect_maxLat = endRectangle[0][1]
    endRect_minLng = endRectangle[1][0]
    endRect_maxLng = endRectangle[1][1]
    
    startRectangleCenter = [[((startRectangle[0][1] - startRectangle[0][0])/2.0) + startRectangle[0][0],((startRectangle[1][1] - startRectangle[1][0])/2.0) + startRectangle[1][0]]]
    endRectangleCenter = [[((endRectangle[0][1] - endRectangle[0][0])/2.0) + endRectangle[0][0],((endRectangle[1][1] - endRectangle[1][0])/2.0) + endRectangle[1][0]]]
    
    startRectangleRadius = (sqrt((startRectangle[0][1] - startRectangle[0][0])**2 + (startRectangle[1][1] - startRectangle[1][0])**2))/2.0
    endRectangleRadius = (sqrt((endRectangle[0][1] - endRectangle[0][0])**2 + (endRectangle[1][1] - endRectangle[1][0])**2))/2.0
    
    startTrip = []
    for p in tripLocations:
		startTrip.append([p[0],p[1]])
		
    endTrip = []
    for p in tripLocations:
		endTrip.append([p[2],p[3]])
		
    startTime = time.time()

    #TODO: insert your code here. You should build the kdtree and use it to query the closest
    #      intersection for each trip

    startTree = spatial.KDTree(startTrip)
    startTree.query_ball_point(startRectangleCenter, r=startRectangleRadius)
    # print len(startTree.query_ball_point(startRectangleCenter, r=startRectangleRadius)[0])
    
    		
    endTree = spatial.KDTree(endTrip)
    endTree.query_ball_point(endRectangleCenter, r=endRectangleRadius)
    # print len(endTree.query_ball_point(endRectangleCenter, r=endRectangleRadius)[0])
    
    startCandidates = startTree.query_ball_point(startRectangleCenter, r=startRectangleRadius)[0]
    endCandidates = endTree.query_ball_point(endRectangleCenter, r=endRectangleRadius)[0]
    
    for p in startCandidates:
		if p in endCandidates:
			indices_temp.append(p)
			
    for i in indices_temp:
		if startRect_minLat <= tripLocations[i][0] <= startRect_maxLat and startRect_minLng <= tripLocations[i][1] <= startRect_maxLng and endRect_minLat <= tripLocations[i][2] <= endRect_maxLat and endRect_minLng <= tripLocations[i][3] <= endRect_maxLng:
			indices.append(i)
		
		
    #
    endTime = time.time()
    print 'The kdtree computation took', (endTime - startTime), 'seconds'
    return indices

def extraCredit(tripLocations, startPolygon, endPolygon):
    #indices is a list that should contain the indices of the trips in the tripLocations list
    #which start in the startPolygon region and end in the endPolygon region
    indices = []

    #TODO: insert your code here. You should build the kdtree and use it to query the closest
    #      intersection for each trip

    return indices    

if __name__ == '__main__':
    #these functions are provided and they already load the data for you
    trips             = loadTaxiTripsPickupAndDropoffs(sys.argv[1])
    
    #
    startRectangle    = [[40.713590,40.721319],[-74.011116,-73.994722]] #[[minLat,maxLat],[minLng,maxLng]]
    endRectangle      = [[40.744532,40.748398],[-74.003005,-73.990881]] #[[minLat,maxLat],[minLng,maxLng]]
    
    #You need to implement this one. You need to make sure that the counts are correct
    p_idx = 0				# trip index
    naiveIndices = naiveApproach(trips,startRectangle, endRectangle)
    # print naiveIndices

    #You need to implement this one. You need to make sure that the counts are correct
    kdtreeIndices = kdtreeApproach(trips,startRectangle, endRectangle)
    # print kdtreeIndices
