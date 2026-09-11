from math import factorial, perm, comb

def perms_and_combs(n, r):
    """
    Returns: [permutations, combinations, factorial] as a list.
    """
    nPr = factorial(n) / factorial(n-r)

    nCr = factorial(n) / ( factorial(n-r) * factorial(r))


    return [nPr, nCr, factorial(n)]