"""
Movie recommendation system based on genres.
"""

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load movie dataset
movies = pd.read_csv("dataset/ml-latest-small/movies.csv")

# Data preprocessing
movies['genres'] = movies['genres'].apply(lambda x: x.lower().replace('|', ' '))

# Create TF-IDF vectorizer and fit the movie dataset
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(movies['genres'])

#Calculate similarity matrix
cosine_sim_matrix = cosine_similarity(tfidf_matrix, tfidf_matrix)

def find_movie_index(movie_title, year):
    if year != None:
        movie_title = f"{movie_title} ({year})"
        if movie_title not in movies['title'].values:
            return None
        return movies[movies['title'] == movie_title].index[0]
    else:
        if not any(movies['title'].str.contains(movie_title)):
            return None
        return movies[movies['title'].str.contains(movie_title)].index[0]

def recommend_movies(movie_title, year=None, n_recommendations=5):
    movie_index = find_movie_index(movie_title, year)
    if movie_index is None:
        movie_not_found_message = f"Movie  '{movie_title}' not found in dataset."
        print(movie_not_found_message)
        return None

    sim_scores = list(enumerate(cosine_sim_matrix[movie_index]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:n_recommendations + 1]

    recommended_movie_indices = [i[0] for i in sim_scores]
    return movies.iloc[recommended_movie_indices]

if __name__ == "__main__":
    year = 1995
    movie_title = "Toy Story"
    n_recommendations = 10
    print(f"Similar recommendations for movie '{movie_title}':")

    recommendations = recommend_movies(movie_title, year, n_recommendations)
    if recommendations is not None:
        print(recommendations)
