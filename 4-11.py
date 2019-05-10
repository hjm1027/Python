names=['asd','dfg','qwre']
for name in names:
	print('I love '+name+' pizza')
friend_pizzas=names[:]
friend_pizzas.append('sdf')
print("My favorite pizzas are:")
for a in names:
	print(a)
print("My friend's favorite pizzas are:")
for b in friend_pizzas:
	print(b)
