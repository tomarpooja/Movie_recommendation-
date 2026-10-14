# 🎬 Movie Recommendation System

A Machine Learning based Movie Recommendation System that suggests similar movies based on user selection. The application is built using Python, Flask, and recommendation algorithms to provide personalized movie suggestions through an interactive web interface.

## 🚀 Features

- Movie recommendation based on similarity scores
- Easy-to-use web interface
- Fast and accurate suggestions
- Trained machine learning model
- Responsive frontend design
- Flask-powered backend

## 📁 Project Structure

```text
Movie_recommendation-
│
├── models/                # Saved machine learning models
├── static/                # CSS, JavaScript, Images
├── templates/             # HTML templates
├── app.py                 # Main Flask application
├── trainmodel.py          # Model training script
├── .gitignore
└── README.md
```

## 🛠️ Technologies Used

- Python
- Flask
- Pandas
- NumPy
- Scikit-Learn
- HTML5
- CSS3
- Machine Learning

## 📦 Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/tomarpooja/Movie_recommendation-.git
```

### Step 2: Navigate to Project Directory

```bash
cd Movie_recommendation-
```

### Step 3: Install Required Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run the Application

```bash
python app.py
```

### Step 5: Open in Browser

```text
http://127.0.0.1:5000
```

## 🤖 Model Training

To retrain the recommendation model:

```bash
python trainmodel.py
```

The trained model files will be saved in the `models` directory.

## 🎯 How It Works

1. Movie data is collected and preprocessed.
2. Features are extracted from movie information.
3. A similarity matrix is generated using machine learning techniques.
4. Users select a movie.
5. The system recommends similar movies based on calculated similarity scores.

## 📸 Application Workflow

- User enters or selects a movie.
- Recommendation engine searches for similar movies.
- Recommended movies are displayed instantly.
- User can explore suggested movies.

## 🔮 Future Enhancements

- User authentication system
- Movie ratings and reviews
- Hybrid recommendation engine
- Integration with TMDB API
- Movie posters and trailers
- Cloud deployment support

## 👩‍💻 Author

**Pooja Tomar**

GitHub: https://github.com/tomarpooja

## ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.

## 📄 License

This project is developed for educational and learning purposes.
