from scipy import stats

def lte(x, exp):
    result = stats.expon.cdf(x, 0, exp)
    print(f"P(x <= {x}) = {result}")
    return result

def gt(x, exp):
    result = 1 - stats.expon.cdf(x, 0, exp)
    print(f"P(X > {x}) = {result}")
    return result

def lte_inv(prob, exp):
    result = stats.expon.ppf(prob, 0, exp)
    print(f"P(X <= x) = {prob} then x = {result}")
    return result