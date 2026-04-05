def ridge_regression(X, y, lam):
    """
    Compute ridge regression weights using the closed-form solution.
    """
    X = np.asarray(X,dtype=float)
    y = np.asarray(y, dtype=float)

    identity_shape = (X.T@X).shape[0]
  
    w = (np.linalg.inv(X.T@X + lam*np.identity(identity_shape))) @ X.T@y

    return w      