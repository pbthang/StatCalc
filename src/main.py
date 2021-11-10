from numpy.core.fromnumeric import trace
import binomial as b
import negBinomial as nb
import poisson as po
import normal
import exponential as exp
import tDist as r
import fDist as f
import chiSq

def main():
    # X ~ B(10, 0.4) -> P(X <= 5)
    b.lte(5, 10, 0.4)

if __name__ == "__main__":
    main()