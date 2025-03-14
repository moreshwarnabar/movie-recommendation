import os
import pandas as pd

def store_features(df: pd.DataFrame) -> None:
    if os.path.exists("data/features.parquet"):
        all_data = pd.read_parquet("data/features.parquet", engine="pyarrow")
        all_data = pd.concat([all_data, df], ignore_index=True)
        all_data.to_parquet("data/features.parquet", engine="pyarrow", index=False)
    else:
        df.to_parquet("data/features.parquet", engine="pyarrow", index=False)