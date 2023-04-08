print('This is a string {}'.format('INSERTED'))
print('the {2} {1} {0}'.format('fox','brown','quick'))
print('the {2} {2} {2}'.format('fox','brown','quick'))
print('the {f} {b} {q}'.format(f='fox',b='brown',q='quick'))
"""FLOAT FORMATTING FALLOWS "{VALUE:WIDTH.PRECISION F}"  """
result=100/7
print(result)
print("The result was = {r}".format(r=result))
print("The result was = {r:10.3f}".format(r=result))

name="Harsha"
print(f'Hello, her name is {name}.')
name="Deepa"
age=23
print(f'{name} is {age} years old.')


