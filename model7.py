import random
import operator
import matplotlib.pyplot
import agentframework
import csv
import matplotlib.animation

#read the csv file and create a 2D List
with open('in.txt', newline='') as f:
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    environment=[]
    for row in reader:
        rowlist=[]
        for value in row:
            rowlist.append(value)
        environment.append(rowlist)
                   
         
num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20
agents = []

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])
#ax.set_autoscale_on(False)


# Make the agents,link them with the environment and the list of agents
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment,agents,neighbourhood))


carry_on = True

def update(frame_number):
    
    fig.clear() 
    global carry_on
      
    # Move the agents and make them interact with the environment and with each other
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)

    if random.random() < 0.1:
        carry_on = False
        print("stopping condition")
    
    #plot the agents and the environment
    matplotlib.pyplot.xlim(0, 99)
    matplotlib.pyplot.ylim(0, 99)
    matplotlib.pyplot.imshow(environment)
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
        
def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < 10) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1

animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=10)
animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)                                                       
matplotlib.pyplot.show()


        
