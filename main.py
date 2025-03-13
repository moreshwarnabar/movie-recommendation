import pandas as pd
from dotenv import load_dotenv
from ingestion.fetch_movies import get_genres, get_movie_data
from processing.preprocess import process_features

load_dotenv()
    
def main():
    genres: pd.DataFrame = get_genres()

    page_num: int
    movies: list
    page_num, movies = get_movie_data()

    if movies:
        process_features(movies, genres)

if __name__ == "__main__":
    main()
