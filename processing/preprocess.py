import pandas as pd

def process_features(movies: list, genre_df: pd.DataFrame) -> None:
    if not movies:
        print("No movies to process.")
        return

    extracted_data: list = []
    for movie in movies:
        movie_id: int = movie["id"]
        title: str = movie["title"]
        overview: str = movie["overview"]
        genres: list = [genre_df.loc[genre_df["id"] == genre]["name"].values[0] 
                        for genre in movie["genre_ids"]]
        
        extracted_data.append({
            "movie_id": movie_id,
            "title": title,
            "overview": overview,
            "genres": genres
        })

    df = pd.DataFrame(extracted_data)