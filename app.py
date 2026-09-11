from flask import Flask, render_template, request
import pickle
import requests
import subprocess

app = Flask(__name__)

# Load trained data
movies = pickle.load(open("models/movies.pkl", "rb"))
similarity = pickle.load(open("models/similarity.pkl", "rb"))

# Put your NEW TMDB API key here
API_KEY = "YOUR_NEW_TMDB_API_KEY"

BASE_URL = "https://api.themoviedb.org/3"
IMAGE_URL = "https://image.tmdb.org/t/p/w500"


def fetch_poster(movie_id):
    try:
        url = f"{BASE_URL}/movie/{int(movie_id)}"

        params = {
            "api_key": API_KEY,
            "language": "en-US"
        }

        response = requests.get(
            url,
            params=params,
            timeout=10,
            headers={"User-Agent": "MovieRecommendationApp/1.0"}
        )

        response.raise_for_status()

        data = response.json()

        poster_path = data.get("poster_path")

        if poster_path:
            return IMAGE_URL + poster_path

    except requests.exceptions.RequestException as e:
        print("TMDB poster error:", e)

    except Exception as e:
        print("Poster error:", e)

    return None


def fetch_trailer(movie_id):
    try:
        url = f"{BASE_URL}/movie/{int(movie_id)}/videos"

        params = {
            "api_key": API_KEY,
            "language": "en-US"
        }

        response = requests.get(
            url,
            params=params,
            timeout=10,
            headers={"User-Agent": "MovieRecommendationApp/1.0"}
        )

        response.raise_for_status()

        data = response.json()

        for video in data.get("results", []):
            if (
                video.get("type") == "Trailer"
                and video.get("site") == "YouTube"
            ):
                return f"https://www.youtube.com/watch?v={video['key']}"

    except requests.exceptions.RequestException as e:
        print("TMDB trailer error:", e)

    except Exception as e:
        print("Trailer error:", e)

    return None


def recommend(movie):

    if not movie:
        return [{
            "title": "❌ Please enter a movie name",
            "poster": None,
            "trailer": None
        }]

    # Remove extra spaces
    movie = movie.strip()

    # Check movie exists
    if movie not in movies["title"].values:

        # Try case-insensitive search
        matching_movies = movies[
            movies["title"].str.lower() == movie.lower()
        ]

        if matching_movies.empty:
            return [{
                "title": "❌ Movie not found in dataset",
                "poster": None,
                "trailer": None
            }]

        movie = matching_movies.iloc[0]["title"]

    # Find movie index
    idx = movies[movies["title"] == movie].index[0]

    # Calculate similarity
    distances = list(enumerate(similarity[idx]))

    # Sort highest similarity first
    sorted_movies = sorted(
        distances,
        key=lambda x: x[1],
        reverse=True
    )[1:6]

    recommendations = []

    for i, score in sorted_movies:

        movie_row = movies.iloc[i]

        title = movie_row["title"]

        # Get TMDB movie ID
        movie_id = movie_row["movie_id"]

        poster = fetch_poster(movie_id)
        trailer = fetch_trailer(movie_id)

        recommendations.append({
            "title": title,
            "poster": poster,
            "trailer": trailer
        })

    return recommendations


@app.route("/", methods=["GET", "POST"])
def index():

    recommendations = None

    if request.method == "POST":

        movie_name = request.form.get("movie")

        recommendations = recommend(movie_name)

    return render_template(
        "index.html",
        recommendations=recommendations
    )


@app.route("/retrain")
def retrain():

    try:
        subprocess.run(
            ["python", "trainmodel.py"],
            check=True
        )

        return "✅ Model retrained successfully!"

    except Exception as e:

        return f"❌ Retraining failed: {e}"


if __name__ == "__main__":
    app.run(debug=True)
