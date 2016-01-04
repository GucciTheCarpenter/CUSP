import csv
import shapefile
import sys
import math
from bokeh.plotting import *
from bokeh.sampledata.iris import flowers

def loadComplaintsCount(complaintsFilename):
  # Reads all complaints and keeps zips which have complaints.
  with open(complaintsFilename) as f:
    csvReader = csv.reader(f)
    headers = csvReader.next()
    incidentZip = headers.index('Incident Zip')

    complaintZipCount = {}
    # colors = []
    for row in csvReader:
		if row[incidentZip] in complaintZipCount:
			complaintZipCount[row[incidentZip]] += 1
		else:
			complaintZipCount[row[incidentZip]] = 1


    return complaintZipCount


def getZipBorough(zipBoroughFilename):
  # Reads all complaints and keeps zips which have complaints.
  with open(zipBoroughFilename) as f:
    csvReader = csv.reader(f)
    csvReader.next()

    return {row[0]: row[1] for row in csvReader}
  

def drawPlot(shapeFilename, zipCounts, zipBorough):
	# Read the ShapeFile
	dat = shapefile.Reader(shapeFilename)
	
	# Creates a dictionary for zip: {lat_list: [], lng_list: []}.
	zipCodes = []
	polygons = {'lat_list': [], 'lng_list': []}
	
	zipCircles = {'zip': [], 'comp_count': [], 'log5_count': [], 'lat_mid': [], 'lng_mid': []}	 
	
	record_index = 0
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
			
			lng_mid = (lng_max + lng_min)/2.0
			lat_mid = (lat_max + lat_min)/2.0
			
			# Stores lat/lng for current zip shape.
			polygons['lng_list'].append(lngs)
			polygons['lat_list'].append(lats)
			
			
			if currentZip in zipCounts:
				zipCircles['zip'].append(currentZip)
				zipCircles['comp_count'].append(zipCounts[currentZip])
				zipCircles['log5_count'].append(math.log(zipCounts[currentZip], 5))
				zipCircles['lng_mid'].append(lng_mid)
				zipCircles['lat_mid'].append(lat_mid)
				
				
		record_index += 1
		
	# Creates the Plot
	output_file("ComplaintCirclePerZip.html", title="problem4")
	hold()
	
	TOOLS="pan,wheel_zoom,box_zoom,reset,previewsave"
	
	# Creates the polygons.
	patches(polygons['lng_list'], polygons['lat_list'], fill_color='#fee8c8', line_color="gray", tools=TOOLS, plot_width=1100, plot_height=700, title="Complaint Circle for each Zip Code in NYC")
	
	# Draws mapPoints on top of map.
	hold()
	
	# zip Circle position on the map.
	# print zipCircles
	scatter(zipCircles['lng_mid'], zipCircles['lat_mid'], fill_color='red',color='red', fill_alpha=0.3, size=zipCircles['log5_count'], name="zipCircles")
	# print zipCircles['comp_count']
	
	show()
    


if __name__ == '__main__':
  if len(sys.argv) != 4:
    print 'Usage:'
    print sys.argv[0] \
    + ' <complaintsfilename> <zipboroughfilename> <shapefilename>'
    print '\ne.g.: ' + sys.argv[0] \
    + ' data/complaints.csv zip_borough.csv data/nyshape.shp'
  else:
    zipCounts = loadComplaintsCount(sys.argv[1])
    zipBorough = getZipBorough(sys.argv[2])
    drawPlot(sys.argv[3], zipCounts, zipBorough)
    #print zipCounts
