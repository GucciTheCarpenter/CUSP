import sys
import collections
import os.path


def clear():
	# clear all staging text files, dict, & lists
	f = open('stagingarea1.txt', 'w')
	f.truncate()
	
	global JOB_IDS
	JOB_IDS = []
		
	global jobPostings
	jobPostings = {}


def insert(fieldValues):
	
	job_id = fieldValues[0]
	if job_id in JOB_IDS:
		pass
	if not job_id in JOB_IDS:
		JOB_IDS.append(job_id)
		jobPostings[job_id] = [fieldValues]
	
	'''with open('stagingarea1.txt', 'a+') as SA1:
		job_id = fieldValues[0]
		if job_id in JOB_IDS:
			pass
		if not job_id in JOB_IDS:
			JOB_IDS.append(job_id)
			jobPostings[job_id] = [fieldValues]
			SA1.write('|'.join(map(str,fieldValues)) + '\n')'''
			
def update_all(params):
    query_field_name = params[0]
    query_field_value = params[1]
    update_field_name = params[2]
    update_field_value = params[3]
    
    query_field_index = fieldOrder[query_field_name]
    update_field_index = fieldOrder[update_field_name]
    
    updatedRowCount = 0
    
    for key in jobPostings:
		if jobPostings[key][0][query_field_index] == query_field_value:
			jobPostings[key][0][update_field_index] = update_field_value
			updatedRowCount +=1

    # Prints number of updated rows in the database.    
    print str(updatedRowCount)
    

def delete_all(params):
	field_name, field_value = params[0], params[1]
	
	field_name_index = fieldOrder[field_name]
	
	delete_ID = []
	
	for key in jobPostings:
		if jobPostings[key][0][field_name_index] == field_value:
			delete_ID.append(key)
			
	for i in delete_ID:
		del jobPostings[i]

def find(params):
	field_name, field_value = params[0], params[1]
	
	field_name_index = fieldOrder[field_name]
	
	find_dict = {}
	
	for key in jobPostings:
		if jobPostings[key][0][field_name_index] == field_value:
			find_dict[key] = jobPostings[key][0]
			
	
	
	# print 'find where ' + field_name + '=' + field_value
	for key in find_dict:
		print ('|'.join(map(str,find_dict[key])))
		
def count(params):
	field_name, field_value = params[0], params[1]
	
	field_name_index = fieldOrder[field_name]
	
	job_count = 0
	
	for key in jobPostings:
		if jobPostings[key][0][field_name_index] == field_value:
			job_count += 1
	
	print job_count


def dump():
	
	jobPostings_Ordered = collections.OrderedDict(sorted(jobPostings.items()))
	
	for key in jobPostings_Ordered:
			for i in jobPostings_Ordered[key]:
				print ('|'.join(map(str,i)))

def view(fieldNames):
	
	viewFields = {}
	
	# print 'view for fields ' + str(fieldNames)
	for key in jobPostings:
		for i in fieldNames:
			if not key in viewFields:
				viewFields[key] = [jobPostings[key][0][fieldOrder[i]]]
			if key in viewFields:
				viewFields[key].append(jobPostings[key][0][fieldOrder[i]])
	
	viewFields_Ordered = collections.OrderedDict(sorted(viewFields.items()))		
	for key in viewFields_Ordered:
		print ('|'.join(map(str,viewFields_Ordered[key][1:])))
			

 
def executeCommand(commandLine):
	tokens = commandLine.split('|') #assume that this symbol is not part of the data
	command = tokens[0]
	parameters = tokens[1:]

	if command == 'insert':
		# print 'insert'
		insert(parameters)
		
	elif command == 'delete_all':
		# print 'delete'
		delete_all(parameters)
		
	elif command == 'update_all':
		# print 'update'
		update_all(parameters)
		
	elif command == 'find':
		find(parameters)
	elif command == 'count':
		count(parameters)
	elif command == 'clear':
		clear()
		# print 'clear' + str(JOB_IDS)
		
	elif command == 'dump':
		dump()
	elif command == 'view':
		view(parameters)
	else:
		print 'ERROR: Command %s does not exist' % (command,)
		assert(False)
	
 
def executeCommands(commandFileName):
	f = open(commandFileName)
	for line in f:
		executeCommand(line.strip())
		
	
  
if __name__ == '__main__':
	
	# load the data from the database here
	
	JOB_IDS = []
	jobPostings = {}
	jobPostings_Ordered = {}
	
	delete_values = {}
	delete_ID = []
	
	
	if os.path.isfile('stagingarea1.txt') == True:
		SA1 = open('stagingarea1.txt', 'r')
		for line in SA1:
			tokens = line.strip().split('|')
			job_id = tokens[0]
			JOB_IDS.append(job_id)
			jobPostings[job_id] = tokens[:]
	if os.path.isfile('stagingarea1.txt') == False:
		open('stagingarea1.txt', 'w+')
		
	#SA1.close()
	
	#SA2 = open('stagingarea2.txt', 'a')
		
	
	fieldOrder = {'Job ID':0, 'Agency':1, '# Of Positions':2, 'Business Title': 3, 
	'Civil Service Title':4, 'Salary Range From':5, 'Salary Range To':6, 
	'Salary Frequency':7, 'Work Location':8, 'Division/Work Unit':9, 'Job Description':10, 
	'Minimum Qual Requirements': 11, 'Preferred Skills':12, 'Additional Information':13,
	'Posting Date': 14}
	
	
	# print 'load ' + str(JOB_IDS)
	
	executeCommands(sys.argv[1])
	# save the data here
	
	'''jobPostings_Ordered = collections.OrderedDict(sorted(jobPostings.items()))'''
	with open('stagingarea1.txt', 'w') as SA1:
		for key in jobPostings:
			for i in jobPostings[key]:
				SA1.write('|'.join(map(str,i)) + '\n')
	
	# print 'save ' + str(JOB_IDS)
	
