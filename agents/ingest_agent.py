import pandas as pd

def ingest_data(file_path: str) -> dict:
    """
    Ingests a CSV dataset and returns it in a dict format expected by LangGraph.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        dict: A state dictionary containing the DataFrame and metadata.
    """
    try:
        df = pd.read_csv(file_path)
        return {
            "status": "data_ingested",
            "df": df,
            "meta": {
                "rows": df.shape[0],
                "columns": df.shape[1],
                "columns_list": df.columns.tolist()
            }
        }
    except Exception as e:
        return {
            "status": "error",
            "error": str(e)
        }
