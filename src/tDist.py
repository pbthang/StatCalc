from scipy import stats

def lte(x, dof):
    result = stats.t.cdf(x, dof)
    print(f"P(x <= {x}) = {result}")
    return result

def gt(x, dof):
    result = 1 - lte(x, dof)
    print(f"P(X > {x}) = {result}")
    return result

def lte_inv(prob, dof):
    result = stats.t.ppf(prob, dof)
    print(f"P(X <= x) = {prob} then x = {result}")
    return result
    
def gt_inv(prob, dof):
    result = stats.t.ppf(1 - prob, dof)
    print(f"P(X > x) = {prob} then x = {result}")
    return result
