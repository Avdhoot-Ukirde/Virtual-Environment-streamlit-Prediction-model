
import streamlit as st
import pickle 
import requests

movies = pickle.load(open('movie_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])) ,key= lambda x: x[1], reverse=True)
    recommended_movie_names = []
    for i in distances[1:11]:

        recommended_movie_names.append(movies.iloc[i[0]].title)
    return recommended_movie_names

st.header("Movie Recommendation System")
movie_list = movies['title'].values
selected_movie = st.selectbox('Type or select a movie from the list',movie_list)

if st.button("Show Recommendation"):
    recommended_movie_names = recommend(selected_movie)
    for i in range(0,10):
        st.subheader(recommended_movie_names[i])


