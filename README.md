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


# Histograms

A histogram plot shows the underlying frequency distribution of a set of continuous data. I created the histograms for analysing each variable from the data set in Matplotlib using the following code.

	IMAGE - CODE
	
	
	
	IMAGE - OUTPUT

 
     
Observations:

Histograms illustrate the shape of the distribution of each feature per species and provide a more accurate depiction by showing a visual breakdown of where the data lies. By looking at the overall distribution of the data it is easy to see petal length and petal width do not have a normal distribution. This is because the Iris Setosa petal length and width are situated on the far left of the graph making it easy to separate Setosa from the other two species. By using sepal length and sepal width we can not separate one species from another as the distribution is over lapping.


# Scatterplots
Scatterplots are used to identify trends within the data. They plot data points on a horizontal and vertical axis to demonstrate how one variable is affected by another. The relationship between two variables is called their correlation.

	IMAGE - CODE
	
	
	IMAGE - PLOTS
  

Observations:

Here we can see from the graphs that there seems to be a positive correlation between the length and width of all species but there is a particularly strong correlation between Petal length and Petal width. There is also a distinct difference in size between the three species and by looking at Petal length and Petal width we can clearly see that the iris Setosa is un-doubtedly smaller than the Versicolor and Virginica. This difference can be seen again with Sepal length and Sepal width. Once again there is an overlapping with the Versicolor and Virginica but in both cases the Virginica seems to be the largest of the three species.


# Pairplot

Pairplots enable us to quickly see the relationships between variables across multiple di-mensions using scatterplots and histograms. It produces a matrix of relationships between each variable in your data allowing for an instant examination. The pairplot allow us to see the scatter plot between any two features within the data set.

	IMAGE - CODE
	
	
	IMAGE - PLOTS
 

Observations:

From a quick glance of the graphs it can be easily seen that the distribution of data for Iris Setosa is very different from Iris Versicolor and Iris Virginica again making it very easy to separate from the other two species. 

There seems to be a positive trend between Sepal length and Petal length as the graph shows an uphill pattern from left to right. The same can be said for Petal length in relation to Sepal length and Petal width. Petal width also displays a strong positive relationship with Petal length in the graph.


# Boxplots
Box plots are a type of chart often used in explanatory data analysis to visually show the dis-tribution of numerical data and skewness through displaying the data quartiles and averag-es. Box plots are useful as they provide a visual summary of the data enabling researchers to quickly identify mean values, the dispersion of the data set, and signs of skewness [13].

	IMAGE - CODE
	
	
	IMAGE - PLOTS
 

    
Observations:

The boxplots show a wider range in data for Petal length and Petal width when compared with Sepal length and Sepal width. It can be seen that the Iris Virginica has the greatest range within Sepal length while the Iris Setosa has the biggest range of Sepal width. The range of Petal width is not great amongst the three species with Iris Setosa been very small in range when compared to the other two species.


# Violinplots

A voilin plot is used to visualise the distribution of the data and its probability density. The thick black bar in the center represents the interquartile range, the thin black line ex-tended from it represents the 95% confidence intervals, and the white dot is the median [14]. 

	IMAGE - CODE
	
	IMAGE - PLOTS
  
   
Observations:

It can be seen from the violinplots that the Iris Virginica has the highest median value be-tween the three species when it comes to Petal length, Petal width and Sepal length. The Iris Setosa shows the greatest median value for Sepal width and also shows a considerable dif-ference between when comparing its Sepal length and width with its Petal length and width. 

# Swarmplots

A swarm plot is a categorical scatterplot with non-overlapping points. This gives a better representation of the distribution of values, although it does not scale as well to large num-bers of observations. A swarm plot can be drawn on its own, but it is also a good comple-ment to a box or violin plot in cases where you want to show all observations along with some representation of the underlying distribution[15].
 	
	IMAGE - CODE
	
	IMAGE - PLOT

 
Observations:

From the graph it is easy to again separate the Iris Setosa from the other two species in re-lation to Petal length and width. Iris Virginica has the greatest range for Sepal length, Petal length and Petal width while Sepal width shows a much shorter range between all three species. The overlapping with Sepal length and sepal width makes it difficult to separate the three species especially with Iris Virginica and Iris Versicolor.


