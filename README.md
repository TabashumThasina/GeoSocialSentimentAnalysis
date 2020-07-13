Main element of geo-social data is social media (Facebook, Twitter) 
with geo location. Online users and geographical activities are sequences
of data points with latitude longitude records. This study combines data, 
assessing and visualizing sentiments related to big impact event in 
geographically confined population. News web sites and social media users’ 
comments were retrieved to analysis sentiment and results are visualized.

The objective of this work is to understand how people perceive
high impact events reported in news by integrating and analyzing
social and socio-economic data.

# Data Collection
To detect similar topics on several news paper, we scrapped
whole news article from the local bangla news portal.
For scrapping the articles, Beautiful Soup package of Python has been
used which parsed HTML documents of the news article.

# Data Filtering
Translating Bangla to English:
As 90% data are in Bangla, this module excludes all the HTML tag from
web scrapped news article then translates into English.
Comments are also translated into English with the help of Py-Translate
package of Python.

# Topic Analysis
In this study we computed Minhash Signature. In the following figure
we computed 12 news articles from our translated dataset and
found the similar topics. From the figure if news articles have similar
H1 and H2 value then the articles are under a same topic.

# Sentiment Analysis:
Comments dataset are proceed to analyze the sentiment combining
five classifier Naïve Bayes, Mulltinomial NB, Bernoulli NB, Logistic
Regression and Linear SVC.
For each classification it is treated as a vote. Then we took the mode of
the votes which will return the most popular votes. We will call this
confidence 
Trained the algorithm with already existing training set of movie reviews positive and
negative.

# Location Clustering
In this Study we clustered the latitudes and longitudes with K-means
clustering.
After clustering locations, we calculated the mean sentiment of that
cluster and displayed the clustering on that corresponding graph.


