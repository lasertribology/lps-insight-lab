from pathlib import Path

import pandas as pd


def load_csv(
    csv_path: str | Path, index_col=None, verbose: bool = False
) -> pd.DataFrame:
    """
    Loads a CSV file into a Pandas DataFrame.

    Args:
        csv_name (str | pathlib.Path): path to csv file.
        index_col (int | str | None): Column to use as the DataFrame index (default is None)
        verbose (bool): If True, prints a quick summary after loading (default is False).

    Returns:
        pandas.DataFrame: The loaded data.
    """
    csv_path = Path(csv_path)
    if not csv_path.exists():
        raise FileNotFoundError(f"{csv_path} does not exist")

    df = pd.read_csv(csv_path, index_col=index_col)

    if verbose:
        print(f"Loaded {df.shape[0]} rows × {df.shape[1]} columns from\n   {csv_path}")
        print(df.head())

    return df
