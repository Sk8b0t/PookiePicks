from flask import Flask, render_template, request
import pandas as pd
import pickle
import numpy as np

app = Flask(__name__)

movies_data = pickle.load(open('movies.pkl', 'rb'))
similarity = np.load(open('similarity.npy', 'rb'))

if isinstance(movies_data, dict):
    movies = pd.DataFrame(movies_data)
else:
    movies = movies_data

def get_recommendations(movie_title):
    matched_movies = movies[movies['title'].str.lower() == movie_title.strip().lower()]
    
    if matched_movies.empty:
        return None 
    
    movie_index = matched_movies.index[0]
    distances = similarity[movie_index]
    
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    recommended_movies = []
    for i in movies_list:
        title = movies.iloc[i[0]].title
        score = f"{i[1] * 100:.1f}%"
        recommended_movies.append({'title': title, 'score': score})
        
    return recommended_movies

@app.route('/', methods=['GET', 'POST'])
def home():
    movie_list = movies['title'].tolist()
    selected_movie = None
    recommendations = None
    error_message = None

    if request.method == 'POST':
        selected_movie = request.form.get('movie')
        if selected_movie:
            results = get_recommendations(selected_movie)
            if results is None:
                error_message = f'Movie "{selected_movie}" was not found in the database. Please select a title from the suggestions!'
            else:
                recommendations = results

    return render_template(
        'index.html', 
        movie_list=movie_list, 
        selected_movie=selected_movie, 
        recommendations=recommendations,
        error_message=error_message
    )

if __name__ == '__main__':
    app.run(debug=True)