from scipy import stats

def at(x, exp):
    result = stats.poisson.pmf(x, exp)
    print(f"P(X = {x}) = {result}")
    return result

def lte(x, exp):
    result = stats.poisson.cdf(x, exp)
    print(f"P(x <= {x}) = {result}")
    return result

def gt(x, exp):
    result = 1 - lte(x, exp)
    print(f"P(X > {x}) = {result}")
    return result

def lte_inv(prob, exp):
    result = stats.poisson.ppf(prob, exp)
    print(f"P(X <= x) = {prob} then x = {result}")
    return result
