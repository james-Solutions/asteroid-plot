# A Look at Asteroid Data with Sage

## - Data Analysis Project -

## By James Bromley

### March 17, 2019


## 1 Introduction

For my Data Analysis project I decided to look at Asteroid Orbital data. Particularly those defined
as close approach. Which are those that pass within 0.2AU of Earth and have an absolute magnitude
brighter than 22.0. Description of the data, and the data set used is discussed in the Data section.

I did this primarily as I was interested in how many Asteroids come within a defined close
distance. I always knew that we of course had passerby’s in space, but I thought this would be a
good way to quantify it all. It was surprising to find so many, close 500 in the chosen data set! Of
course I wanted to see how many Asteroids would come near us by distance and time. Which is
what led to the creation of the plots in this project. This is discussed further in the section called
Plots. That includes as well the plots this project produced.

I used Python to create the plots in this project. Sage has a Notebook feature that allows
you to work in a workspace. Which is useful for smaller projects. However, for my data I felt that
working in Python would make handling the data easier. As I am used to working in compiled
languages this made the most sense to me. I have completed many projects of reading in simple
text file data, which helped learning to read csv data into Python easier.


## 2 Plots

I created two plots for this project. One is the Miss in AU vs Year Plot, or the distance plot. The
other is similar but with velocity, which is the Miss in AU vs Velocity, or velocity plot.

The distance plot is a Sage scatter plot object. It is interesting to note a higher visible
density until about the year 2040 +/-, after which the Asteroids become more sparse. As to why
this is, I am unsure. Speculation might lead me to believe that it is because other further out
Asteroids have not been detected. Since their light is not visible yet. But, this is still speculation.

![alt text](https://firebasestorage.googleapis.com/v0/b/react-portfolio-58cba.appspot.com/o/distance-plot.png?alt=media&token=3a6876c7-74bb-4438-a3c1-df13a5e5d331 "Distance-Plot")
```
Figure 1: Plot of Miss in AU vs Year Data
```

For the velocity plot, I devised a way programmatically to make the plot more visibly
pleasing. Which was to make 4 grouping of Asteroid speeds and setting each group to a color in
the scatter plot. Where green is the slowest group of Asteroids, and of course red is the fastest. To
do this required parsing of the data in Python, explained more so in the Python section.

![alt text](https://firebasestorage.googleapis.com/v0/b/react-portfolio-58cba.appspot.com/o/velocity-plot.png?alt=media&token=ad29a4e5-86ba-49be-91d5-6a187e48a882 "Distance-Plot")
```
Figure 2: Plot of Miss in AU vs Velocity Data
```
## 3 Python Code

This one of my first more in depth projects with Python. I had some prior experience but this
strengthened well. The reading in of csv data with Python compared to text files with C++ was
very easy. Allowing me to access the csv row and add that attribute to my Asteroid class.

I originally thought about utilizing the bubble sort to sort the data based on velocity.
However, thinking about efficiency I decided another strategy would be better. Which was to find
a max and minimum velocity, then assign groups based on these values. Which would take less time
than a bubble sort would require, primarily fewer loops to get the data in a manageable format.

Working with Sage in this manner helped me clarify its usefulness. I can now imagine
ways of creating functions to manipulate data with sage and interacting with sage objects. This
experience will help me with future projects.

## 4 Data

The full data set is available here in the file data.csv. For descriptions of the columns visit the 
column description file. The full dataset and many more like this are at the Planetary Data 
System Asteroid Orbital Data[1]. My project primarily looked at the year, miss in AU and velocity 
fields from this data. This data can easily be broken into monthly and yearly in the future for analysis.

## References

[1] M. S. W. Keesey. (1999). Earth-asteroid close approaches, [Online]. Available:https://sbn.
psi.edu/pds/resource/earthapp.html(visited on 02/23/2019).


