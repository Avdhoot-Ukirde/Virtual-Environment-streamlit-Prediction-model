import streamlit as st
import pickle
import requests

movies=pickle.load(open('movie_list.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))

def fetch_poster(movie_id):
  url='https://api.themoviedb.org/3/movie/{}?api_key=2736a08daef7a534d3cf2d8c371e0427&language=en-US'.format(movie_id)
  data=requests.get(url)
  data=data.json()
  poster_path=data['poster_path']
  full_path="https://image.tmdb.org/t/p/w500"+data['poster_path']
  return full_path

def recommend(movie):
  index=movies[movies['title']==movie].index[0]
  distances=sorted(list(enumerate(similarity[index])),key=lambda x:x[1],reverse=True)
  recommended_movie_names=[]
  recommended_movie_posters=[]

  for i in distances[1:11]:
    movie_id=movies.iloc[i[0]].movie_id
    recommended_movie_names.append(movies.iloc[i[0]].title)
    recommended_movie_posters.append(fetch_poster(movie_id))
  return recommended_movie_names,recommended_movie_posters

