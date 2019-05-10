lt=['Tom','Tim','Jenny','Tina','Hjm']
informant={
	'Tom':'C',
	'Tim':'Python',
	'Hjm':'C&Python',
	'test':'Jenny',
	}
for a in lt:
	if a in informant:
		print('Thank you,'+a)
	else:
		print(a+', I invite you to join the research')
