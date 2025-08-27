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

st.header("Movie Recommender System")
movie_list=movies['title'].values
selected_movie=st.selectbox("Type or select a movie from the list",movie_list)

if st.button("Show Recommendations"):
  recommended_movie_names,recommended_movie_posters=recommend(selected_movie)
  c1,c2,c3,c4,c5,c6,c7,c8,c9,c10=st.tabs(["Movie 1","Movie 2","Movie 3","Movie 4","Movie 5","Movie 6","Movie 7","Movie 8","Movie 9","Movie 10"])
  with c1:
    st.text(recommended_movie_names[0])
    st.image(recommended_movie_posters[0])
  with c2:
    st.text(recommended_movie_names[1])
    st.image(recommended_movie_posters[1])
  with c3:
    st.text(recommended_movie_names[2])
    st.image(recommended_movie_posters[2])
  with c4:
    st.text(recommended_movie_names[3])
    st.image(recommended_movie_posters[3])
  with c5:
    st.text(recommended_movie_names[4])
    st.image(recommended_movie_posters[4])
  with c6:
    st.text(recommended_movie_names[5])
    st.image(recommended_movie_posters[5])
  with c7:
    st.text(recommended_movie_names[6])
    st.image(recommended_movie_posters[6])
  with c8:
    st.text(recommended_movie_names[7])
    st.image(recommended_movie_posters[7])
  with c9:
    st.text(recommended_movie_names[8])
    st.image(recommended_movie_posters[8])
  with c10:
    st.text(recommended_movie_names[9])
    st.image(recommended_movie_posters[9])
