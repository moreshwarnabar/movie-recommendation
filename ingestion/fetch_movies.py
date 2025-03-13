import os
import requests
import pandas as pd

def get_genres() -> pd.DataFrame:
    if os.path.exists("data/genres.csv"):
        return pd.read_csv("data/genres.csv")
    
    url = f"https://api.themoviedb.org/3/genre/movie/list"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {os.getenv('TMDB_API_KEY')}"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        genres = response.json()["genres"]
        df = pd.DataFrame(genres)
        df.to_csv("data/genres.csv", index=False)
        return df
    else:
        print(f"Failed to fetch genres. Status code: {response.status_code}")
        return None

def get_movie_data(page_num: int = 1) -> tuple[int, list]:
    url = f"https://api.themoviedb.org/3/discover/movie?language=en-US&page={page_num}&sort_by=popularity.desc"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {os.getenv('TMDB_API_KEY')}"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        resp_json: dict = response.json()
        movies: list = resp_json["results"]
        page: int = resp_json["page"]

        return page + 1, movies
    else:
        print(f"Failed to fetch movie data. Status code: {response.status_code}")
        return page_num, None