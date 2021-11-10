from scipy import stats

def lte(x, exp, sd):
    result = stats.norm.cdf(x, exp, sd)
    print(f"P(x <= {x}) = {result}")
    return result

def gt(x, exp, sd):
    result = 1 - lte(x, exp, sd)
    print(f"P(X > {x}) = {result}")
    return result

def from_to(x1, x2, exp, sd):
    result = lte(x2, exp, sd) - lte(x1, exp, sd)
    print(f"P({x1} < X < {x2}) = {result}")
    return result

def lte_inv(prob, exp, sd):
    result = stats.norm.ppf(prob, exp, sd)
    print(f"P(X <= x) = {prob} then x = {result}")
    return result