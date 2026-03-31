# csa2026
# Movie Recommendation System

## Overview
This project is a basic movie recommendation system created using Python. The main goal of this project is to suggest movies to users based on the similarity of genres. It uses simple Natural Language Processing (NLP) techniques and similarity measurement.

## Objective
The objective of this project is to understand how recommendation systems work using machine learning concepts like TF-IDF and cosine similarity.

## Tools and Technologies
Python programming language is used to develop this project. The following libraries are used:

- Pandas (for data handling)
- Scikit-learn (for vectorization and similarity calculation)

## Working Principle
First, a small dataset of movies and their genres is created. After that, TF-IDF Vectorizer converts text data into numerical form. Then cosine similarity is used to find how closely movies are related. When the user enters a movie name, the system finds similar movies and displays the top 3 recommendations.

## Features
- Simple and easy to understand logic
- Command line based interaction
- Fast recommendation process
- Beginner level machine learning implementation

## How to Run the Project

Step 1: Install required libraries

pip install pandas  
pip install scikit-learn  

Step 2: Run the python file

python movie_recommender.py

## Sample Result

If user enters:

avengers

System suggests similar movies like Iron Man, Thor and Captain America.

## screenshot (code)

![movie_Recommendation_system code 1](https://github.com/user-attachments/assets/4525debd-abdc-4348-8c50-f2d1bf57dd25)
![movie_Recommendation_system code 2](https://github.com/user-attachments/assets/c4d45a30-48ca-459d-beef-3cbdd699ac29)

## Result
![movie_Recommendation_system result](https://github.com/user-attachments/assets/512020cd-f9d9-4e3d-8246-433d37a04f87)


## Limitations
Currently the dataset is very small. Recommendations may improve if more movies and more features like ratings and reviews are added.

## Future Scope
This project can be improved by:
- Adding large datasets
- Creating a graphical interface
- Adding user ratings
- Using advanced recommendation algorithms

## Usage Instructions
Clone this repository or download the python movie_recommender.py file.

Run the script in your terminal: python movie_recommender.py

When prompted, enter a movie name (e.g., inception or avengers).

The system will output the top 3 movies you might like based on the database.



## Academic Use
This project is developed for learning purpose as part of AI/ML study.

