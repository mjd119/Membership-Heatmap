lines = []
with open('zip_codes.csv',  encoding='utf-8') as f:
	lines = f.readlines()

key = ""
with open('key.txt', encoding='utf-8') as f:
	key = f.readline()
	key = key.strip()

trimmed_lines = []
for line in lines:
	trimmed_line = line.strip()
	dash_index = trimmed_line.find('-')
	if dash_index > -1:
		trimmed_line = trimmed_line[:dash_index]
	trimmed_lines.append(trimmed_line)

zip_code_dict = {}
for line in trimmed_lines:
	if not line in zip_code_dict:
		zip_code_dict[line] = 1
	else:
		zip_code_dict[line] = zip_code_dict[line] + 1

print(zip_code_dict)

#zip_code_dict = dict(filter(lambda element: element[1] >= 50, zip_code_dict.items()))
#print(len(zip_code_dict.keys()))
url = 'http://maps.googleapis.com/maps/api/staticmap?center=pittsburgh&zoom=10&size=1920x1080&maptype=roadmap'
for zip_code in zip_code_dict.keys():
	url = url + '&markers='
	url = url + 'color:blue%7C'
	url = url + 'label:' + str(zip_code_dict[zip_code]) + '%7C'
	url = url + zip_code
url = url + '&key=' + key

print(url)
