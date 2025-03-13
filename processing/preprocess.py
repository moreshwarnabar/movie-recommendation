import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

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
    
    df = encodeGenres(df, genre_df["name"].to_list())
    df = vectorizeOverview(df)

    if os.path.exists("data/preprocessed_data.csv"):
        preprocessed_df = pd.read_csv("data/preprocessed_data.csv")
        preprocessed_df = pd.concat([preprocessed_df, df], axis=0)
        preprocessed_df.to_csv("data/preprocessed_data.csv", index=False)
    else:
        df.to_csv("data/preprocessed_data.csv", index=False)

def encodeGenres(df: pd.DataFrame, genres: list) -> pd.DataFrame:
    for genre in genres:
        df[genre] = df["genres"].apply(lambda x: 1 if genre in x else 0)
    return df.drop("genres", axis=1)

def vectorizeOverview(df: pd.DataFrame) -> pd.DataFrame:
    vectorizer = TfidfVectorizer()
    overview_vectors = vectorizer.fit_transform(df["overview"])

    overview_df = pd.DataFrame(overview_vectors.toarray(), columns=vectorizer.get_feature_names_out())
    df = df.drop("overview", axis=1)

    return pd.concat([df, overview_df], axis=1)