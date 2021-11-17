import statistics

def avg(data):
    result = statistics.mean(data)
    print(f"Mean: {result}")
    return result

def var_pop(data):
    variance = statistics.pvariance(data)
    print(f"Population variance: {variance}")
    return variance

def var_samp(data):
    variance = statistics.variance(data)
    print(f"Sample variance: {variance}")
    return variance

def sd_pop(data):
    sd = statistics.pstdev(data)
    print(f"Population stdev: {sd}")
    return sd

def sd_samp(data):
    sd = statistics.stdev(data)
    print(f"Sample stdev: {sd}")
    return sd

def summary_pop(data):
    print(f"Population Summary Statistics for {data}")
    avg(data)
    var_pop(data)
    sd_pop(data)

def summary_samp(data):
    print(f"Sample Summary Statistics for {data}")
    avg(data)
    var_samp(data)
    sd_samp(data)