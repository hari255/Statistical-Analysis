

# 1. Dimensionality Reduction.

**Dimensionality reduction is a process used in machine learning and statistics to reduce the number of input variables in a dataset while retaining as much information as possible. This technique is crucial for handling high-dimensional data, improving model performance, and making data visualization easier. There are several methods for dimensionality reduction, including Principal Component Analysis (PCA), t-Distributed Stochastic Neighbor Embedding (t-SNE), Linear Discriminant Analysis (LDA), and Autoencoders.

Principal Component Analysis (PCA) and t-Distributed Stochastic Neighbor Embedding (t-SNE) are two popular dimensionality reduction techniques used in data science. They help simplify complex datasets, making it easier to visualize and analyze data. Here’s a detailed guide to both methods**

| Option | Description |
| ------ | ----------- |
| **PCA**  | PCA is a method that reduces the number of dimensions (features) in your data while keeping as much information as possible. It creates new features that are combinations of the original ones. The first new feature captures the most variation in the data, the second new feature captures the second most variation, and so on. This helps in simplifying and visualizing the data. |
| **T-SNE**|t-SNE is a technique that reduces the number of dimensions in your data to make it easier to visualize. It focuses on keeping similar points close together in a new, lower-dimensional space, like 2D or 3D, so you can see clusters and patterns that might be hidden in the original high-dimensional data.|

***Context and Objective*** 
The MNIST dataset is an acronym that stands for the **Modified National Institute of Standards and Technology** dataset.
This dataset consists of 60,000 grayscale images, which are of 28x28 pixel images.
These are images of handwritten digits from 0 to 9. We will work on this data of handwritten digits images and visualize the images in two-dimensional space using the above discussed dimensionality reduction techniques PCA and t-SNE.


Note: We will use the datasets module of the sklearn library to load the data and will only consider 6 classes, i.e., digits from 0 to 5.


### t-SNE embedding of the digits dataset
```py



print("Computing t-SNE embedding")

t0 = time()

tsne = manifold.TSNE(n_components = 2, init = 'pca', random_state = 0) 

X_tsne = tsne.fit_transform(X)

t1 = time()

tsne_time = t1-t0

print("t-SNE-Embeddings in time {}".format(tsne_time),"\n", X_tsne)

```

<img width="432" alt="image" src="https://github.com/hari255/Statistical-Analytics/assets/59302293/19f276b2-d51f-43d4-ab6b-dcc6e37ec2e4">

---

### Projection on the first 2 principal components using PCA

``` py
print("Computing PCA projection")

t0 = time()

X_pca = decomposition.PCA(n_components = 2).fit_transform(X)

t1 = time()

pca_time = t1 - t0

print("PCA projections in time {}".format(pca_time), "\n", X_pca)

print("***************************************************")

```


<img width="432" alt="image" src="https://github.com/hari255/Statistical-Analytics/assets/59302293/ccbfc3aa-05a4-4bf5-9958-1a5959efa4ca">


## Results and Conclusion

+ We have effectively reduced the dimensionality of the images, from 64 to 2, using t-SNE and PCA, and plotted the 2D embeddings and projections.

+ Out of the two methods used above, t-SNE takes a longer time to generate embeddings but gives better visualizations with well-separated clusters for each handwritten digit.

+ The annotations show that while PCA gives the same clusters, the overall plot represents more of a blob and is not as well-separated as t-SNE.

+ t-SNE is good for visualizing the data in lower dimensions but is very slow and should only be used on small datasets, whereas PCA is more computationally efficient     and can be used on large datasets as well.

-----
-----




# 2. FoodHub - Exploratory Data Analysis
```I believe before making any assumnptions on the data and builidng models, It is important to ask ourselves questions like;  (whether this data is correct or enough? To what extreeme/level I can relly on this data?). ``` 

EDA is a technique to understand data and make informed decisions.


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
Below plot gives us an idea on the popular/busy restanurants, this information is curcial interms of allocating more delivery drives in the area during peak hours*
`

<img width="289" alt="image" src="https://github.com/hari255/Statistical-Analytics/assets/59302293/264ee188-583e-4d99-b32a-d9f5873c0a9f">


### Performing Exploratory data analytics on data helps us to identify the patterns and make informed decisions. It gives us a good starting point while building a predective model.



---

---

# 3. Hypothesis Testing
Hypothesis testing is a statistical method used to determine if there is enough evidence in a sample of data to infer that a certain condition is true for the entire population. In the context of this project, hypothesis testing can be used to assess whether the marketing campaign had a significant effect on conversions.


**The Quest:**
We're investigating whether offering mammography is a game-changer in the fight against breast cancer. We use data to prove that mammography significantly reduces the risk of death leveraging a technique from statistics called **Hypothesis testing**.

We

 <img width="403" alt="Screenshot 2024-07-20 at 1 03 45 PM" src="https://github.com/user-attachments/assets/7e747351-dcaa-4b46-8e38-8372f0a8baac">


**Tool**
Hypothesis testing is like a magnifying glass helping us determine if the difference in death rates between those who got mammography and those who didn't, Is real or just a coincidence?. We're not just hoping; we're scientifically proving that mammography is a hero in the battle against breast cancer.


**Understanding Hypothesis Testing**
Hypothesis testing helps us figure out if something we believe is true, Is actually true or just a coincidence? Imagine you're investigating a crime (or in our case, a question), you have a suspect (null hypothesis - H0) and a claim you want to prove (alternative hypothesis - H1). Then, you gather evidence (data) and analyze it to see if there's enough proof to support your claim.

**Hypothesis Notation- It is a standard notation used in most of the Statistics Texbooks**


+ H0 - Null Hypothesis - Null hypothesis states that taking mammography doesn't decrease the risk of Heart disease.
 
+ H1 - Alternative Hypothesis - Alternative hypothesis(opposite of Null) states there is an effect(big/small) taking mammography.



A#alternative will be against null, saying that the control group will have less death rate

The total number of trials / observations = 31,000
The hypothesized probability = 0.002
The number of deaths due to breast cancer in the treatment group = 39

**Why it's Important:**
Hypothesis testing is crucial in science and research. It helps us make decisions based on evidence, ensuring we're not just guessing. In our case, it's about saving lives. If mammography significantly reduces the risk of death, it means a powerful tool in the fight against breast cancer!

<img width="881" alt="Screenshot 2024-07-20 at 1 02 50 PM" src="https://github.com/user-attachments/assets/6f51612b-c20f-4d4a-a70c-8310c9d6ca44">





# 4. Discriminant Analysis

Discriminant analysis is a statistical technique used in `Data analysis` and `Machine learning` to classify observations into different groups based on their characteristics or features.

Discriminant analysis is used when we have data with known categories (like types of fruits) and want to develop a method to classify new observations into these categories based on their features (like color, size, and shape). It helps us discover the important characteristics that differentiate between different groups, making it easier to classify new data.

You can think, that logistic regression can also capable of doing this, but the main difference lies in how they model the relationship between the features and the categories. Logistic regression estimates the probabilities of belonging to different categories directly, using a logistic function. On the other hand, discriminant analysis models the distribution of the features within each category and uses Bayes' theorem to calculate the probability of belonging to each category.  Logistic regression may be preferred when the relationship between the features and the categories is more linear, while discriminant analysis may be more suitable when the distribution of the features within each category is known or assumed to be normal.


