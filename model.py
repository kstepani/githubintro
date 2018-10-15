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
y0=random.randint(0,99)
x0=random.randint(0,99)
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
y1=random.randint(0,99)
x1=random.randint(0,99)
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

