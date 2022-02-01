import math


def d1(S,X,T,r,v):
    return math.log(S / X) + (r + v ** 2 / 2) * T

def d2(S,X,T,r,v):
    return d1(S, X, T, r, v) - v * math.sqrt(T)


def c(S,X,T,r,v,N):
    return S * d1(S, X, T, r, v) * N - X * N * d2(S, X, T, r, v) * math.exp(-r * T)

def p(S,X,T,r,v,N):
    return X * N * -d2(S, X, T, r, v) * math.exp(-r * T) - S * -d1(S,X, T, r, v) * N


# Test 
print(p(1500,1200,0.3,0.9,10.2,12))
  
