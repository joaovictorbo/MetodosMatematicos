"""
Uma popula¸c˜ao est´avel de 35.000 p´assaros vive em trˆes ilhas. Cada
ano, 10% da popula¸c˜ao da ilha A migra para ilha B, 20% da popula¸c˜ao
da ilha B migra para a ilha C e 5% da popula¸c˜ao da ilha C migra para
ilha A.
Denotando por An, Bn e Cn, respectivamente, as quantidades de
p´assaros nas ilhas A, B e C no n-´esimo ano antes da ocorrˆencia da
migra¸c˜ao e admitindo a convergˆencia das sequˆencias {An}, {Bn} e
{Cn}, aproxime a quantidade de p´assaros em cada ilha ap´os muitos
anos (independentemente da popula¸c˜ao inicial em cada ilha).
"""

import numpy as np
import matplotlib.pyplot as plt
def passaranos(x,i):
    for i in range(i):
        x = np.array([0.9*x[0] + 0.05*x[2],0.8*x[1] + 0.1*x[0],0.95*x[2] + 0.2*x[1]])
    return x

def metodos3():
    x = [400,600,1000]
    y = passaranos(x,200)
    print(y)
    plt.plot([x,y])
    plt.xlabel('inicio')
    plt.ylabel('fim')
    plt.title('Azul = A, Laranja = B, Verde = C')
    plt.show()
    

metodos3()
