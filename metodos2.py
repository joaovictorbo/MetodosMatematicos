
# Importando bibliotecas
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Função que define o termo geral de uma sequência numérica
def a(n):
    return 1/(n**2)

# Função que define o termo geral de uma sequência numérica 
# sabidamente convergentes
def b(n):
    return 1/(np.exp(n) + 1)

# Função que define o termo geral de uma sequência numérica
# sabidamente limitada porém divergente

def c(n):
    return (-1)**n

# Função que define o termo geral de uma sequência numérica
# sabidamente não limitada

def d(n):
    return np.exp(n)

func = int(input('digite 1 para a(n), 2 para b(n), 3 para c(n) e 4 para d(n): '))
if func == 1:
    nmin = int(input('Digite o valor de nmin: '))
    nmax = int(input('Digite o valor de nmax: '))
    # Criando uma lista com os valores de n
    n = np.arange(nmin, nmax + 1, 1)

    # Criando uma lista com os valores de a(n)
    an = a(n)

    # plotando o gráfico
    plt.plot(n, an, 'ro')
    plt.xlabel('n')
    plt.ylabel('a(n)')
    plt.title('Gráfico de a(n)')
    plt.show()
    #mostrando a tabela com os valores de n e a(n)
    df = pd.DataFrame({'n': n, 'a(n)': an})
    print(df)


elif func == 2:

    #ele tende a zero em L
    L = float(input('Digite o valor do limite L: '))
    eps = float(input('Digite o valor da tolerância eps: '))
    #ele fica dentro do eps 0.0001 depois do 10
    nmin = int(input('Digite o valor de nmin: '))
    nmax = int(input('Digite o valor de nmax: '))

    # Criando uma lista com os valores de n
    n = np.arange(nmin, nmax + 1, 1)

    # Criando uma lista com os valores de b(n)
    bn = b(n)

    # Criando uma lista com os valores de L + eps
    Leps = np.ones(len(n))*L + eps

    # Criando uma lista com os valores de L - eps
    Leps2 = np.ones(len(n))*L - eps

    # Criando uma lista com os valores de L
    Leps3 = np.ones(len(n))*L

    # plotando o gráfico
    plt.plot(n, bn, 'ro', n, Leps, 'b-', n, Leps2, 'b-', n, Leps3, 'g-')
    plt.xlabel('n')
    plt.ylabel('b(n)')
    plt.title('Gráfico de b(n)')
    plt.show()

    #mostrando a tabela com os valores de n e a(n)
    df = pd.DataFrame({'n': n, 'a(n)': bn})
    print(df)
elif func == 3:
    K = float(input('Digite o valor de K: '))
    M = float(input('Digite o valor de M: '))
    nmin = int(input('Digite o valor de nmin: '))
    nmax = int(input('Digite o valor de nmax: '))

    # Criando uma lista com os valores de n
    n = np.arange(nmin, nmax + 1, 1)

    # Criando uma lista com os valores de c(n)
    cn = c(n)

    # Criando uma lista com os valores de K
    Keps = np.ones(len(n))*K

    # Criando uma lista com os valores de M
    Meps = np.ones(len(n))*M

    # plotando o gráfico
    plt.plot(n, cn, 'ro', n, Keps, 'b-', n, Meps, 'b-')
    plt.xlabel('n')
    plt.ylabel('c(n)')
    plt.title('Gráfico de c(n)')
    plt.show()
    #mostrando a tabela com os valores de n e a(n)
    df = pd.DataFrame({'n': n, 'a(n)': cn})

elif func == 4:
    M = float(input('Digite o valor de M: '))
    nmin = int(input('Digite o valor de nmin: '))
    nmax = int(input('Digite o valor de nmax: '))

    # Criando uma lista com os valores de n
    n = np.arange(nmin, nmax + 1, 1)

    # Criando uma lista com os valores de d(n)
    dn = d(n)
    
    # Criando uma lista com os valores de M
    Meps = np.ones(len(n))*M

    # plotando o gráfico
    plt.plot(n, dn, 'ro', n, Meps, 'b-')
    plt.xlabel('n')
    plt.ylabel('d(n)')
    plt.title('Gráfico de d(n)')
    plt.show()
    #mostrando a tabela com os valores de n e a(n)
    df = pd.DataFrame({'n': n, 'a(n)': dn})


    