import pandas as pd
import numpy as np

def extract_features_and_insights(state: dict) -> dict:
    df = state["df"]

    insights = {}

    # 1. Detect high cardinality categorical columns
    high_card_cols = [col for col in df.select_dtypes('object').columns if df[col].nunique() > 20]
    if high_card_cols:
        insights["high_cardinality"] = high_card_cols

    # 2. Find highly correlated numeric features (r > 0.8)
    corr = df.corr(numeric_only=True)
    correlated_pairs = []
    for i in range(len(corr.columns)):
        for j in range(i):
            if abs(corr.iloc[i, j]) > 0.8:
                correlated_pairs.append((corr.columns[i], corr.columns[j], corr.iloc[i, j]))
    if correlated_pairs:
        insights["high_correlations"] = correlated_pairs

    # 3. Skewness detection
    skewed = df.skew(numeric_only=True).sort_values(ascending=False)
    skewed_features = skewed[abs(skewed) > 1].to_dict()
    if skewed_features:
        insights["skewed_features"] = skewed_features

    # 4. Missing value summary
    missing = df.isnull().mean()
    missing_over_10 = missing[missing > 0.1].to_dict()
    if missing_over_10:
        insights["missing_data_over_10pct"] = missing_over_10

    return {
        **state,
        "insights": insights,
        "status": "features_extracted"
    }
