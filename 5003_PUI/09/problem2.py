import csv
import shapefile
import sys
from bokeh.plotting import *
from bokeh.objects import HoverTool
from collections import OrderedDict


# import zip/borough csv and create dict; key = zip, val = borough
def getZipBorough(filename):
	with open(filename) as f:
		csvReader = csv.reader(f)
		header = next(csvReader)
		
		zip_boro = {}
		
		for row in csvReader:
			zip_boro[row[0]] = row[1]
			
		return zip_boro
  
# tally agency complaint counts by zip	
def getZipAgencyComplaints(filename):
	with open(filename) as f:
		csvReader = csv.reader(f)
		header = next(csvReader)

		
		comp_count = {}
		
		for row in csvReader:
			agency = row[3]
			incident_zip = row[8]
			if not incident_zip in comp_count:
				comp_count[incident_zip] = {agency: 1}
			if incident_zip in comp_count:
				if not agency in comp_count[incident_zip]:
					comp_count[incident_zip][agency] = 1
				if agency in comp_count[incident_zip]:
					comp_count[incident_zip][agency] += 1
					
		return comp_count
			
'''def getZipTopAgency(zipBorough, zipComplaints):
	zip_TopAgency = {}
	
	for key in zipComplaints:
		if key in zipBorough:
			agencySort = sorted(zipComplaints[key].items(), key=lambda x: (-x[1]))		
			zip_TopAgency[key] = agencySort[0]
			
	return zip_TopAgency'''

# get agency specific counts/comp
def getZipAgencyCompare(agency1, agency2):
	zip_AgencyCompare = {}
	colorscale = ['#fef0d9', '#fdcc8a', '#fc8d59', '#e34a33', '#b30000']
	
	for key in zipComplaints:
		if key in zipBorough:
			if agency1 not in zipComplaints[key] and agency2 not in zipComplaints[key]:
				zip_AgencyCompare[key] = 'white'
			elif agency1 not in zipComplaints[key]:
				zip_AgencyCompare[key] = colorscale[0]
			elif agency2 not in zipComplaints[key]:
				zip_AgencyCompare[key] = colorscale[4]
			else:
				zip_AgencyCompare[key] = colorscale[int((float(zipComplaints[key][agency1])/(zipComplaints[key][agency1] + zipComplaints[key][agency2]))*5)]
			
	return zip_AgencyCompare


def drawPlot(shapeFilename, zipBorough, zipAgencyComp):
	# Read the ShapeFile
	dat = shapefile.Reader(shapeFilename)
	
	# Creates a dictionary for zip: {lat_list: [], lng_list: []}.
	zipCodes = []
	polygons = {'lat_list': [], 'lng_list': [], 'color_list': []}
	
	# colorscale = ['#fef0d9', '#fdcc8a', '#fc8d59', '#e34a33', '#b30000']
	agencyTypeDict = {}
	
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
			
			# Stores lat/lng for current zip shape.
			polygons['lng_list'].append(lngs)
			polygons['lat_list'].append(lats)
			
			# assign color to zip by top agency
			if currentZip in zipAgencyComp:
				polygons['color_list'].append(zipAgencyComp[currentZip])
			else:
				color = 'white'
				polygons['color_list'].append(color)
				
				
		record_index += 1
	
	source = ColumnDataSource(data=dict(zip_code = zipCodes))
	
	# Creates the Plot
	output_file("TwoAgencies.html", title="problem2")
	hold()
	
	TOOLS="pan,wheel_zoom,box_zoom,reset,previewsave"
	figure(title="Comparing Agencies in NY: " + sys.argv[4] + " (Darker) & "+ sys.argv[5] + " (Lighter)", tools=TOOLS, plot_width=1200, plot_height=800)
	
	# Creates the polygons.
	patches(polygons['lng_list'], polygons['lat_list'], fill_color=polygons['color_list'], line_color="gray")
	
	# hover = curplot().select(dict(type=HoverTool))
	# hover.tooltips = OrderedDict([('zip code', '@zipCodes')])
	
	agencyColor = {k: colorscale[agencyTypeDict[k]] for k in agencyTypeDict}
	# print agencyColor



	show()


if __name__ == '__main__':
  if len(sys.argv) != 6:
    print 'Usage:'
    print sys.argv[0] + ' <complaints> <zipboroughfilename> <shapefilename> <agency1> <agency2>'
    print '\ne.g.: ' + sys.argv[0] + '311.csv zip_borough.csv data/nyshape.shp DOT NYPD'
  else:
	# import zip/borough csv and create dict; key = zip, val = borough
    zipBorough = getZipBorough(sys.argv[2])
    
    # tally agency complaint counts by zip	
    zipComplaints = getZipAgencyComplaints(sys.argv[1])
    
    # get agency specific counts/comp
    zipAgencyComp  = getZipAgencyCompare(sys.argv[4], sys.argv[5])
    
    drawPlot(sys.argv[3], zipBorough, zipAgencyComp)
  # print zipTopAgency

