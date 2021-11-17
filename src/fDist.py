from scipy import stats

def lte(x, n1, n2):
    result = stats.f.cdf(x, n1, n2)
    print(f"P(x <= {x}) = {result}")
    return result

def gt(x, n1, n2):
    result = 1 -lte(x, n1, n2)
    print(f"P(X > {x}) = {result}")
    return result

def lte_inv(prob, n1, n2):
    result = stats.f.ppf(prob, n1, n2)
    print(f"P(X <= x) = {prob} then x = {result}")
    return result
    
def gt_inv(prob, n1, n2):
    result = stats.f.ppf(1 - prob, n1, n2)
    print(f"P(X > x) = {prob} then x = {result}")
    return result
