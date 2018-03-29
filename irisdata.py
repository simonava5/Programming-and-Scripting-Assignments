# Simona Vasiliauskaite
# 02/03/2018
# Exercise 5 - Formatting Iris Data Set

# The data set consists of 50 samples from each of three
# species of Iris (Iris setosa, Iris virginica and Iris versicolor)

with open('data/iris.csv') as f: #opens the file iris csv which is saved on my device
    for line in f: #loops through each line
        n = line.split(',') #splits each line into a list
        print(n[0],n[1],n[2],n[3])   

   

