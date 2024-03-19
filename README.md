# Genre-Based Movie Recommender

An intuitive movie recommendation system leveraging genre similarity with TF-IDF and cosine similarity for a personalized film discovery experience.

## Getting Started

These instructions will help you set up the movie recommendation system on your local machine.

### Prerequisites

Ensure that you have the following installed on your machine:

- Python 3.6 or later
- pandas
- scikit-learn
- numpy

You can install the required packages using pip:

```sh
pip install -r requirements.txt
```

### Installing

1. Clone this repository to your local machine:

```sh
git clone https://github.com/Shanmuk12/Movie-Recomandation-based-on-users-Genre
.git
```

2. Change to the repository directory:

```sh
cd Movie-Recomandation-based-on-users-Genre

```

3. Download the movie dataset from [MovieLens](https://grouplens.org/datasets/movielens/) and save it in the **'dataset/ml-latest-small/'** directory.

4. Make sure the dataset file is named **'movies.csv'**.

## Usage

1. Open the **'movie_recommender.py'** file and modify the following lines with the appropriate movie title and year:

```python
year = 1995
movie_title = "Toy Story"
```

2. Save the changes and run the script:

```sh
python movie_recommender.py
```

3. The script will print the top 10 recommended movies similar to the specified movie.

```
Similar recommendations for movie  'Toy Story' ：
      movieId                                              title  \
1706     2294                                        Antz (1998)   
2355     3114                                 Toy Story 2 (1999)   
2809     3754     Adventures of Rocky and Bullwinkle, The (2000)   
3000     4016                   Emperor's New Groove, The (2000)   
3568     4886                              Monsters, Inc. (2001)   
6194    45074                                   Wild, The (2006)   
6486    53121                             Shrek the Third (2007)   
6948    65577                     Tale of Despereaux, The (2008)   
7760    91355  Asterix and the Vikings (Astérix et les Viking...   
8219   103755                                       Turbo (2013)   

                                           genres  
1706  adventure animation children comedy fantasy  
2355  adventure animation children comedy fantasy  
2809  adventure animation children comedy fantasy  
3000  adventure animation children comedy fantasy  
3568  adventure animation children comedy fantasy  
6194  adventure animation children comedy fantasy  
6486  adventure animation children comedy fantasy  
6948  adventure animation children comedy fantasy  
7760  adventure animation children comedy fantasy  
8219  adventure animation children comedy fantasy  
```

## Contributing

If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes and push them to your fork.
4. Create a pull request to merge your changes into the main repository.


## Acknowledgments

* [MovieLens](https://grouplens.org/datasets/movielens/) for providing the movie dataset.
