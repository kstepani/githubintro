import random

#set up variables
y0=50
x0=50
print (y0)
print (x0)


#random walk one step y0
if random.random()<0.5:
    y0=y0+1
else:
    y0=y0-1
    
    
#random walk one step x0
if random.random()<0.5:
    x0+=1
else:
    x0-=1

print (y0,x0)


#random walk one step y0
if random.random()<0.5:
    y0=y0+1
else:
    y0=y0-1
    
    
#random walk one step x0
if random.random()<0.5:
    x0+=1
else:
    x0-=1
print (y0,x0)


#second set of point
#set up variables
y1=50
x1=50
print (y1)
print (x1)


#random walk one step y0
if random.random()<0.5:
    y1=y1+1
else:
    y1=y1-1
    
    
#random walk one step x0
if random.random()<0.5:
    x1+=1
else:
    x1-=1

print (y1,x1)


#random walk one step y0
if random.random()<0.5:
    y1=y1+1
else:
    y1=y1-1
    
    
#random walk one step x0
if random.random()<0.5:
    x1+=1
else:
    x1-=1
print (y1,x1)

distance=((y0-y1)**2+(x0-x1)**2)**0.5
print (distance)

#randomise 100x100 grid 
#set up variables
y2=10
x2=60
print (y2)
print (x2)


#random walk one step y2
if random.randint(0,99)<50:
    y2=y2+10
else:
    y2=y2-10
    
    
#random walk one step x2
if random.randint(0,99)<50:
    x2+=10
else:
    x2-=10

print (y2,x2)


#random walk one step y2
if random.randint(0,99)<50:
    y2=y2+10
else:
    y2=y2-10
    
    
#random walk one step x2
if random.randint(0,99)<50:
    x2+=10
else:
    x2-=10
print (y2,x2)


#second set of point
#set up variables
y3=20
x3=70
print (y3)
print (x3)


#random walk one step y3
if random.randint(0,99)<50:
    y3=y3+10
else:
    y3=y3-10
    
    
#random walk one step x3
if random.randint(0,99)<50:
    x3+=10
else:
    x3-=10

print (y3,x3)


#random walk one step y3
if random.randint(0,99)<50:
    y3=y3+10
else:
    y3=y3-10
    
    
#random walk one step x3
if random.randint(0,99)<50:
    x3+=10
else:
    x3-=10
print (y3,x3)

distance=((y2-y3)**2+(x2-x3)**2)**0.5
print (distance)
