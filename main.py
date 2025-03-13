from dotenv import load_dotenv
from ingestion.fetch_movies import get_genres, get_movie_data

load_dotenv()
    
def main():
    genres = get_genres()
    page_num, movies = get_movie_data()

    if movies:
        m = movies[0]
        m['genre_ids'] = [genres[genres['id'] == g]['name'].values[0] for g in m['genre_ids']]
        print(f"Movie:\n{m}")
        print(f"Num of movies: {len(movies)}")

if __name__ == "__main__":
    main()
