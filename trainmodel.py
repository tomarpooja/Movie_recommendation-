import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load datasets
movies = pd.read_csv("tmdb_5000_movies.csv")
credits = pd.read_csv("tmdb_5000_credits.csv")

# Merge
movies = movies.merge(credits, on='title')

# Create tags safely
movies['tags'] = (
    movies['overview'].fillna('') + " " +
    movies['genres'].fillna('') + " " +
    movies['keywords'].fillna('') + " " +
    movies['cast'].fillna('')
)

# Vectorize
cv = CountVectorizer(max_features=5000, stop_words='english')
vectors = cv.fit_transform(movies['tags']).toarray()

# Similarity matrix
similarity = cosine_similarity(vectors)

# Save model + data
pickle.dump(movies, open("models/movies.pkl", "wb"))
pickle.dump(similarity, open("models/similarity.pkl", "wb"))
print("✅ Model trained and saved in models/ folder")
