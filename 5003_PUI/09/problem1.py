import csv
import shapefile
import sys
from bokeh.plotting import *
from bokeh.objects import HoverTool
from collections import OrderedDict


def getZipBorough(filename):
	with open(filename) as f:
		csvReader = csv.reader(f)
		header = next(csvReader)
		
		zip_boro = {}
		
		for row in csvReader:
			zip_boro[row[0]] = row[1]
			
		return zip_boro
  
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
			
def getZipTopAgency(zipBorough, zipComplaints):
	zip_TopAgency = {}
	
	for key in zipComplaints:
		if key in zipBorough:
			agencySort = sorted(zipComplaints[key].items(), key=lambda x: (-x[1]))		
			zip_TopAgency[key] = agencySort[0]
			
	return zip_TopAgency

def drawPlot(shapeFilename, zipBorough, zipTopAgency):
	# Read the ShapeFile
	dat = shapefile.Reader(shapeFilename)
	
	# Creates a dictionary for zip: {lat_list: [], lng_list: []}.
	zipCodes = []
	polygons = {'lat_list': [], 'lng_list': [], 'color_list': []}
	
	colorscale = ['#8dd3c7', '#ffffb3', '#bebada', '#fb8072', '#80b1d3', '#fdb462', '#b3de69', '#fccde5', '#d9d9d9', '#bc80bd', '#ccebc5', '#ffed6f']
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
			if currentZip in zipTopAgency:
				if not zipTopAgency[currentZip][0] in agencyTypeDict:
					agencyTypeDict[zipTopAgency[currentZip][0]] = len(agencyTypeDict)
				colorindex = agencyTypeDict[zipTopAgency[currentZip][0]] % len(colorscale)
				polygons['color_list'].append(colorscale[colorindex])
			else:
				color = 'white'
				polygons['color_list'].append(color)
				
				
		record_index += 1
	
	source = ColumnDataSource(data=dict(zip_code = zipCodes))
	
	# Creates the Plot
	output_file("TopAgencyNYCzip.html", title="problem1")
	hold()
	
	TOOLS="pan,wheel_zoom,box_zoom,reset,hover,previewsave"
	figure(title="Top agency in each NYC zip code", tools=TOOLS, plot_width=1200, plot_height=800)
	
	# Creates the polygons.
	patches(polygons['lng_list'], polygons['lat_list'], fill_color=polygons['color_list'], line_color="gray") # polygons['color_list']
	
	#### NO LUCK WITH LEGEND OR HOVER
	# patches.legend(title='Agencies')
	# hover = curplot().select(dict(type=HoverTool))
	# hover.tooltips = OrderedDict([('zip code', '@zipCodes')])
	
	agencyColor = {k: colorscale[agencyTypeDict[k]] for k in agencyTypeDict}
	print agencyColor



	show()


if __name__ == '__main__':
  if len(sys.argv) != 4:
    print 'Usage:'
    print sys.argv[0] + ' <complaints> <zipboroughfilename> <shapefilename>'
    print '\ne.g.: ' + sys.argv[0] + ' data/nyshape.shp zip_borough.csv'
  else:
    zipBorough = getZipBorough(sys.argv[2])
    zipComplaints = getZipAgencyComplaints(sys.argv[1])
    zipTopAgency = getZipTopAgency(zipBorough, zipComplaints)
    drawPlot(sys.argv[3], zipBorough, zipTopAgency)
  # print zipTopAgency

