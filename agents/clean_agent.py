import pandas as pd

def clean_data(state: dict) -> dict:
    df = state["df"]

    # Example cleaning steps
    df_cleaned = df.copy()

    #1. Drops rows with too many missing values NaNs
    df_cleaned = df_cleaned.dropna(thresh = int(0.6 * df_cleaned.shape[1]))

    #2. Fill numeric columns with median 
    for col in df_cleaned.select_dtypes(include = "number").columns:
        median_value = df_cleaned[col].median()
        df_cleaned[col] = df_cleaned[col].fillna(median_value)

    #3. Fill object column with mode
    for col in df_cleaned.select_dtypes(include = "object").columns:
        mode_value = df_cleaned[col].mode()[0]
        df_cleaned[col] = df_cleaned[col].fillna(mode_value)

    return {
        "status" : "data_cleaned",
        "df" : df_cleaned,
        "meta" : {
            **state.get("meta", {}),
            "cleaned" : True
        } 
    }
