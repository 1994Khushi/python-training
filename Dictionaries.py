                       #todo NUMBERS
m= (60 + (10 ** 2) / 4*7) -134.75
print(m)
a= 4 * (6+5)
print(a)
b = 4 * 6 + 5
print(b)
c= 4 + 6 * 5
print(c)
print(m + a + b + c)
d =  3 + 1.5 + 5
print(d)
                        #TODO FLOATING POINT NUMBER
E = 100 ** 0.5            # SQUARE ROOT
print(E)
F= 10 ** 2                # SQUARE
print(F)
                        #TODO strings
g = 'HELLO'
print(g[1] , g[4])
print(g[ ::-1])          # REVERSE STRING using slicing
print(g[-4])             # reverse letter indexing
h= [0] *3
print(h)
list2 = [0,0,0]
print(list2)
list3 = 1,2,[3,4,'hello']
list3[2][2] = 'good bye'
print(list3)
                          #todo Sort
list4 = [5,3,4,6,1]
print(sorted(list4))
print(list4.sort())
                          #todo Dictionaries
j = { 'simple_key': 'Hello'}          # GRAB
print(j['simple_key'])
k ={'k1':{'k2': 'hello'}}
print(k['k1']['k2'])
l= {'k1':[{'nest_key':['this is deep', ['hello']]}]}
print(l['k1'][0]['nest_key'][1][0])
m= {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(m['k1'][2]['k2'][1]['tough'][2][0])

                     #todo TUPLES
n= (1,2,3)
print(n)
                             # todo SETS
o= [1,2,2,33,4,4,11,22,3,3,2]
print(set(o))
                                   #todo BOOLEANS
P= 2>3
print(P)
q= 3<=2
print(q)
r = 3==2.0
print(r)
s =3.0 ==3
print(s)
t= 4 ** 0.5 !=2
print(t)
u = [1,2,[3,4]]
u1 =[1,2,{'k1':4}]
print(u[2][0]>=u1[2]['k1'])
v= 2==2
print(v)
w = 2==1
print(w)
x= 'Hello'=='bye'
print(x)
y = 'bye'=='Bye'
print(y)
z = '2'==2
print(z)
a1= 2.0 == 2
print(a1)
b1 = 3!=3
print(b1)
c1=  4!= 5
print(c1)
d1= 2>1
print(d1)
e = 1>2
print(e)
f= 1<2
print(f)
g=2<5
print(g)
h= 2>=2
print(h)
i = 4<=1
print(i)