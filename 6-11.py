cities={
	'wuhan':{
		'country':'China',
		'popularion':'fifteen million',
		'fact':'I live in wuhan',
		},
		
	'shanghai':{
		'country':'China',
		'population':'thirty million',
		'fact':'I know little about shanghai',
		},
		
	'guangzhou':{
		'country':'China',
		'population':'ten million',
		'fact':'This city is really hot',
		},
	}
for city,message in cities.items():
	print(city+':'+str(message))
	
