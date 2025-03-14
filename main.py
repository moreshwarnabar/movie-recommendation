import pandas as pd
from dotenv import load_dotenv
from ingestion.fetch_movies import get_genres, get_movie_data
from processing.preprocess import process_features, store_features

load_dotenv()
    
def main():
    genres: pd.DataFrame = get_genres()

    page_num: int
    movies: list
    page_num, movies = get_movie_data()

    if movies:
        df: pd.DataFrame = process_features(movies, genres)
        store_features(df)

if __name__ == "__main__":
    main()
