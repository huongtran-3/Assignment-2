#!/usr/bin/env python
# coding: utf-8

# In[2]:


# The algorithm for the model:

# 1. Set up the environment
#    1.1 Create the list
#    1.2 Read the raster data
#    1.3 Put drunk.plan file csv into rows.
#    1.4 Locate the pubs and returns its position.
#    1.5 Check how the environment looks

# 2. Create drunk model and name drunks
#    2.1 Create the list of drunks.
#    2.2 Create the number of drunks and iterations.
#    2.3 Code to size the plot and animating.
#    2.4 Create and name drunks

# 3. Move the drunks and draw the density
#    3.1 Creating a list with the coordinates of every drunks (no. drunks, x, y)
#    3.2 Creating a text file with the coordinates of evety drunks
#    3.3 Plot to check if the model works

# 4. Save the density map to a file as text


# First, we import all packages we will need for the model.
import csv
import matplotlib.pyplot
import matplotlib.animation
import drunkframework

# 1. Set up the environment.
# 1.1 Create the list.
environment = []

# 1.2 Read the raster data.
f = open('drunk.txt', newline='')
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)

# 1.3 Put drunk.plan file csv into rows.
for row in reader:
    rowlist =[]
    for value in row:
        rowlist.append(value)
    environment.append(rowlist)
f.close()

# 1.4 Locate the pubs and returns its position.
row_counter = 0
for row in environment:
    for value in row:
        if value != 0:
            x = row.index(value)
            y = row_counter
            #print("pub at coordinates","x =", x, "y =", y)
            
    row_counter += 1


# 1.5 Check how the environment looks.

matplotlib.pyplot.xlim(0, 300)
matplotlib.pyplot.ylim(0, 300)
matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.show()
    

# 2. Create drunk model and name drunks

# 2.1 Create the list of drunks.
drunks = []

# 2.2 Create the number of drunks and iterations.
num_of_drunks = 25; # There are 25 drunks in the town name from 1 to 25, and their home from 100 to 250 repectively.
num_of_iterations = 100000 # There are unlimited step unti drunks reach their home, I assmue drunks do 100000 iterations

# 2.3 Code to size the plot and animating.
fig = matplotlib.pyplot.figure(figsize=(5, 5))
ax = fig.add_axes([0, 0, 1, 1])

# 2.4 Create and name drunks
for i in range(num_of_drunks):
    name = ((1+i)*10) # Python starts in 0 we have to add 1 first and then just multiply by 10.
#   print(name) # test names are correct.
    drunks.append(drunkframework.Drunk(environment, drunks, name))
    
    
# 3. Move the drunks and draw the density.
for i in range (num_of_drunks):
    drunk = drunks[i]
    for j in range(num_of_iterations):
        if environment [drunk.y][drunk.x] != drunk.name: 
            drunks[i].move()
            drunks[i].steps()

        
# 3.1 Creating a list with the coordinates of every drunks (no.drunks, x, y)
drunks_location = []
for p in range(num_of_drunks):
    no_drunks = [] 
    no_drunks.append(p + 1)
    no_drunks.append(drunks[p].x)
    no_drunks.append(drunks[p].y)   
    drunks_location.append(no_drunks)             
            
# 3.2 Creating a text file with the coordinates of every drunks
with open('planningfordrunk.txt', 'w', newline='') as f:
    csvwriter = csv.writer(f, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
    csvwriter.writerow(["drunks","x","y"])
    for row in drunks_location:
        csvwriter.writerow(row)
              

# 3.3 Plot to check if the model works
matplotlib.pyplot.xlim(0,300)
matplotlib.pyplot.ylim(0,300)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_drunks):
    matplotlib.pyplot.scatter(drunks[i].x,drunks[i].y)

matplotlib.pyplot.show()

# 4. Save the density map to a file as text.
with open('drunks_environment.density.txt', 'w', newline='') as f:
    csvwriter = csv.writer(f, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
    for row in environment:
        csvwriter.writerow(row)


# In[ ]:




