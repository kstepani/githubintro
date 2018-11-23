import random
import operator
import matplotlib.pyplot
import agentframework
import csv

#read the csv file and create a 2D List


with open('in.txt', newline='') as f:
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    environment=[]
    for row in reader:
        rowlist=[]
        for value in row:
            rowlist.append(value)
        environment.append(rowlist)
        
#plot the raster image
matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.show()            

            
num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20

agents = []

# Make the agents linking them with the environment and also the list of agents
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment,agents,neighbourhood))


# Move the agents.
for j in range(num_of_iterations):
    random.shuffle(agents)
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)


#plot the agents and the environment
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
matplotlib.pyplot.show()


        
