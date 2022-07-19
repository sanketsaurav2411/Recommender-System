import pandas as pd
import streamlit as st
import pickle
import requests
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
from PIL import Image
import streamlit.components.v1 as components
import codecs

st.set_page_config(
    page_title="Movie Recommender App",
    page_icon=":movie_camera:",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

hide_menu_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """
st.markdown(hide_menu_style, unsafe_allow_html=True)

selected = option_menu(
    menu_title=None,
    options=["Home", "Project", "About Us"],
    icons=["house", "file-earmark-code", "people"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
)


def fetch_poster(movie_id):
    response = requests.get(
        'https://api.themoviedb.org/3/movie/{}?api_key=907a7ba82f3f1e84c774e51ad9b7e489&language=en-US'
        .format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x1: x1[1])[1:21]

    recommended_movies = []
    recommended_movies_posters = []
    for x in movies_list:
        movie_id = movies.iloc[x[0]].movie_id
        recommended_movies.append(movies.iloc[x[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


bp = 0

if selected == "Home":
    lottie_movie1 = load_lottieurl("https://assets1.lottiefiles.com/datafiles/0BYCsvMJc8EIEvp/data.json")
    lottie_movie2 = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_CTaizi.json")
    ct1, ct2 = st.columns((2, 1))
    with ct1:
        st.markdown("""
            <div style='text-align: left;
            margin-left: 100px; 
            font-size: 45px; 
            font-family: "Century Gothic";
            font-weight: bold;
            text-shadow:  3px 3px 20px #DF3F2B, -2px 1px 10px #DFC85A;
            color: #FFFFFF;'>
            Movie Recommender System
        """, unsafe_allow_html=True)
        st_lottie(
            lottie_movie1,
            speed=0.7,
            reverse=False,
            loop=False,
            quality="high",
            width=200,
            key=None,
        )
    with ct2:
        st_lottie(
            lottie_movie2,
            speed=0.8,
            reverse=False,
            loop=True,
            quality="high",
            width=250,
            key=None,
        )

    movies_dict = pickle.load(open('movie_list.pkl', 'rb'))
    movies = pd.DataFrame(movies_dict)

    with open('./template/style2.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    similarity = pickle.load(open('similarity.pkl', 'rb'))
    cm1, cm2, cm3, cm4 = st.columns([1, 31, 10, 1])
    with cm1:
        st.write(' ')
    with cm2:
        selected_movie_name = st.selectbox(
            'Search your favorite movie here...',
            movies['title'].values,
            index=0,
        )
    with cm3:
        st.subheader(' ')
        st.text(' ')
        if st.button('Recommend'):
            names, posters = recommend(selected_movie_name)
            bp = 1
    with cm4:
        st.write(' ')

    if bp:
        lottie_ty = load_lottieurl("https://assets4.lottiefiles.com/temporary_files/jzVfLn.json")
        st.header(' ')
        st.markdown("""
            <div style='text-align: center;
            font-size: 30px; 
            font-family: "Century Gothic";
            font-weight: normal;
            text-shadow:  3px 3px 20px #028993, -2px 1px 10px #02CFD9;
            color: #FFFFFF;'>
            <img src="https://i.ibb.co/PGtdBTf/camera.png" style="width: 30px; height: 30px;" class="icon2"> </a>
            &nbsp;Movies Recommended for you...
        """, unsafe_allow_html=True)
        st.header(' ')
        st.subheader(' ')

        c1, c2, c3, c4, c5 = st.columns(5)
        j = -1
        st.subheader(' ')
        st.subheader(' ')

        st_lottie(
            lottie_ty,
            speed=0.8,
            reverse=False,
            loop=True,
            quality="high",
            height=500,
            key=None,

        )
        for i in range(0, 10):
            st.header(' ')

        while j <= 20:
            j += 1
            with c1:
                st.text(names[j])
                st.image(posters[j])
                st.subheader(' ')
            j += 1
            with c2:
                st.text(names[j])
                st.image(posters[j])
                st.subheader(' ')
            j += 1
            with c3:
                st.text(names[j])
                st.image(posters[j])
                st.subheader(' ')
            j += 1
            with c4:
                st.text(names[j])
                st.image(posters[j])
                st.subheader(' ')
            j += 1
            with c5:
                st.text(names[j])
                st.image(posters[j])
                st.subheader(' ')


if selected == "Project":
    lottie_proj2 = load_lottieurl("https://assets4.lottiefiles.com/private_files/lf30_8npirptd.json")
    lottie_proj10 = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_o6spyjnc.json")
    lottie_proj11 = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_4kx2q32n.json")

    st.header(' ')
    cl1, cl2, cl3 = st.columns(3)
    with cl1:
        st.text(' ')
    with cl2:
        st.markdown("<h1 style='text-align: center; color: grey;'>This Project</h1>", unsafe_allow_html=True)
    with cl3:
        st_lottie(
            lottie_proj2,
            speed=0.9,
            reverse=False,
            loop=True,
            quality="high",
            width=100,
            key=None,

        )

    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""<div style="text-align: justify; font-size: 24px; font-family: Bierstadt; color: 
        #CFCFDF;margin-left: 120px; width: 800px;">
        <br><br> A Web Base user-item Movie Recommendation Engine using 
        Collaborative Filtering by matrix factorizations algorithm and the recommendation based on the underlying 
        idea that if a person likes a particular movie, then with the help of dataset tags, related movies are 
        recommended. Represent our project using streamlit framework.""", unsafe_allow_html=True)

    with col2:
        st_lottie(
            lottie_proj10,
            speed=1,
            reverse=False,
            loop=True,
            quality="high",
            width=500,
            key=None,

        )

    st.subheader(' ')
    st.markdown("<h2 style='text-align: left; color: grey;margin-left: 120px;'>Know more about the Project</h2>",
                unsafe_allow_html=True)

    cl21, cl22 = st.columns([1, 2])
    with cl21:
        st_lottie(
            lottie_proj11,
            speed=0.6,
            reverse=False,
            loop=True,
            quality="high",
            width=400,
            key=None,

        )
    with cl22:
        st.subheader(' ')
        st.subheader(' ')
        st.markdown("""
            <h2 style='text-align: left;
            color: #A0D981;
            font-size: 25px; 
            font-family: "hack";
            font-weight: normal;
            margin-left: 120px;'>
            here's github repo;</h2>
        """, unsafe_allow_html=True)
        st.markdown("""
            <div style="color: #0E1117">
            __________________________
            <a href="https://github.com/">
            <img src="https://i.ibb.co/b395BLv/pngegg.png" style="width: 100px; height: 100px;" class="repo_btn" > </a>
        """, unsafe_allow_html=True)


if selected == "About Us":
    lottie_about1 = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_v1yudlrx.json")
    cl1, cl2, cl3 = st.columns(3)
    with cl1:
        st.text(' ')
    with cl2:
        st.subheader(' ')
        st.subheader(' ')
        st.markdown("<h1 style='text-align: center; color: grey;'>Our Team</h1>", unsafe_allow_html=True)
    with cl3:
        st_lottie(
            lottie_about1,
            speed=1,
            reverse=False,
            loop=True,
            quality="high",
            width=400,
            key=None,
        )

    with open('./template/style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    img1 = Image.open('./images/img11.jpeg')
    img2 = Image.open('./images/img22.jpeg')
    img3 = Image.open('./images/img33.jpeg')
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image(img1, caption=' ')
        st.markdown("""
            <div style="text-align: center; font-size: 35px; color: #CFCFDF;">
            Sanket Saurav<br>
            <div style="text-align: center; font-size: 22px; font-family: "Century Gothic"; color: rgb(174,167,175);">
            1CR20CS170
            <div style="text-align: center; font-size: 18px; font-family: "Century Gothic"; color: rgb(174,167,175);">
            BE-CSE (4<sup>th</sup> Sem) <br>
            CMRIT, Bangalore
        """, unsafe_allow_html=True)
        st.text(' ')
        st.text(' ')
        st.markdown("""
            <div style="color: #0E1117">
            <p align="center">
            <a href="https://www.linkedin.com/in/sanket-saurav-19621a17a/">
            <img src="https://www.edigitalagency.com.au/wp-content/uploads/Linkedin-logo-png-white.png"
            style="width: 30px; height: 30px;" class="icon1"> </a>
             .....
            <a href="https://github.com/sanketsaurav2411">
            <img <img src="https://i.ibb.co/b395BLv/pngegg.png"
            style="width: 30px; height: 30px;" class="icon2"></a></p>
        """, unsafe_allow_html=True)
    with col2:
        st.image(img2, caption=' ')
        st.markdown("""
            <div style="text-align: center; font-size: 35px; font-family: "Arial Rounded MT Bold"; color: #CFCFDF;">
            Shruti Sinha
            <div style="text-align: center; font-size: 22px; font-family: "Century Gothic"; color: rgb(174,167,175);">
            1CR20CS182
            <div style="text-align: center; font-size: 18px; font-family: "Century Gothic"; color: rgb(174,167,175);">
            BE-CSE (4<sup>th</sup> Sem) <br>
            CMRIT, Bangalore            
        """, unsafe_allow_html=True)
        st.text(' ')
        st.text(' ')
        st.markdown("""
            <div style="color: #0E1117">
            <p align="center">
            <a href="https://www.linkedin.com/">
            <img src="https://www.edigitalagency.com.au/wp-content/uploads/Linkedin-logo-png-white.png"
            style="width: 30px; height: 30px;" class="icon1"> </a>
             .....
            <a href="https://github.com/">
            <img <img src="https://i.ibb.co/b395BLv/pngegg.png"
            style="width: 30px; height: 30px;" class="icon2"></a></p>
        """, unsafe_allow_html=True)
    with col3:
        st.image(img3, caption=' ')
        st.markdown("""
            <div style="text-align: center; font-size: 35px; font-family: "Arial Rounded MT Bold"; color: #CFCFDF;">
            Prateek Kumar Srivastav
            <div style="text-align: center; font-size: 22px; font-family: "Century Gothic"; color: rgb(174,167,175);">
            1CR20CS141
            <div style="text-align: center; font-size: 18px; font-family: "Century Gothic"; color: rgb(174,167,175);">
            BE-CSE (4<sup>th</sup> Sem) <br>
            CMRIT, Bangalore            
        """, unsafe_allow_html=True)
        st.text(' ')
        st.text(' ')
        st.markdown("""
            <div style="color: #0E1117">
            <p align="center">
            <a href="https://www.linkedin.com/">
            <img src="https://www.edigitalagency.com.au/wp-content/uploads/Linkedin-logo-png-white.png"
            style="width: 30px; height: 30px;" class="icon1"> </a>
             .....
            <a href="https://github.com/">
            <img <img src="https://i.ibb.co/b395BLv/pngegg.png"
            style="width: 30px; height: 30px;" class="icon2"></a></p>
        """, unsafe_allow_html=True)


    def about_tab(about_html, width=1200, height=1000):
        about_file = codecs.open(about_html, 'r')
        page = about_file.read()
        components.html(page, width=width, height=height, scrolling=True)
