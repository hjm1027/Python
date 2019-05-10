current_users=['as','df','zx','xc','cv']
new_users=['qw','we','AS','XC','GH']
for users in new_users:
	if users.lower() in current_users:
		print('You have to input another name')
	else:
		print("This name haven't been used yet")
