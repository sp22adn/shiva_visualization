#import the python libraries in directory
import pandas as pd  #Importing pandas and pyplot
import matplotlib.pyplot as plt
data=pd.read_csv("spi_matches_latest.csv")# reading the dataset
data.info() # displaying the info about the data frame

#line plots, first a single line plot is plotted in between prob1 and score 1
x_ax=data["prob1"]
y_ax_1=data["score1"]
plt.plot(x_ax,y_ax_1)
plt.xlabel("probability of home team winning")
plt.ylabel("points scored by home team")
plt.show

def mult_plot(x,y1,y2): #defining  a function to plot 2 line plots in the same graph
  vect=[y1,y2]
  for i in vect:                
    plt.plot(data[x],data[i])
  
  plt.xlabel(x)
  plt.legend((y1,y2), loc='upper right', shadow=True)
  plt.show  

mult_plot(x="prob1",y1="score1",y2="score2") #multi line plot

mult_plot(x="prob1",y1="xg1",y2="xg2") #multi line plot

mult_plot(x="prob1",y1="proj_score1",y2="proj_score2") #multi line plot

def mult_scatter(x,y1,y2): #defining a function to plot 2 scatter plots
  vect=[y1,y2]
  f=0
  for i in vect:      # plotting multiple scatter plots using for loop
    plt.figure(f)     # new figure window for each value of f
    plt.scatter(data[x],data[i])
    plt.xlabel(x)
    plt.ylabel(i)
    f=f+1

mult_scatter(x="prob1",y1="score1",y2="score2") #multiple scatter plot

mult_scatter(x="prob1",y1="xg1",y2="xg2") #multiple scatter plot

mult_scatter(x="prob1",y1="xg1",y2="xg2") #multiple scatter plot 
mult_scatter(x="prob1",y1="proj_score1",y2="proj_score2") #multiple scatter plot

def mult_hist(x1,x2,x3,x4): #defining
#a function to plot 4 independent histograms plots
  vect=[x1,x2,x3,x4]
  f=0
  for i in vect: # plots multiple histograms in different figure windows
    plt.figure(f)
    plt.hist(data[i],bins=100)
    plt.xlabel(i)
    # plt.ylabel(i)
    f=f+1

mult_hist(x1="prob1",x2="prob2",x3="xg1",x4="xg2") #plotting 4 histograms

mult_hist(x1="prob1",x2="prob2",x3="proj_score1",x4="proj_score2") #plotting 4 histograms

mult_hist(x1="prob1",x2="prob2",x3="score1",x4="score2") #plotting 4 histograms



