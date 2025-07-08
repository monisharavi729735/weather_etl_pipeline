from etl.extract import extract
import pandas as pd

def transform():
    raw = extract()
    df = pd.DataFrame([raw])
    return df