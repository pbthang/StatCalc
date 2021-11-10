from scipy import stats


def at(x, n, p):
    result = stats.binom.pmf(x, n, p)
    print(f"P(X = {x}) = {result}")
    return result

def lt(x, n, p):
    result = stats.binom.cdf(x - 1, n, p)
    print(f"P(X < {x}) = {result}")
    return result

def lte(x, n, p):
    result = stats.binom.cdf(x, n, p)
    print(f"P(X <= {x}) = {result}")
    return result

def gte(x, n, p):
    result = 1 - lt(x, n, p)
    print(f"P(X >= {x}) = {result}")
    return result

def gt(x, n, p):
    result = 1 - stats.binom.cdf(x, n, p)
    print(f"P(X > {x}) = {result}")
    return result

def lte_inv(prob, n, p):
    result = stats.binom.ppf(prob, n, p)
    print(f"P(X <= x) = {prob} then x = {result}")
    return result