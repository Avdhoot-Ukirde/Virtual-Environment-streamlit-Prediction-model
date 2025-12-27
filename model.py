import streamlit as st
import pickle
import requests
import joblib

# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬",
    layout="wide"
)

# ---------------- LOAD DATA ----------------
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = joblib.load('similarity_compressed.pkl')

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
body {
    background-color: #0f0f0f;
}
.main {
    background-color: #0f0f0f;
}
h1 {
    color: #e50914;
    font-size: 60px;
    text-align: center;
}
h3 {
    text-align: center;
    color: #b3b3b3;
}
.movie-card {
    background-color: #181818;
    padding: 15px;
    border-radius: 12px;
    transition: transform 0.3s;
}
.movie-card:hover {
    transform: scale(1.05);
}
.movie-title {
    text-align: center;
    font-weight: bold;
    color: white;
    margin-top: 10px;
}
img {
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- FUNCTIONS ----------------
def fetch_poster(movie_id):
    api_key = "d07d0518e173b028b74dd7bc809ec9e7"
    url = f"https://api.themoviedb.org/3/movie/{int(movie_id)}?api_key={api_key}&language=en-US"
    data = requests.get(url).json()

    if data.get("poster_path"):
        return "https://image.tmdb.org/t/p/w500" + data["poster_path"]

    return "https://via.placeholder.com/500x750?text=No+Poster"


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(
        list(enumerate(similarity[index])),
        key=lambda x: x[1],
        reverse=True
    )

    names, posters = [], []
    for i in distances[1:11]:
        movie_id = movies.iloc[i[0]].movie_id
        names.append(movies.iloc[i[0]].title)
        posters.append(fetch_poster(movie_id))

    return names, posters

# ---------------- UI ----------------
st.markdown("<h1>🎬 Movie Recommender</h1>", unsafe_allow_html=True)
st.markdown("<h3>Find movies you'll love using Machine Learning</h3>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

movie_list = movies['title'].values
selected_movie = st.selectbox("🎥 Select a movie", movie_list)

if st.button("🚀 Recommend Movies"):
    with st.spinner("Finding the best movies for you... 🍿"):
        names, posters = recommend(selected_movie)

    st.markdown("## ⭐ Recommended Movies")

    # 5 x 2 Grid
    for row in range(0, 10, 5):
        cols = st.columns(5)
        for col, i in zip(cols, range(row, row + 5)):
            with col:
                st.markdown('<div class="movie-card">', unsafe_allow_html=True)
                st.image(posters[i], use_container_width=True)
                st.markdown(
                    f"<div class='movie-title'>{names[i]}</div>",
                    unsafe_allow_html=True
                )
                st.markdown('</div>', unsafe_allow_html=True)
