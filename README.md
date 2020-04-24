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

![Iris.png](https://github.com/dconn20/Project2020/blob/master/Images/Iris.png)
    

# Exploring the Data

As a starting point I wanted to output some basic statistics about the data. I ran a script to output the number of different species contained in the data set. Then I used the pandas .describe module as it generates some descriptive statistics from the data set, allowing for us to view the Count, Min, Max, Mean, Median and Standard Deviation. 

![Image](https://github.com/dconn20/Project2020/blob/master/code1.PNG)
    
    
![Summary](https://github.com/dconn20/Project2020/blob/master/Images/Summary1.PNG?raw=true)

 
 

To examine the differences across species, the same summary statistics were generated per species using the .groupby module on the categorical species variables.


![Groupby](https://github.com/dconn20/Project2020/blob/master/Images/code2.PNG?raw=true)
    
    
 
![GroupSum](https://github.com/dconn20/Project2020/blob/master/Images/code3.PNG?raw=true)

 

The statistics tables are a nice way of allowing us to view the data clearly and more easily.  Already we can see there is a big range in the size of the Sepal Length and Petal Length. The Petal length ranges from 1.0 - 6.9, meaning there is a difference of approx. 5.9cm between the min and max values. This would be the category that covers the largest range of the data. Whereas the other categories range is as follows: Sepal Length - 3.6cm, Sepal Width - 2.4cm, Petal Width - 2.4cm.


# Histograms

A histogram plot shows the underlying frequency distribution of a set of continuous data. I created the histograms for analysing each variable from the data set in Matplotlib using the following code.

![Hist.code](https://github.com/dconn20/Project2020/blob/master/Images/Hist.code.PNG?raw=true)
	
	
	
![Histograms](

 
     
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


# Conclusion

The aim of this project was to research Fisher’s Iris Data Set by using Python and its differ-ent libraries to analyse it. Throughout this process the libraries I mainly used were Pan-das, Seaborn, Matplotlib and Numpy. I began this project by researching the huge amount of information available in relation to the data set online. From this research it is clear to see that Fisher’s Iris Data Set is one of the best known and most used data sets in relation to Machine Learning and Data Science. 

From my investigations I believe that visual data is a much better platform from which to study data. I found it made the data more clear and easier to visualise and it seemed more  accurate and reliable. Graphs such as the histogram allow you to view the data but do not give a good range of the overall data set. Using scatterplots and pairplots allowed me to view the data in a different way and separate it from each other more easily. I also created boxplots and violinplots to help me analyse the data more thoroughly. These were some-thing I came across quite often during my research and decided to add them to the project in order to gain experience creating them within Python and using them to study the data. 

Throughout this project I have learned a huge amount in relation to programming and how it is used to analyse data sets. Before starting this course in January, I had no previous pro-gramming experience and found the weekly tasks to be quite challenging. This project really helped me to understand Python and its different libraries. I spent quite a bit of time run-ning, testing and altering code I had written in order to produce the correct results. I en-countered many errors over the course of this project but found solutions to each one along the way. I am happy with the content that I have produced as I found it both challenging and rewarding. I have achieved what I set out to do at the beginning of the project, which was to understand the data set and develop the skills needed to analyse it by writing and executing scripts within Python and its libraries. I have gained valuable experience using Pandas, Sea-born, Matplotlib and Numpy and learned how to create visual graphs such as histograms, scatterplots, pairplots, boxplots, violinplots and swarmplots. I also gained important experi-ence using Visual Studio Code and Github. 





# REFERENCES:

1.	https://www.anaconda.com/

2.	https://code.visualstudio.com/

3.	https://www.python.org/

4.	https://matplotlib.org/

5.	https://pandas.pydata.org/

6.	https://cs231n.github.io/python-numpy-tutorial/

7.	https://seaborn.pydata.org/

8.	https://github.com/

9.	https://medium.com/@avulurivenkatasaireddy/exploratory-data-analysis-of-iris-data-set-using-python-823e54110d2d

10.	https://pythonhosted.org/bob/temp/bob.db.iris/doc/example.html

11.	Anderson, E. (1936). The species problem in Iris. Annals of the Missouri Botanical Garden, 23(3), 457-509.

12.	Runkler, T. A. (2012). Chapter 2: Data and Relations. Models and Algorithms for Intelligent Data Analysis. Vieweg and Teubner 		Verlag.

13.	https://www.simplypsychology.org/boxplots.html 

14.	https://datavizcatalogue.com/methods/violin_plot.html

15.	https://kite.com/python/docs/seaborn.swarmplot



# Bibliography:

https://www.academia.edu/13069408/Report_on_Edgar_Anderson_s_Iris_Data_Analysis

https://realpython.com/python-histograms/

https://www.programming-techniques.com/2019/05/python-program-to-copy-the-contents-of-a-file-to-another-file.html

https://www.datacamp.com/community/tutorials/histograms-matplotlib

https://stackoverflow.com/questions/44119653/creating-a-boxplot-with-matplotlib

https://rpubs.com/AjinkyaUC/Iris_DataSet

https://medium.com/@avulurivenkatasaireddy/exploratory-data-analysis-of-iris-data-set-using-python-823e54110d2d

https://kite.com/python/docs/sys.stdout

https://www.codegrepper.com/code-examples/python/reading+and+writing+data+in+a+text+file+with+python

https://www.geeksforgeeks.org/reading-writing-text-files-python/

https://matplotlib.org/

http://blog.bharatbhole.com/creating-boxplots-with-matplotlib/

http://statweb.stanford.edu/~jtaylo/courses/stats202/visualization.html

https://problemsolvingwithpython.com/06-Plotting-with-Matplotlib/06.04-Saving-Plots/

https://rpubs.com/AjinkyaUC/Iris_DataSet

https://www.sciencedirect.com/topics/mathematics/iris-data

https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html

https://datacarpentry.org/image-processing/05-creating-histograms/

https://stackoverflow.com/questions/51458892/how-to-view-the-whole-table

https://www.surveysystem.com/correlation.htm

https://pythonspot.com/matplotlib-scatterplot/

https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html

https://kaggle.com/jchen2186/machine-learning-with-iris-dataset

https://www.kaggle.com/danalexandru/simple-analysis-of-iris-dataset

https://www.kaggle.com/lalitharajesh/iris-dataset-exploratory-data-analysis.com

https://www.kaggle.com/ekapylski/iris-dataset-visualization

https://www.kaggle.com/abhishekkrg/python-iris-data-visualization-and-explanation




