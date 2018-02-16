import csv
import sys

#CHECK THAT CORRECT NUMBER OF ARGUMENTS GIVEN
if len(sys.argv) != 3:
	print 'Invalid call. Please call as follows:'
	print 'python test2.py inputfile.csv outputfile.csv'
	sys.exit()

#READ IN THE DESTINATION OUTPUT FILENAMES
input_file = sys.argv[1]
output_file = sys.argv[2]

#READ IN THE FILE, CONVERT STRINGS TO INTS
your_list = []
with open(input_file, 'rU') as infile:
	reader = csv.reader(infile, lineterminator = '\r')
	for row in infile:
		num = row.strip('[]\'\r')
		your_list.append(int(num))
	
	#for line in infile.readlines():
	#	num = line.strip('[]\'\r')
	#	your_list.append(int(num))

infile.close()

#ITERATE THROUGH your_list, GET PAIRS, ADD PAIRS TO NEW LIST
i = len(your_list)
dataArray = []

for x in range (0, i - 1):
	for y in range (x + 1, i):
		tempList = [your_list[x], your_list[y]]
		dataArray.append(tempList)

#WRITE NEW LIST TO FILE       
with open(output_file, 'wb') as outfile:
    datawriter = csv.writer(outfile)
    for row in dataArray:
        datawriter.writerow(row)
        
outfile.close()