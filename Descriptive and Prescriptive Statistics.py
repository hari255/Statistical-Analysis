#!/usr/bin/env python
# coding: utf-8

# # Project Foundations for Data Science: FoodHub Data Analysis
# 
# 

# ### Context
# 
# The number of restaurants in New York is increasing day by day. Lots of students and busy professionals rely on those restaurants due to their hectic lifestyles. Online food delivery service is a great option for them. It provides them with good food from their favorite restaurants. A food aggregator company FoodHub offers access to multiple restaurants through a single smartphone app.
# 
# The app allows the restaurants to receive a direct online order from a customer. The app assigns a delivery person from the company to pick up the order after it is confirmed by the restaurant. The delivery person then uses the map to reach the restaurant and waits for the food package. Once the food package is handed over to the delivery person, he/she confirms the pick-up in the app and travels to the customer's location to deliver the food. The delivery person confirms the drop-off in the app after delivering the food package to the customer. The customer can rate the order in the app. The food aggregator earns money by collecting a fixed margin of the delivery order from the restaurants.
# 
# ### Objective
# 
# ****The food aggregator company has stored the data of the different orders made by the registered customers in their online portal. They want to analyze the data to get a fair idea about the demand of different restaurants which will help them in enhancing their customer experience. 
# 
# ### Data Description
# 
# The data contains the different data related to a food order. The detailed data dictionary is given below.
# 
# ### Data Dictionary
# 
#  * order_id Unique ID of the order
#  * customer_id ID of the customer who ordered the food
#  * restaurant_name Name of the restaurant
# * cuisine_type: Cuisine ordered by the customer
# * cost: Cost of the order
# * day_of_the_week: Indicates whether the order is placed on a weekday or weekend (The weekday is from Monday to Friday and the weekend is Saturday and Sunday)
# * rating: Rating given by the customer out of 5
# * food_preparation_time: Time (in minutes) taken by the restaurant to prepare the food. This is calculated by taking the difference between the timestamps of the restaurant's order confirmation and the delivery person's pick-up confirmation.
# * delivery_time: Time (in minutes) taken by the delivery person to deliver the food package. This is calculated by taking the difference between the timestamps of the delivery person's pick-up confirmation and drop-off information

# ### Let us start by importing the required libraries

# In[1]:


# import libraries for data manipulation
import numpy as np
import pandas as pd

# import libraries for data visualization
import matplotlib.pyplot as plt
import seaborn as sns


# ### Understanding the structure of the data

# In[2]:


# read the data
data = pd.read_csv('foodhub_order.csv')
# returns the first 5 rows
data.head()


# #### Observations:
# 
# The DataFrame has 9 columns as mentioned in the Data Dictionary. Data in each row corresponds to the order placed by a customer.

# ### **Question 1:** How many rows and columns are present in the data? 

# In[3]:


# Write your code here
data.shape


# #### Observations: Our data has 1898 rows and 9 columns
#  

# ### **Question 2:** What are the datatypes of the different columns in the dataset? (The info() function can be used)

# In[4]:


# Use info() to print a concise summary of the DataFrame
data.info()


# #### Observations: In our data, features ordere_id, customer_id, food_preparation_time, delivery_time are intizers, cost of th eorder being float and rest of them are characters(object)
# 

# ### **Question 3:** Are there any missing values in the data? If yes, treat them using an appropriate method.
# 

# In[5]:


# Write your code here1`
data.isna()


# In[6]:


data.isna().sum()


# #### Observations: There are no missing values in our data
# 

# ### **Question 4:** Check the statistical summary of the data. What is the minimum, average, and maximum time it takes for food to be prepared once an order is placed?

# In[7]:


# Write your code here

data.corr()


# In[8]:


data.describe()


# In[9]:


#### from the above table we can see the munimum, avg and maximmum time taken to prepare the food can be found. They are 
#### avg food_preparation_time = 27 mins, minimum food_preparation_time = 20 mins, max food_preaparation_time = 35 mins


# #### Observations: order_id and customer_id being nominal data, Average cost_of_the_order  is about 16.5 and food_preparation and delivery_time average being roughly around 25 minutes
# 

# ### **Question 5:** How many orders are not rated?

# In[10]:


data.columns
data = pd.DataFrame(data)


# In[11]:


no_rating_count = 0
for each_rating in data['rating']:
    if each_rating == 'Not given':
        no_rating_count = no_rating_count + 1
      


# #### Running below line will print all the 736 records, for the enhancement and readibility, I've put itlike below. you may try running it 

# In[12]:


# print(no_rating_count)   


# #### Observations: There are 736 records that are not rated in the given dataset.
# 
# 

# ### Exploratory Data Analysis (EDA)

# ### Univariate Analysis

# ### **Question 6:** Explore all the variables and provide observations on their distributions. (Generally, histograms, boxplots, countplots, etc. are used for univariate exploration.)

# In[13]:


# since order_id and customer_id are nominal and doesn't hold any value other than distinction,
# we will be focusing majorlly on the other fetaues in the dataset
# variables that will we are going to explore and bring insights are 
# restaurant_name, cusine_type, cost_of_the_order, day_of_the_week, rating, food_preparation_time, delivery_time


# In[14]:


plt.hist(data['day_of_the_week'])
plt.xlabel("Day of the week")
plt.ylabel("Number of orders placed")


# ### From the above bar-chart we can see that number of orders on weekends are high compared to the weekdays.
# 

# In[15]:



plt.xlabel("Cost of the order")
plt.ylabel("number of orders")


# ### From the above histogram we can say that majority of the orders are inbetween the price of range 10 dollars to 16 dollars.

# In[16]:


print(data['cuisine_type'].unique())


# ### There are a total of 14 cuisines in the foodhub dataset

# In[17]:


sns.countplot(y=data['cuisine_type'], orient = 'v')


# ### From the above count plot, it's obvious that most of the orders were from American, Japanese, Italian and Chinese.

# In[18]:


plt.hist(data['rating'], color = ['green'])
plt.xlabel('Rating')
plt.ylabel('Number of orders')


# ### Above graph shows ratings given by customers on x-axis with number of orders on y-axis

# In[19]:


plt.hist(data['delivery_time'], color = ['green'])
plt.xlabel('delivery_time in Minutes')
plt.ylabel('Number of orders')


# ### Above graph shows the delivery time on x-axis with number of orders on y-axis

# In[20]:


plt.hist(data['food_preparation_time'], color = ['green'])
plt.xlabel('food_preparation_time')
plt.ylabel('Number of orders')


# ### Above graph shows the food preparation time in x-axis with number of orders on y-axis

# ####   ==================================================================================================== ####

# ### **Question 7**: Which are the top 5 restaurants in terms of the number of orders received? 

# In[21]:


# first let's find out the distinct restaurants in the dataset
restaurants_list = data['restaurant_name'].unique()
len(restaurants_list)


# In[22]:


# Below is the list of restaruants according to orders placed
#for each_restaurant in data['restaurant_name']:
#   print(each_restaurant)


# In[24]:


### Below is the list of distinct restaurants.
count_each_restaurant = data['restaurant_name'].value_counts()


# ### Observations: The top 5 restaurants are Shake Shack, The Meatball Shop, Blue Ribbon Sushi, Blue Ribbon Fried Chicken, Parm.

# ### **Question 8**: Which is the most popular cuisine on weekends?

# In[25]:


# Filtering data based on the day of the week.

weekend_data = data.query("day_of_the_week == 'Weekend'")
weekend_data.head(10)


# In[26]:


count_each_cuisinetype = weekend_data['cuisine_type'].value_counts()
count_each_cuisinetype


# #### Observations: American, Japanese, Chinese, Mixican and Indian are the top five restanurants on weekends in terms of number of orders placed
# 

# ### **Question 9**: What percentage of the orders cost more than 20 dollars? 

# In[27]:


# Write the code here
#Visual insepection of the cost_of_orders using an histogram

plt.hist(data['cost_of_the_order'])
plt.xlabel("Cost of the order")
plt.ylabel("number of orders")


# In[28]:


# Calculating the percentage

percentage_of_every_order = (data['cost_of_the_order'] / data['cost_of_the_order'].sum()) * 100
percentage_of_every_order


# In[29]:


greater_than_20 = data[data['cost_of_the_order']>20]
greater_than_20


# In[30]:


plt.hist(greater_than_20['cost_of_the_order'])
plt.xlabel("Cost of the order")
plt.ylabel("number of orders")


# In[31]:


percentage =(greater_than_20.shape[0] / data.shape[0]) * 100
percentage


# #### Observations: Roughly 30% of the orders placed are above 20 USD.
# 

# ### **Question 10**: What is the mean order delivery time?

# In[32]:


# Write the code here
plt.hist(data['delivery_time'])
plt.xlabel("delivery_time")
plt.ylabel("number of orders")


Avg_order_delivery_time = data['delivery_time'].mean()
Avg_order_delivery_time


# #### Observations: Average delivery time of the orders is 24 minutes, but most of the orders are delivered between 25 to 30 minutes.
# 

# ### **Question 11:** The company has decided to give 20% discount vouchers to the top 3 most frequent customers. Find the IDs of these customers and the number of orders they placed.

# In[33]:


# Write the code here

frequent_customer = data['customer_id'].value_counts()
frequent_customer[0:3]


# #### Observations: customer 52832  placed 13 orders, which is most by any customer, followed by 47440 and 83287 with 10 and 9 orders respectively.
# 
#  

# ### Multivariate Analysis

# ### **Question 12**: Perform a multivariate analysis to explore relationships between the important variables in the dataset. (It is a good idea to explore relations between numerical variables as well as relations between numerical and categorical variables) 
# 

# In[34]:


# Write the code here


sns.pairplot(data)


###The below correlation plot shows the relation btw all the numerical variables, here from the below plot order_id can be 
### though of as like a categorical, since it doesn't possess any transformations. Other vaiables seems like they are not poseesimng any correlatoin.
### As the each individual pair plot seems like uniformly distributed.


# In[35]:


data.corr()


# #### If the coorelation between the variables is closer to zero, They are not showing any significant relationship.
# #### From the below table, correlation coefficient values between the variables are pretty close to zero, proving there isn't any relationship or lineratiy between the vaiables

# In[36]:


### Let's find the correlation between cost_of_the_order and delivery_time.

plt.scatter(data['cost_of_the_order'], data['delivery_time'])


# In[37]:


plt.scatter(data['cost_of_the_order'], data['food_preparation_time'])


# ### **Question 13:** The company wants to provide a promotional offer in the advertisement of the restaurants. The condition to get the offer is that the restaurants must have a rating count of more than 50 and the average rating should be greater than 4. Find the restaurants fulfilling the criteria to get the promotional offer. 

# In[38]:


data_rated = data[data['rating'] != 'Not given'].copy()

# Convert rating column from object to integer
data_rated['rating'] = data_rated['rating'].astype('int')  

# Create a dataframe that contains the restaurant names with their rating counts
data_rating_count = data_rated.groupby(['restaurant_name'])['rating'].count().sort_values(ascending = False).reset_index()
data_rating_count.head() 


# In[39]:


rest_names = data_rating_count['restaurant_name'] # Complete the code to get the restaurant names having rating count more than 50
rest_names


# In[40]:



# Filter to get the data of restaurants that have rating count more than 50
df_mean_4 = data_rated[data_rated['restaurant_name'].isin(rest_names)].copy()
df_mean_4


# In[41]:



# Group the restaurant names with their ratings and find the mean rating of each restaurant
df_mean_4.groupby(['restaurant_name'])['rating'].mean().sort_values(ascending = False).reset_index().dropna() # Complete the code to find the mean rating


# #### Observations: No restauranat qualifies for the promotion, since no restaurant meets the given condition.
# 

# ### **Question 14:** The company charges the restaurant 25% on the orders having cost greater than 20 dollars and 15% on the orders having cost greater than 5 dollars. Find the net revenue generated by the company across all orders. 

# In[52]:


# Write the code here

for cost in data['cost_of_the_order']:
   # if cost > 5 and cost < 20 :
       # print("15% Charge: " ,cost)
   # if cost > 20 :
       # print("25% Charge: ", cost)
  


# In[43]:


def compute_rev(x):
    if x > 20:
        return x*0.25
    elif x > 5:
        return x*0.15
    else:
        return x*0

data['Revenue'] = data['cost_of_the_order'].apply(compute_rev) # Write the apprpriate column name to compute the revenue
data.head()

sum(data['Revenue'])


# #### Observations: The total revenue generated by the company across all orders is 6166 Dollars.
# 

# ### **Question 15:** The company wants to analyze the total time required to deliver the food. What percentage of orders take more than 60 minutes to get delivered from the time the order is placed? (The food has to be prepared and then delivered.) 

# In[44]:


## let's find out the total delivery time for each order 
data['Total_time'] = data['food_preparation_time'] + data['delivery_time']
data['Total_time']


# In[45]:


# Let's do visual inspection on the total_time variable. 

plt.hist(data['Total_time'])
plt.xlabel("time in minutes")
plt.ylabel("number of orders")


# ##### We can see there were some orderes from the right tail that represents orders that took more than 60 minutes to get delivered since the time order placed
# 

# In[46]:


time_greater_than_60 = data[data['Total_time']>60]
time_greater_than_60


# In[47]:


Greater_than_60_min_delivery_time_percentage = time_greater_than_60.shape[0]/data.shape[0]
Greater_than_60_min_delivery_time_percentage


# #### Observations: 10% of the orders were delivered after 60 mins.
# 

# ### **Question 16:** The company wants to analyze the delivery time of the orders on weekdays and weekends. How does the mean delivery time vary during weekdays and weekends? 

# In[48]:


# Write the code here
weekend_data = data.query("day_of_the_week == 'Weekend'")
weekend_data.head(10)


# In[49]:


weekday_data = data.query("day_of_the_week == 'Weekday'")
weekday_data


# In[50]:


mean_delivery_time_weekdays = weekday_data['delivery_time'].mean()
mean_delivery_time_weekdays


# In[51]:


mean_delivery_time_weekend = weekend_data['delivery_time'].mean()
mean_delivery_time_weekend


# #### Observations: The average deilvery time on weekends is low compared to the average delivery time on weekdays
# 

# ### Conclusion and Recommendations

# ### **Question 17:** What are your conclusions from the analysis? What recommendations would you like to share to help improve the business? (You can use cuisine type and feedback ratings to drive your business recommendations.) 

# ### Conclusions:
# #### There is no coorelation between the variables, having more data with some other features might be helpful.
# #### Top 5 restaurants and cuisines are found from the analysis. 
# #### Avg delivery time on weekends is low.
# #### Cost of the orders total time taken to deliver the food from the time order placed follows roughly a normal distribution.

# ### Recommendations:
# 
# #### Company should hire more delivery drivers during the weekdays, since the average delivery time is high during weekdays.
# #### Foodhub should promote or give discounts on 1. Shake Shack	2. The Meatball Shop 3. Blue Ribbon Sushi	4. Blue Ribbon Fried Chicken	5. RedFarm Broadway	
# #### Also consider promoting offers on AMERICAN, JAPANESE, ITALIAN, CHINESE cuisines.
# #### Food hub should hire more delivery drivers, so that It can deliver more fastly.
# #### To boost it's business, it should also promote restaurants with less food_preparation_time.
# 

# ---

# In[ ]:





# In[ ]:





# In[ ]:




