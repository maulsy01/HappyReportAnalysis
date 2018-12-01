## Sydney Maule's Journal 

#### November 2, 2018
We started searching for a data set for our project. One of the initial thoughts we had was a data set relating to Game of Thrones data. 
There is a data set relating to the battles and deaths in Game of Thrones. Some other data sets I found that I thought might work were
college student meals, McDonald's menu calories, board game information, and Olympics data.

#### November 6, 2018
We decided on a data set that Sam found: US Traffic Fatality Records. Some possible questions we would like to answer with this data set 
are: What is correlated to crashes? Are certain days of the week, months, or years that are more common for accidents?

#### November 8, 2018
There are many different data sets available, and we looked through them all to decide which ones we wanted to use. We decided to use the
Accident data sets from 2015 and 2016 because they encompass the most interesting information. We will combine these two data sets into
one. 

After deciding this, we attempted to download the data. Kaggle will not allow download the data directly. It said we had to query the data
on Kaggle.

#### November 9, 2018
We were unable to figure out how to access the traffic fatality data. After some more searching for data sets, we decided to use the data
set World Happiness Report for the years 2015, 2016, and 2017. Some questions we would like to consider are: What are the happiest countries/regions? What factors have led
to this happiness? How has happiness changed over time? We then brainstormed ideas for what visualizations we wanted to do with our data.

#### November 13, 2018

While Sam worked on setting up the github website, I worked on cleaning and combining the data sets for the three years of data into one.
I had to change the column names in the 2017 data set so they are the same as the other two data sets. After I changed the column names, I 
added a column to each data set with the year so we will know the year after the data sets are combined. I then wanted to create a column in the 2017 data for region using the region information in the other data sets.

#### November 14, 2018

Around noon, I continued to try and create a region column for the 2017 data using the other data sets. I struggled to find a way to do this. I first tried using a for loop to create a new column. Then I created a dictionary of the countries and their regions, and I tried to use thisdictionary to add regions for the 2017 data with another loop. I then created a region column and just tried to change the values in the column. None of these attempts were successful.


At 3:30, we figured out how to use the new column. We needed .at instead of .loc because .loc was giving us a series and we needed it to
be an individual value. We then had to reset the index so there were not repeating values. I exported the csv to my public.html so we 
both have access to it. I then created an SSH key. Lastly, we divided up our planned visualizations.

#### November 15, 2018

In the morning, I created an area plot. I wanted to compare the values that go into the total score for the happiest country in each year. I created a data frame with just those categories with the year as the index. I successfully created the plot, but the plot split the years into parts of the years, which was not what I wanted. I was unable to figure out how to change this at this time.

I then wanted to create a plot comparing the happiness in each region. First, I grouped the 2017 data by region and summed. I then realized this was not what I wanted. I wanted to find the average happiness score for each region and plot it.

During class, I created a horizontal bar graph by using the .mean instead of .sum. I then figured out how to get rid of the extra x
values on the area plot by using xticks. I spent a long time researching how to create a map of the world using the happiness score for
each country. After being unsuccessful, I moved on to creating a scatterplot with the points different sizes and colors. I attempted to
compate economy and health with size reflecting score or rank. I tried to use region to determine color but I was unsuccessful. I was
able to create plots with score as size and rank as size.

In the evening I was able to create a scatterplot with colors related to score and the size based on the rank. I did this for health vs
economy, and family vs freedom. I then created another area plot showing the category distribution for the top 50 happiest countries in
2017. 

#### November 19, 2018

I did more research on how to create a map using the happiness score for each country. I was able to create a clorepleth map using code
I found related to this dataset on kaggle. I had to use plotly in order to create this map. I then found information on the plotly 
website on how to change the formating of the map. I was able to change the color scale to something that is easier to see. I played around with different colors and how thick to make the borders.

I then created a heatmap for the 2017 data to find correlations between the categories, score, and rank. I then attempted to create a bar graph showing the average score of each category for each year. I was unable to successfully format this graph at this time.

#### November 20, 2018

We created a plan for what to do over break and what we need to do before we give our presentation on December 4th. We decided what we are going to include in our website. We still need to include more comments into our code describing our visualizations. I then worked on typing my written journals into GitHub.

#### November 21, 2018

Today I finished typing my journal into GitHub. I then made more comments into my python notebook describing the code and the visualizations I created.

#### November 27, 2018

Today during class, Sam and I planned out the order of our narrative and visualizations. We changed the theme and formating of our website to what we want. We created an image folder on github to put all of our visualizations so we can easily link to them for our website. We now have a plan to easily add our information to the website. 

#### November 28, 2018

I worked on organizing the website into the categories of our analysis. I then included the plots I had created in each category of our analysis. I also included descriptions and what we learned from each plot. The one plot I had an issue with importing is the world map displaying happiness score. I am unsure how to save the map in a way it can be interactive on the website.

#### November 29th, 2018

I added more information on what data we obtained and what information is contained in the datasets to the website. I also worked on adding more graphs and explinations of the graphs onto the website. We had some issues linking our Jupyter Notebooks to the website.
