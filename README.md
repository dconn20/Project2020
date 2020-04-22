# Project2020


# Intro
This project is being undertaken as part of my final submission for the module 'Programming and Scripting' as part of my course ‘Higher Diploma in Computer Science with Data Analytics’. 
The purpose of this project is to investigate ‘The Iris Flower Data Set’ and prove my understanding of the data set. I intend to research the data set and write documentation to support my findings. I will write code and run scripts within Python that I will use to investigate it and then provide written support of my views and knowledge of the data set.

# Technology Used
Anaconda is the standard platform for Python data science, leading in open source innova-tion for machine learning.[1]

Visual Studio Code is a source-code editor developed by Microsoft for Windows, Linux and macOS.[2]

Python Programming Language is an interpreted, high-level, general-purpose programming language[3]

Matplotlib is a comprehensive library for creating static, animated, and interactive visuali-zations in Python.[4]

Pandas is a software library written for the Python programming language for data manipu-lation and analysis.[5]

NumPy is the fundamental package for scientific computing with Python[6]

Seaborn is a Python visualization library based on matplotlib. It provides a high-level inter-face for drawing attractive statistical graphics.[7]

GitHub is a web-based version-control and collaboration platform for software developers.[8]



# Summary

The Iris flower data set or Fisher's Iris data set is a multivariate data set introduced by the British statistician and biologist Ronald Fisher for his 1936 paper "The use of multiple measurements in taxonomic problems" as an example of linear discriminant analysis [9]. It is sometimes called Anderson’s Iris data set because Edgar Anderson collected the data to quantify the morphologic variation of Iris flowers of three related species [10]. 
The data set consists of 50 samples from three different species of Iris, they are: Iris Setosa, Iris Virginica and Iris Versicolor. Four features were measured from each sample: the length and the width of the sepals and petals, in centimetres. Based on the combination of these four features, Fisher developed a linear discriminant model to distinguish the species from each other [9]. 
Two of the species, I. setosa and I. versicolor were collected on the Gaspé Peninsula, Quebec, Canada "all from the same pasture, and picked on the same day and measured at the same time by the same person with the same apparatus", and published by Edgar in 1935 [11]. It is presumed that the same apparatus and rigor were applied to the measurement of I. virginica before Edgar shared the data with the British statistician and biologist Sir Ronald Aylmer Fisher in 1936 [11]. 
The data set was originally used by Fisher as an example for multivariate discriminate analyses but since then it has become one of the most widely used reference data sets for classification and prediction studies, and more recently for machine learning approaches to clustering, classification and pattern recognition [12].
    
    IMAGE

# Exploring the Data

As a starting point I wanted to output some basic statistics about the data. I ran a script to output the number of different species contained in the data set. Then I used the pandas .describe module as it generates some descriptive statistics from the data set, allowing for us to view the Count, Min, Max, Mean, Median and Standard Deviation. 
		
    IMAGE - CODE
    
    
 
    IMAGE - OUTPUT
 
 

To examine the differences across species, the same summary statistics were generated per species using the .groupby module on the categorical species variables.


    IMAGE - CODE
    
    
 
    IMAGE - OUTPUT

 

The statistics tables are a nice way of allowing us to view the data clearly and more easily.  Already we can see there is a big range in the size of the Sepal Length and Petal Length. The Petal length ranges from 1.0 - 6.9, meaning there is a difference of approx. 5.9cm between the min and max values. This would be the category that covers the largest range of the data. Whereas the other categories range is as follows: Sepal Length - 3.6cm, Sepal Width - 2.4cm, Petal Width - 2.4cm.


