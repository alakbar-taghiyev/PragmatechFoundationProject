""" print('hello world')
print('helloworld')
print('hello\nworld') 

a=3 #int
b=3.5 #float
c= "helloworld" #string
d= [1,2,3, "world"] #list
e= (1,2,3, "world") #tuple
f= {"Alik":22, "Aida":19} #dict
# g = true, false #bool
print(type(d))  #deyishenin novu
 """

""" print(10/4)
print(10//4)
print(-10//4)
print(-10/4)
print(-9//4)
print(-7//4) 
print(-10%3)
print(-15%2) """

""" print("Aida"*5)
print('hello'+'Aida')
print("*"*2) """

# a="Python"

# b=[1,2,3,4,"Aida"]

""" 
print(a[3]) #h
print(a[5]) #n
print(b[0]) #1
print(b[4]) #Aida """

""" print(len(a))
print(b[len(b)-1])  """

""" print(b[0:5])
print(b[0:5:2])
print(b[1:])
print(b[:3])
print(b[0:4:2]) """

""" f= {
    "Alik":22, "Aida":19, "Samir":44
    }

x = f.keys()
y = f.items()
z= f.values()
print(x)
print(y)
print(z)
 """

""" a = int(input("eded daxil edin "))
b= int(input("Eded daxil edin "))
c = a+b
print('cavab:',c) """

""" a =int(input("bal daxil edin"))

if a>90&a<100:
    print("Netice yuksekdir")
elif a>70&a<90:
    print('Netice kafidir')
else:
    print('Kesildiniz') """

""" n = int(input())

if not(n%2 !=0):
    print('Tek edeler olur')
else:
    print('cut ededdir') """

""" i=0
while i<=10:
    if i==5:
        i+=1
        continue
    print(i)
    i+=1 #i=i+1 """
    
""" i=20
while i<=50:
    print(i)
    i+=5  """

""" i=1
while i<1000:
    print(i)
    i*=2 """

""" a = [1,2,3,4,5,6,7,8,9,10,24]
for i in a:
    print(i,end="") """

""" b = "PragmatechEducation"
for i in b:
    print(i) """

""" for i in range(10,100,2):
    print(i) """

#range (10) yazdiqda default olaraq 0-dan 10-a qeder goturur

""" for i in range (1,20):
    if i%3==0: 
        print( i,  "Ededler 3-e tam bolunur") """

""" def my_function():
    print("hello Aida")

my_function() """

""" def my_function(basqa_birshey):
    print("hello",basqa_birshey)

my_function("Alik")
my_function("Aida")


def myFunction(model="bmw"):
    print("Mashin:",model)

myFunction("BMW")
myFunction("07")
myFunction("AUDI")
myFunction("Qazel")
myFunction("Kamaz")
myFunction() """

""" def toplam(a,b):
    print(a+b)

toplam(2,7) """

