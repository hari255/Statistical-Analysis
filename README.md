# 1. FoodHub - Exploratory Data Analysis**
## Context
The number of restaurants in New York is increasing day by day. Lots of students and busy professionals rely on those restaurants due to their hectic lifestyles. Online food delivery service is a great option for them. It provides them with good food from their favorite restaurants. A food aggregator company FoodHub offers access to multiple restaurants through a single smartphone app.

The app allows the restaurants to receive a direct online order from a customer. The app assigns a delivery person from the company to pick up the order after it is confirmed by the restaurant. The delivery person then uses the map to reach the restaurant and waits for the food package. Once the food package is handed over to the delivery person, he/she confirms the pick-up in the app and travels to the customer's location to deliver the food. The delivery person confirms the drop-off in the app after delivering the food package to the customer. The customer can rate the order in the app. The food aggregator earns money by collecting a fixed margin of the delivery order from the restaurants.

## Objective
The food aggregator company has stored the data of the different orders made by the registered customers in their online portal. They want to analyze the data to get a fair idea about the demand of different restaurants which will help them in enhancing their customer experience. Performed the data analysis to find answers to these questions that will help the company to improve the business.

### Exploratory Data Anlaytics

Exploratory Data Analysis (EDA) is a crucial step in the data science process. It involves analyzing data sets to summarize their main characteristics, often using visual methods. EDA helps in understanding the data and uncovering patterns. 

**Distinct Cuisines**

`
There are a total of 14 difffernet cuisines in the dataset.
`

<img width="468" alt="image" src="https://github.com/hari255/Statistical-Analytics/assets/59302293/8ea09fe5-c707-47cb-a746-473e498ce253">


---

**Week-day Vs Weekends**


`
To effectively understand the dynamics of online orders, quantifying the orders on weekdays versus weekends is crucial.
`
<img width="395" alt="image" src="https://github.com/hari255/Statistical-Analytics/assets/59302293/e7a3c8c7-96c3-4923-80df-0c5d691112ba">


---

**Ratings Distribution**


`
Below plot gives us an idea on the popular or busy restanurants, this is curcial interms of allocating more delivery drives in the area during peak hours*
`

<img width="289" alt="image" src="https://github.com/hari255/Statistical-Analytics/assets/59302293/264ee188-583e-4d99-b32a-d9f5873c0a9f">

---
**Deliery time**
`
This plot tells us that the avergae time taken to delivery an order, Most of the orders takes 45-60 mins to deliver.
`

<img width="382" alt="image" src="https://github.com/hari255/Statistical-Analytics/assets/59302293/46582a89-886f-4a45-ae51-0668b69b827a">

---

**In the conetxt of the problem, it's important to know the how much money people of spend on food**

<img width="385" alt="image" src="https://github.com/hari255/Statistical-Analytics/assets/59302293/3cbf5629-2b0b-4969-b762-774cc01da69b">

##### Let's see the number of orders that cost more than $20

``` py
percentage_of_every_order = (data['cost_of_the_order'] / data['cost_of_the_order'].sum()) * 100
greater_than_20 = data[data['cost_of_the_order']>20]
percentage =(greater_than_20.shape[0] / data.shape[0]) * 100

```

```
29.241 percent of the orders placed were more than $20.
```

### Performing Exploratory data analytics or visual representation of data could help us to identify the patterns and make informed decisions. It gives us a good starting point while building a predective model on the dataset. 

---
# 2. Dimensionality Reduction.


The MNIST dataset is an acronym that stands for the **Modified National Institute of Standards and Technology** dataset.

***Context and Objective*** 

This dataset consists of 60,000 grayscale images, which are small 28x28 pixel images.
These are images of handwritten digits from 0 to 9. We will work on this image data of handwritten digits and will visualize the images in two-dimensional space using the two dimensionality reduction techniques PCA and t-SNE.

Note: We will use the datasets module of the sklearn library to load the data and will only consider 6 classes, i.e., digits from 0 to 5.

---
# 3. Project: Mammography's Impact - Solved using Hypothesis Testing


**The Quest:**
We're investigating whether offering mammography is a game-changer in the fight against breast cancer. We use data to prove that mammography significantly reduces the risk of death.

**The Superpower:**
Hypothesis testing is like a magical magnifying glass helping us determine if the difference in death rates between those who got mammography and those who didn't is real or just a coincidence. We're not just hoping; we're scientifically proving that mammography is a hero in the battle against breast cancer.

**Our Mission:**
Our mission is to make the world healthier by figuring out if mammography is a true superhero in reducing the risk of death from breast cancer. We're not just crunching numbers; we're saving lives and making a real impact on healthcare!

***Understanding Hypothesis Testing***

Hypothesis testing is like being a detective for numbers! 🕵️‍♂️ It helps us figure out if something we believe is true is actually true or just a coincidence. Imagine you're investigating a crime (or in our case, a question). You have a suspect (null hypothesis - H0) and a claim you want to prove (alternative hypothesis - H1). Then, you gather evidence (data) and analyze it to see if there's enough proof to support your claim.

In our example, we're like a health detective! Investigating whether offering mammography (the suspect) significantly reduces the risk of death from breast cancer (the claim). Hypothesis testing helps you decide if the difference in death rates is real or just due to chance.

**Why it's Important:**
Hypothesis testing is crucial in science and research. It helps us make decisions based on evidence, ensuring we're not just guessing. In our case, it's about saving lives. If mammography significantly reduces the risk of death, it means a powerful tool in the fight against breast cancer!

# 4. Discriminant Analysis

Discriminant analysis is a statistical technique used in data analysis and machine learning to classify observations into different groups based on their characteristics or features.

Discriminant analysis is used when we have data with known categories (like types of fruits) and want to develop a method to classify new observations into these categories based on their features (like color, size, and shape). It helps us discover the important characteristics that differentiate between different groups, making it easier to classify new data.

You can think, that logistic regression can also capable of doing this, but the main difference lies in how they model the relationship between the features and the categories. Logistic regression estimates the probabilities of belonging to different categories directly, using a logistic function. On the other hand, discriminant analysis models the distribution of the features within each category and uses Bayes' theorem to calculate the probability of belonging to each category.  Logistic regression may be preferred when the relationship between the features and the categories is more linear, while discriminant analysis may be more suitable when the distribution of the features within each category is known or assumed to be normal.


