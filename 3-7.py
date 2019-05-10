names=['Jim','Tom','Tina']
b='invite '
print(b+names[0])
print(b+names[1])
print(b+names[2])
print("\nJim can not come\n")
names[0]='Jenny'
print(b+names[0])
print(b+names[1])
print(b+names[2])
print("\nI have found a bigger canzhuo\n")
names.insert(0,'Tony')
names.insert(0,'Hjm')
names.append('asd')
for name in names:
	print (b+name)
print ('I can only invite 2 people')
namespop=names.pop(-1)
print('Sorry,I cannot invite '+namespop)
namespop=names.pop(-1)
print('Sorry,I cannot invite '+namespop)
namespop=names.pop(-1)
print('Sorry,I cannot invite '+namespop)
namespop=names.pop(-1)
print('Sorry,I cannot invite '+namespop)
for name in names:
	print ('I can invite ' + name)
del names[0]
del names[0]
print (names)
