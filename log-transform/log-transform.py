def log_transform(values):
    """
    Apply the log1p transformation to each value.
    """
    values = np.array(values, dtype=float)

    submission = np.log(1+values)

    return submission.tolist()