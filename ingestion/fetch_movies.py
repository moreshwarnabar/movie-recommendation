import os
import requests
import pandas as pd
from utils.logging import setup_logger
from utils.request_handler import fetch_data

logger = setup_logger('fetch_movies')

def get_genres() -> pd.DataFrame:
    if os.path.exists("data/genres.csv"):
        return pd.read_csv("data/genres.csv")
    
    url = f"https://api.themoviedb.org/3/genre/movie/list"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {os.getenv('TMDB_API_KEY')}"
    }

    data= fetch_data(url, headers)

    if data and data["genres"]:
        genres = data["genres"]
        df = pd.DataFrame(genres)
        df.to_csv("data/genres.csv", index=False)
        return df
    
    return None

def get_movie_data(page_num: int = 1) -> tuple[int, list]:
    url = f"https://api.themoviedb.org/3/discover/movie?language=en-US&page={page_num}&sort_by=popularity.desc"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {os.getenv('TMDB_API_KEY')}"
    }

    data = fetch_data(url, headers)

    if data and data["results"]:
        movies: list = data["results"]

        return movies
    
    return None