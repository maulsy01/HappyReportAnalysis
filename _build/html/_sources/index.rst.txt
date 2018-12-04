.. Happy Report Analysis documentation master file, created by
   sphinx-quickstart on Tue Nov 13 11:45:08 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Happiness Report Analysis
=================================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

What does the world happiness look like?
-----------------------------------------
The main focus of our data analysis is answering "what does the world happiness look like?". Is it increasing, decreasing, or remaining the same? What regions of the world are happier? Which country is the happiest? What categories are highest for the happiest countries and/or regions? In general, we want to find the trends of happiness and those specific categories for each country and region over the past three years. Also, with this knowledge in mind, it may help us describe our future or explain how events in the world may affect happiness score. 

Data Acquisition
-----------------
The following data is from the Happiness Report data from `2015 <https://www.kaggle.com/unsdsn/world-happiness#2015.csv>`_, `2016 <https://www.kaggle.com/unsdsn/world-happiness#2016.csv>`_, and `2017 <https://www.kaggle.com/unsdsn/world-happiness#2017.csv>`_. Each of the datasets contain the country, their happiness score, and their happiness rate. Also, it shows the scores of each of the different categories that make up the happiness score. These scores for the categories added together make up the happiness score. These categories are: Distopia Residual, Economy (GDP per Capita), Family, Freedom, Generosity, Health (Life Expectancy), and Trust (Government Corruption). 


Cleaning the Data
-----------------
We obtained the Happiness Report data from 2015, 2016, and 2017. We wanted to combine the three datasets into one dataset. The columns in the 2017 data had to be changed in order to match the other two datasets. We also added a year column to each dataset so when we combined them we could be able to tell which year the data is from. We also needed to add a region column to the 2017 data using the other datasets because there was not a region column. 

Here is the code we used to create the region column:

.. code-block:: python

   h = happy15[['Country','Region']]
   countries = dict(h.values)
   happy17['Region'] = 'Region'
   for c in happy17.index:
       if happy17.at[c, 'Country'] in countries:
           happy17.at[c, 'Region'] = countries[happy17.at[c, 'Country']]
       else:
           happy17.at[c, 'Region'] = 'Unknown'

Now that all of the datasets had the same organization, we concatinated them into one dataframe using this code:

.. code-block:: python

   frames = [happy15, happy16, happy17]
   happy = pd.concat(frames)
   happy = happy.set_index(['Country'])
   happy = happy.reset_index()

Notebooks
------------
`This notebook <notebooks/Happiness\ Report.ipynb>`_  and `this notebook <notebooks/finalproject.ipynb>`_
contain the code for cleaning the datasets as well as the code for the following visualizations.

General Information
-------------------

We first wanted to know more general information about the data, such as what countries are the happiest and how have the countries changed over the years.

We started by generally looking at the difference in happiness score over the time period of 2015-2017.

The following plot shows the average happiness score in the world over 3 years. As one can see from the graph, the happiness score from 2015 to 2016 increases by around 0.010. However, from 2016-2017, the happiness score drops. Although the drop seems very signigicant on the line plot, it only drops around a happiness score of 0.030. Also, this is solely a drop of around 0.020 from 2015 to 2017. It is quite interesting, however, to note that happiness over the world is not just a continous increase.

|

.. figure:: images/happinessLine.png
    :width: 100%

|

Next, we wanted to see the top countries for happiness over three years, and whether or not they vary significantly.

The following bar plot shows the number of country appearances in the top 5 happiest countries over 2015-2017. The plot shows that only 6 countries in the world reach the top 5 happiest over three years. Therefore, the happiest countries remain relatively stable over the years. Four out of the six countries have been in the top 5 happiest countries every year. The only exceptions include Canada, with only 1 appearance, and Finland, with two appearances.

|

.. figure:: images/top5.png
    :width: 100%

|

We then wondered how the happiness of the different regions compare.

The following plot shows the average happiness score in each region in the year 2017. It shows that Western Europe, North America, and Australia and New Zealand have the highest average happiness scores, while Sub-Saharan Africa and Sourhtern Asia have the lowest average happiness scores.

|

.. figure:: images/regionbar.png
    :width: 100%

|

We, then, wondered whether the percent change of happiness score over the three years would have any specific trend for regions, countries, or with one of the 6 categories. So, we created a new data frame with percent change as a column.

The code to create the dataframe with percent change is shown below:

.. code-block:: python

   happy = pd.read_csv("http://knuth.luther.edu/~maulsy01/happy.csv")
   happy = happy.drop(columns=["Unnamed: 0"])
   # Create a dataframe that is just 2015 and 2017. Then split those into two seperate series,
   # then merge them back together.
   over_years = happy[happy["Year"] != 2016]
   over_years = happy[["Country", "Region", "Happiness Score", "Year"]]
   series_2015 = over_years[over_years["Year"] == 2015].drop(columns="Year")
   series_2017 = over_years[over_years["Year"] == 2017].drop(columns="Year")
   country_change = pd.merge(series_2015, series_2017, on='Country', how='outer')
   # Use the country_change dataframe, subtract happines score y and x, 
   # then divide it all by x and times it by 100. This gives
   # the percent change for each country over the three years.
   country_change["Percent Change"] = (country_change["Happiness Score_y"] \
   - country_change["Happiness Score_x"]) / country_change["Happiness Score_x"] * 100
   country_change = country_change.dropna().drop(columns="Region_y")\
   .sort_values(by="Percent Change", ascending=False)
   
With the new percent change dataframe, we wanted to see which countries had the top growth in happiness score, and which countries had the least growth in happiness score.

The following bar plot shows the highest and lowest growth of percent change over 2015-2017 for each country. The plot shows that Togo had the highest growth in happiness over the three years, followed by Senegal, Syria, Latvia, etc. The country with least growth is Central African Republic, followed by Venezuela, Liberia, Lesotho, etc. One intriguing find was that there were a couple countries from Africa on both the top growth and least growth. Also, a couple Latin America countries are in the least growth trend.

|

.. figure:: images/percentChangeBar.png
        :width: 100%

|

From the plot above's interesting finds of countries from specific regions, we decided to look further into that trend. So, we decided to plot the average percent score for each region in the world.
        
The following bar plot shows each region's percent change over 2015-2017. Australia and New Zealand, Eastern Asia, and Western Europe all seem to have increased slightly, but by not that much. Latin America and Caribbean drastically decreased compared to the other countries, while Southeastern Asia had the largest growth in happiness over the 3 years.

|     

.. figure:: images/regionPctChange.png
    :width: 100%

|

It only seemed logical to further look at percent change for each region with a scatter plot.

The following scatter plot has each point representing each country, labels it depending on the region, and plots it based on its average percent change of happiness score over 3 years. Western Europe seems to be relatively stable when it comes to percent change. However, Sub-Saharan Africa seems to change drastically with some countries with high percent changes, and some countries with the complete opposite change.

|

.. figure:: images/pctchangeScatter.png
    :width: 100%

|

Categorical Exploration
-----------------------

Our next question in our analysis was which areas of happiness are most important in forming the happiness score.

The following line plot shows the average mean score over every year for every category. Dystopia Residual went up in 2016 but dropped down in 2017, whereas family went down in 2016 but back up in 2017. Economy has slightly gone up over the years, but other than that the other categories are almost linear.

|

.. figure:: images/avgScoreByCategory.png
    :width: 100%

|

The following line plot takes the average score for each happiness rank over the past three years and plots them starting with rank 1 on the left. There is a lot more variation in the line for some of the ranks than what one would assume over three years. Of course, the general trends moves down as Happiness Rank gets larger.

|

.. figure:: images/avgScoreByCategoryRank.png
    :width: 100%

|

The following bar plot is seperated by each year, and for each year, there is a bar to represent the average score for one of the six categories. Over the years, dystopia residual has moved down, while family has increased. Other than that, the general shape for each years remains similiar.

|

.. figure:: images/avgScoreByCategoryBar.png
    :width: 100%

|

The following area plot shows the happiness score for the happiest country in 2015, 2016, and 2017 and the distribution of the categories that make up the score. It shows that the distopia residual makes up the largest portion of the score, while generosity and trust make up the smallest portions of the score.

|

.. figure:: images/areaplot.png
    :width: 100%

|

The following area plot shows the top 50 happiest countries in 2017 with their category distributions. There is relatively a pattern of what is typically the most important in creating the score, but there some variations.

|

.. figure:: images/areaplot2.png
    :width: 100%

|

The following bar plot is seperated by each region, and for each region, there is a bar to represent the average score for one of the six categories. 

|

.. figure:: images/regionCategoryBar.png
    :width: 100%

|

Correlations
-------------

We then wanted to look for correlations between the different categories of the happiness score.

The following is a scatter plot showing Economy vs Health with size relating to the rank and color relating to the score. The larger the circle the worse the rank, and the lighter the circle the higher the score. This scatter plot shows a very high correlation between economy and health.

|

.. figure:: images/healthvseconomy.png
    :width: 100%

|

The following is a scatter plot showing Family vs Freedom with size relating to the rank and color relating to the score in the same way as the previous plot. This plot shows there is not as high of a correlation between Freedom and Family compared to Economy and Health.

|

.. figure:: images/freedomvsfamily.png
    :width: 100%

|

The following plot shows the correlation between family score and trust score. This plot shows a small correlation between a negative relationship between family and trust.

|

.. figure:: images/trustVsFamily.png
    :width: 100%

|

The following plot shows the correlation between the different categories, total score, and rank. There is a high positive correlation between happiness score and almost every category, and there is a high negative correlation between happiness rank and almost every category, which is to be expected. Some other somewhat high correlations are economy and health, family and economy, and family and health.

|

.. figure:: images/correlation.png
    :width: 100%

|

Overall
---------
Finally, we wanted to be able to generalize our findings.

The following map shows the happiness score for countries on a map. I used code found on kaggle relating to this data set to assist in creating this map. The darker the country, the higher the happiness score. The map makes it easier to see that the happiest countries are in North America, Europe, and Australia/New Zealand, and the least happy countries are found in Africa and Southern Asia.

In order to interact with this graph, go to our jupiter notebooks linked above.

|

.. figure:: images/map.png
   :width: 100%

Conclusion
-----------

We have succeeded in answering our questions of which countries and regions have the highest and lowest happiness scores. We were able to see which areas of happiness contribute the most to rating a country's happiness.

One question we still have after our analysis is whether or not these scores accurately depict the happiness found within these countries and regions. Sadly, we wish we could find out potential causes or correlations from the Happiness score changes. However, it would be interesting to see if different types of past events affect each country. From this, it may be beneficial to predict changes in happiness score from current events.

Overall, the data analysis gave us interesting results that not only answered our questions, but presented us with questions we did not expect.
