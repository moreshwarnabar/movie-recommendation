import os
import requests
import pandas as pd

def get_genres():
    if os.path.exists("data/movies/genres.csv"):
        return pd.read_csv("data/movies/genres.csv")
    
    url = f"https://api.themoviedb.org/3/genre/movie/list"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {os.getenv('TMDB_API_KEY')}"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        genres = response.json()["genres"]
        df = pd.DataFrame(genres)
        df.to_csv("data/movies/genres.csv", index=False)
        return df
    else:
        print(f"Failed to fetch genres. Status code: {response.status_code}")
        return None

def get_movie_data(page_num: int = 1):
    url = f"https://api.themoviedb.org/3/discover/movie?language=en-US&page={page_num}&sort_by=popularity.desc"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {os.getenv('TMDB_API_KEY')}"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        resp_json = response.json()
        movies = resp_json["results"]
        page = resp_json["page"]

        print(f"Total Movies: {resp_json['total_results']}")

        return page + 1, movies
    else:
        print(f"Failed to fetch movie data. Status code: {response.status_code}")
        return page_num, None