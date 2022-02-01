def factorielle(n):

    if (not isinstance(n, int)):
        raise TypeError('l\'argument doit etre un entier')

    if(n<0):
        raise ValueError('l\'argument doit etre un entier positif')

    if (n<=1):
        return 1
    else:
        return n *factorielle(n-1)


try:
    print(factorielle(5))
except TypeError as err:
    print(err)
except ValueError as err:
    print(err)