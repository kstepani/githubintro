import random
import operator
import matplotlib.pyplot
import time
start = time.clock()
#define distance function
def distance_between(agents_row_a, agents_row_b):
    dist=((agents_row_a[0]-agents_row_b[0])**2+(agents_row_a[1]-agents_row_b[1])**2)**0.5
    return dist
    
    
num_of_agents=10
num_of_iterations=100
agents=[]
distances=[]
#make agents
for i in range(num_of_agents):
    agents.append([random.randint(0,100),random.randint(0,100)])
#move agents
for j in range(num_of_iterations):    
    for i in range(num_of_agents):
    
        if random.random()<0.5:
            agents[i][0] = (agents[i][0] + 1) % 100
        else:
            agents[i][0] = (agents[i][0] - 1) % 100
            
                 
        if random.random()<0.5:
            agents[i][1] = (agents[i][1] + 1) % 100
        else:
            agents[i][1] = (agents[i][1] - 1) % 100
                    


matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
matplotlib.pyplot.show()

#call distance function
for i in range(num_of_agents):
    for j in range(num_of_agents):
        if i!=j and i<j:
            distance = distance_between(agents[i],agents[j])
            print(i,j,distance)
            distances.append(distance)
#find max and min distance
max_dist=max(distances)
min_dist=min(distances)

end = time.clock()
print("time = " + str(end - start))