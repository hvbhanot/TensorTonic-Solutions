import pandas as pd

def inspect_dataframe(data):
    """
    Returns: dict with 'rows', 'cols' (ints), 'columns' (list),
    'dtypes' (dict), 'total_values' (int)
    """
    df = pd.DataFrame(data)

    m,n = df.shape

    out = {
        'rows' : int(m),
        'cols' : int(n),
        'columns' : df.columns.tolist(),
        'dtypes' : {cols : str(dtype) for cols, dtype in df.dtypes.items()},
        'total_values' : int(m*n)
    }

    return dict(out) 