import time
import pandas as pd
from dotenv import load_dotenv
from ingestion.fetch_movies import get_genres, get_movie_data
from processing.preprocess import process_features
from processing.feature_store import store_features
from utils.logging import setup_logger

logger = setup_logger('main')

load_dotenv()
    
def main():
    genres: pd.DataFrame = get_genres()

    for page in range(1, 251):
        logger.info(f"Fetching page {page}...")
        movies: list = get_movie_data(page)

        if not movies:
            logger.warning(f"No movies found on page {page}. Skipping...")
            continue

        try:
            df: pd.DataFrame = process_features(movies, genres)
            store_features(df)
            logger.info(f"Processed and Stored features for page {page}.")
        except Exception as e:
            logger.error(f"Error processing features for page {page}: {e}")

        time.sleep(30)

if __name__ == "__main__":
    main()
