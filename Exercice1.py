##### Fonctions

def polynome(x):
    return  x**3 - 1.5*(x**2) - 6*x + 5

def factorielle(n):
    if (n<=1):
        return 1
    else:
        return n *factorielle(n-1)

def fibonacci(n):
   if n <= 1:
       return n
   else:
       return(fibonacci(n-1) + fibonacci(n-2))


##### Test

# Polynome
print('Test de la fonction Polynome(5) : '+ str(polynome(5)))

# Factorielle
print('Test de la fonction Factorielle(5) : '+ str(factorielle(5)))

# Fibonnaci
print('Test de la fonction Fibonacci')
nombre = int(input('Entrez un nombre : '))  
print('La suite Fibonacci est :')  
for i in range(nombre):  
    print(fibonacci(i))  