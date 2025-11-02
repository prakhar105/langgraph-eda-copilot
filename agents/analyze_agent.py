import pandas as pd

def analyze_data(state: dict) -> dict:
    df = state["df"]

    # 1. Basic stats
    stats = df.describe(include='all').to_dict()

    # 2. Correlation matrix (if numeric columns)
    corr = df.corr(numeric_only=True).to_dict()

    # 3. Value counts for top 3 categorical columns
    value_counts = {}
    for col in df.select_dtypes(include='object').columns[:3]:
        value_counts[col] = df[col].value_counts().head(5).to_dict()

    # Save to state
    return {
        **state,
        "status": "analyzed",
        "eda": {
            "summary": stats,
            "correlation": corr,
            "value_counts": value_counts
        }
    }
