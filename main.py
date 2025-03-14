import pandas as pd
from dotenv import load_dotenv
from ingestion.fetch_movies import get_genres, get_movie_data
from processing.preprocess import process_features
from processing.feature_store import store_features

load_dotenv()
    
def main():
    genres: pd.DataFrame = get_genres()

    for page in range(1, 251):
        movies: list = get_movie_data(page)
        df: pd.DataFrame = process_features(movies, genres)
        store_features(df)

if __name__ == "__main__":
    main()
