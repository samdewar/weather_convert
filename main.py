import json
import csv
def process_json(input, output, date):
	with open(input) as json_file:
		data = json.load(json_file)
	weather_data = data['children']
	data_file = open(output, 'w')
	csv_writer = csv.writer(data_file)
	output=''
	for i in range(0, len(data['children'][1]['children'])):
		try:
			line=date+","
			for j in range(0,len(data['children'][1]['children'][i]['children'])):
				cell = ""
				for k in range(0, len(data['children'][1]['children'][i]['children'][j]['name'])):

					if(data['children'][1]['children'][i]['children'][j]['name'][k]!='Â' and data['children'][1]['children'][i]['children'][j]['name'][k]!="°"):
						cell=cell+data['children'][1]['children'][i]['children'][j]['name'][k]
				line=line+cell+','
			output=output+'\n'+line
		except:
			print("fail on ", input)

	#data_file.close()
	return output

if __name__ == '__main__':
	directory=input("Directory")
	day_range=input("upper range of days(int)")
	month=input("calendar month(int)")


	output=directory+"\\output.csv"
	data_file = open(output, 'w')
	csv_writer = csv.writer(data_file)
	data=""
	for i in range(1,int(day_range)):
		filepath=directory+'\\'+str(i)+'-'+month+'-19.json'
		data=data+process_json(filepath,output, str(i)+"-"+month)
		#csv_writer.writerow([str(i)+","+data])

	csv_writer.writerow([data])
	data_file.close()