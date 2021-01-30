import csv

lines = []
with open('zip_codes.csv',  encoding='utf-8') as f:
	lines = f.readlines()

key = ""
with open('key.txt', encoding='utf-8') as f:
	key = f.readline()
	key = key.strip()

map_html = ""
with open('map.html', 'rt', encoding='utf-8') as f:
	map_html = f.read()
map_html = map_html.replace('YOUR_API_KEY', key)
with open('map.html', 'wt', encoding='utf-8') as f:
	f.write(map_html)

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

zip_lat_long_converter = {}
with open('us-zip-code-latitude-and-longitude.csv', encoding='utf-8') as zip_lat_long:
	zip_lat_long_reader = csv.reader(zip_lat_long, delimiter=';')
	for row in zip_lat_long_reader:
		if row[0] in zip_code_dict.keys():
			zip_lat_long_converter[row[0]] = (row[3], row[4])

lat_long_density = {}
for zip_code in zip_code_dict:
	if zip_code in zip_lat_long_converter:
		lat_long_density[zip_lat_long_converter[zip_code]] = zip_code_dict[zip_code]

max_density = max(zip_code_dict.values())

with open('index.js', 'wt', encoding='utf-8') as f:
	f.write('function initMap() {\n')
	f.write('  var heatMapData = [\n')
	for lat_long in lat_long_density:
		f.write('    {location: new google.maps.LatLng(' + lat_long[0] + ', ' + lat_long[1] + '), weight: ' + str(lat_long_density[lat_long]/max_density) + '},\n')
	f.write('  ];\n')
	f.write('  var pittsburgh = new google.maps.LatLng(40.4406, -79.9959);\n')
	f.write('  map = new google.maps.Map(document.getElementById(\'map\'), {\n')
	f.write('    center: pittsburgh,\n')
	f.write('    zoom: 13,\n')
	f.write('  });\n')
	f.write('  var heatmap = new google.maps.visualization.HeatmapLayer({\n')
	f.write('    data: heatMapData,\n')
	f.write('    radius: 30,\n')
	f.write('  });\n')
	f.write('  heatmap.setMap(map)\n')
	f.write('}\n')

