import csv
import shapefile
import sys
import numpy as np
import math
from bokeh.plotting import *


def loadComplaintsPoints(complaintsFilename):
  # Reads all complaints and keeps zips which have complaints.
  with open(complaintsFilename) as f:
    csvReader = csv.reader(f)
    headers = csvReader.next()
    incidentZip = headers.index('Incident Zip')
    latColIndex = headers.index('Latitude')
    lngColIndex = headers.index('Longitude')

    lat = []
    lng = [] 
    compZip = []   

    for row in csvReader:
      try:
        lat.append(float(row[latColIndex]))
        lng.append(float(row[lngColIndex]))
        compZip.append(row[incidentZip])
      except:
        pass

    return {'zip_list': compZip, 'lat_list': lat, 'lng_list': lng}


def getZipBorough(zipBoroughFilename):
  # Reads all complaints and keeps zips which have complaints.
  with open(zipBoroughFilename) as f:
    csvReader = csv.reader(f)
    csvReader.next()

    return {row[0]: row[1] for row in csvReader}
  

def drawPlot(shapeFilename, mapPoints, zipBorough, n):
	# Read the ShapeFile
	dat = shapefile.Reader(shapeFilename)
	
	# Creates a dictionary for zip: {lat_list: [], lng_list: []}.
	zipCodes = []
	polygons = {'lat_list': [], 'lng_list': []}
	
	record_index = 0
	
	minMapLng = 180.0
	maxMapLng = -180.0
	minMapLat = 90.0
	maxMapLat = 0.0
	for r in dat.iterRecords():
		currentZip = r[0]
		
		# Keeps only zip codes in NY area.
		
		if currentZip in zipBorough:
			zipCodes.append(currentZip)
			
			# Gets shape for this zip.
			shape = dat.shapeRecord(record_index).shape
			points = shape.points
			
			# Breaks into lists for lat/lng.
			lngs = [p[0] for p in points]
			lats = [p[1] for p in points]
			
			lng_min, lng_max = min(lngs), max(lngs)
			lat_min, lat_max = min(lats), max(lats)
			
			if lng_min < minMapLng:
				minMapLng = lng_min
			if lng_max > maxMapLng:
				maxMapLng = lng_max
			if lat_min < minMapLat:
				minMapLat = lat_min
			if lat_max > maxMapLat:
				maxMapLat = lat_max
				
			# Stores lat/lng for current zip shape.
			polygons['lng_list'].append(lngs)
			polygons['lat_list'].append(lats)
			
		record_index += 1
		
	stepMapLng = (maxMapLng - minMapLng)/n
	stepMapLat = (maxMapLat - minMapLat)/n
	
	n_sq = n ** 2
	grid_count = np.zeros(n_sq).reshape(n,n)
	
	cellCircles = {'comp_count': [], 'log2_count': [], 'lat_mid': [], 'lng_mid': []}
	
	for i in range(len(mapPoints['zip_list'])):
		if mapPoints['zip_list'][i] in zipBorough:
			x = int((mapPoints['lng_list'][i] - minMapLng)/stepMapLng)
			y = int((mapPoints['lat_list'][i] - minMapLat)/stepMapLat)
			grid_count[y,x] +=1
			
	# print grid_count
	
	for i in range(n):
		for j in range(n):
			cellCircles['comp_count'].append(grid_count[i][j])
			cellCircles['lng_mid'].append((minMapLng + (stepMapLng/2)) + (stepMapLng * j))
			cellCircles['lat_mid'].append((minMapLat + (stepMapLat/2)) + (stepMapLat * i))
			if grid_count[i][j] > 0.0:
				cellCircles['log2_count'].append(math.log(grid_count[i][j], 2))
			else:
				cellCircles['log2_count'].append(0)
			
	# print cellCircles
	
	# Creates the Plot
	output_file("ComplaintCirclePerNCells.html", title="problem3")
	# hold()
	
	TOOLS="pan,wheel_zoom,box_zoom,reset,previewsave"
	
	# Creates the polygons.
	patches(polygons['lng_list'], polygons['lat_list'], \
          fill_color='#fee8c8', line_color="gray", \
          tools=TOOLS, plot_width=1100, plot_height=700, \
          title="Complaint Circle Per " + str(n_sq) + " Cells in NY")
          
	# Draws mapPoints on top of map.
	hold()

	scatter(cellCircles['lng_mid'], cellCircles['lat_mid'],
		fill_color='red',color='red', fill_alpha=0.3, line_alpha=0.1, size=cellCircles['log2_count'], name="mapPoints")
		
	show()


if __name__ == '__main__':
	if len(sys.argv) != 5:
		print 'Usage:'
		print sys.argv[0] \
		+ ' <n> <complaintsfilename> <zipboroughfilename> <shapefilename>'
		print '\ne.g.: ' + sys.argv[0] \
		+ ' 5 data/complaints.csv zip_borough.csv data/nyshape.shp'
	else:
		n = int(sys.argv[1])
		mapPoints = loadComplaintsPoints(sys.argv[2])
		zipBorough = getZipBorough(sys.argv[3])
		drawPlot(sys.argv[4], mapPoints, zipBorough, n)

