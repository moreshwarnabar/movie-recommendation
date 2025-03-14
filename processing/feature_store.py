import pandas as pd

def store_features(df: pd.DataFrame) -> None:
    df.to_parquet('data/features.parquet', 
                  engine='pyarrow', index=False)