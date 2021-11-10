from scipy import stats

def at(trials, successes, p):
    result = stats.nbinom.pmf(trials - successes, successes, p)
    print(f"P(X = {trials}) = {result}")
    return result

def lte(trials, successes, p):
    result = stats.nbinom.cdf(trials - successes, successes, p)
    print(f"P(X <= {trials}) = {result}")
    return result

def gt(trials, successes, p):
    result = 1 - lte(trials, successes, p)
    print(f"P(X > {trials}) = {result}")
    return result

def lte_inv(prob, successes, p):
    result = successes + stats.binom.ppf(prob, successes, p)
    print(f"P(X <= x) = {prob} then x = {result}")
    return result
