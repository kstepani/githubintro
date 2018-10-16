import random
import operator
import matplotlib.pyplot
agents=[]
#set up variables
#randomise starting points y0,x0
agents.append([random.randint(0,99),random.randint(0,99)])


#random walk one step y0
if random.random()<0.5:
    agents[0][0]+=1
else:
    agents[0][0]-=1
    
    
#random walk one step x0
if random.random()<0.5:
    agents[0][1]+=1
else:
    agents[0][1]-=1

print (agents[0][0],agents[0][1])


#random walk one step y0
if random.random()<0.5:
    agents[0][0]+=1
else:
    agents[0][0]-=1
    
    
#random walk one step x0
if random.random()<0.5:
    agents[0][1]+=1
else:
    agents[0][1]-=1
print (agents[0][0],agents[0][1])


# second set of points y1,x1
agents.append([random.randint(0,99),random.randint(0,99)])

#random walk one step y1
if random.random()<0.5:
    agents[1][0]+=1
else:
    agents[1][0]-=1
    
    
#random walk one step x1
if random.random()<0.5:
    agents[1][1]+=1
else:
    agents[1][1]-=1

print (agents[1][0],agents[1][1])


#random walk one step y1
if random.random()<0.5:
    agents[1][0]+=1
else:
    agents[1][0]-=1
    
    
#random walk one step x1
if random.random()<0.5:
    agents[1][1]+=1
else:
    agents[1][1]-=1
    
print (agents[1][0],agents[1][1])

distance=((agents[0][0]-agents[1][0])**2+(agents[0][1]-agents[1][1])**2)**0.5
print (distance)
max=max(agents,key=operator.itemgetter(1))

matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.scatter(agents[0][1],agents[0][0])
matplotlib.pyplot.scatter(agents[1][1],agents[1][0])
matplotlib.pyplot.scatter(max[1],max[0], color='red')
matplotlib.pyplot.show()

