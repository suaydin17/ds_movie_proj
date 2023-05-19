# Top 1000 Highest Grossing Movies Data Analysis Project

## In this project, movie dataset analyzed with the goal of performing data cleaning and  exploratory data analysis (EDA). 

* Top 1000 Highest Grossing Movies dataset in Kaggle is used for this project.

## Code and Resources Used
**Python Version:** 3.9

**Packages:** pandas, numpy, matplotlib, seaborn.

## Data Insight
The dataset contains information about top 1000 highest grossing movies. It initially had 918 rows and 14 columns. Some of the important variables are:

* Titles 
* Genres
* Release dates
* Production companies
* Box office sales
* Movie runtime
* License

## Data Cleaning
* Unnamed column is dropped.
* Year information from movie title is omitted.
* Release date column is divided as year and month.
* A new column for the age of movie is created.
* Runtime is converted into minutes. 
* New columns called info_len and genre_num are created. 

These tasks ensure that the data is clean and ready for analysis.

## Exploratory Data Analysis
Once the data is cleaned, exploratory data analysis is performed to gain insights into the dataset. This involves visualizing the data using various plots and charts to understand the relationships between variables, identify trends, and patterns.

* The initial data is inspected. Shape of the data, dtypes, null values and information about numerical variables are inspected.
* **Distributiıns of Numerical Variables.** Age, runtime and number of genres show a distribution close to normal distribution, but Distribution of World Sales is right-skewed.

<div>
  <img src="https://user-images.githubusercontent.com/132287565/236802011-b4e1133c-1e06-434a-9e3c-18f92aa30e80.png" width="400" height="300" style="margin-right: 10px;">
  <img src="https://user-images.githubusercontent.com/132287565/236802046-ac1656d6-62c4-4db9-bd78-009e647437d5.png" width="400" height="300">
</div>
<div>
  <img src="https://user-images.githubusercontent.com/132287565/236802060-89732aaf-1937-463d-9e8d-84c95e033fca.png" width="400" height="300" style="margin-right: 10px;">
  <img src="https://user-images.githubusercontent.com/132287565/236801950-f12a6632-174d-452a-8f14-40f2a4dcd48e.png" width="400" height="300">
</div>

* **Boxplot of Sales Data.** There are some outliers for three of the sales data.

<img src="https://user-images.githubusercontent.com/132287565/236803983-d3dd7961-4a25-42ad-b35a-40b7d04cd3a8.png" width="50%">

* **Correlation Between Numerical Variables.** Domestic, international and world sales are highly correlated with eachother. This is why World Sales column is used to evaluate the sales success of a movie.

<img src="https://user-images.githubusercontent.com/132287565/236804717-abdf85ab-1e06-461a-8be0-656179e2e39c.png" width="50%">

* **Graphs for Categorical Variables.** Number of movies for each category in the dataset.

<div style="display:flex;">
  <img src="https://user-images.githubusercontent.com/132287565/236804922-1d5189ae-f3e9-4f56-ba52-a8e89a942a25.png" style="width:30%;">
  <img src="https://user-images.githubusercontent.com/132287565/236804956-8e727209-04e3-4987-b202-4a6eb78a70d4.png" style="width:30%;">
  <img src="https://user-images.githubusercontent.com/132287565/236804998-205e22d1-66e8-4562-abbf-20a67b543b36.png" style="width:30%;">
</div>

* **Movie Success and Seasons.** It is seen that highest saled movies are usually released in summer and spring.

<p float="left">
  <img src="https://user-images.githubusercontent.com/132287565/236805498-d0ea1b63-a243-4c6e-8311-7114ecacc713.png" width="400" />
  <img src="https://user-images.githubusercontent.com/132287565/236805521-3e77ec97-eb4b-4cb2-9423-908c447c66c5.png" width="400" />
</p>

* **Movie Sales for Each Genre.** Sci-fi, adventure and fantasy are the top three most popular genres regarding world sales.

<img src="https://user-images.githubusercontent.com/132287565/236805816-e55e5784-7ce5-4260-b3ec-e94034291f85.png" width="70%">

<img src="https://user-images.githubusercontent.com/132287565/236805853-beb082eb-4434-4cca-8aae-ffbf2cc05d60.png" width="70%">

* **Wordcloud for the Movie Information Texts.**

<img src="https://user-images.githubusercontent.com/132287565/236806262-43cb5418-3349-4b0b-a8f4-07b62b57b506.png" width="70%">

* **Distributor Informations.** Top 6 distributors make most of the sales.

<img src="https://user-images.githubusercontent.com/132287565/236806388-ad8d26c9-38e5-4376-842b-92055107ce64.png" width="70%">

<img src="https://user-images.githubusercontent.com/132287565/236806406-9367ef47-aac9-4b1e-8191-d714c390d2ef.png" width="70%">

* **Licence Informations.** PG-13 movies are sold the most.

G – General Audiences

PG – Parental Guidance Suggested

PG-13 – Parents Strongly Cautioned

R – Restricted

<img src="https://user-images.githubusercontent.com/132287565/236806719-f84dcaed-90b1-476b-9fab-bd0269a02ac4.png" width="60%">

* **World Sales by Total Runtime.** Movies between 2 hours and 2.5 hours long are the most popular.

<img src="https://user-images.githubusercontent.com/132287565/236807615-0b73eb7b-1117-400e-8248-eba088002c6e.png" width="60%">

* **Inspecting the Popularity of Movie Series Through Years.**

Avengers series don't lose their fame as the years pass.

<img src="https://user-images.githubusercontent.com/132287565/236808405-166cda92-2065-40b6-b5f4-14736ddb0c2c.png" style="width: 60%;" alt="image">

Star Wars movies are not able to continue their success in theaters.

<img src="https://user-images.githubusercontent.com/132287565/236808494-2b8c2f64-186a-4af5-8088-f2ba08308bb7.png" style="width: 50%;" alt="image">

