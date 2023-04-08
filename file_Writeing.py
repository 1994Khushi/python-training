f = open("khushi.txt", 'rt')
#content = f.read()
#print(content)
#for line in content:
 #   print(line)        """ for character by character print"""
#for line in f:
#    print(line, end="")    """ for line by line print by default"""
#print(f.readline())        """ for read new line character"""
#print(f.readline())
#print(f.readlines())     """ for read list print """
#content = f.read(3)
#print(content)
#content = f.read(34455222)
#print('1',content)
print(f.seek(0))
print(f.read())

f.close()