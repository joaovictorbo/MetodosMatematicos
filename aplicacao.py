import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Carrega a imagem
img = Image.open("imagem.jpg")

# Converte a imagem para escala de cinza
img_gray = img.convert('LA')

# Converte a imagem para um array numpy
img_arr = np.array(img_gray)[:,:,0]

# Realiza a decomposição SVD
U, S, V = np.linalg.svd(img_arr)

# Define o número de componentes a serem mantidos
num_components = 100

# Reconstrói a imagem a partir das componentes selecionadas
reconstructed_img_arr = np.dot(U[:,:num_components], np.dot(np.diag(S[:num_components]), V[:num_components,:]))

# Plota a imagem original e a imagem reconstruída
fig, axs = plt.subplots(1, 2, figsize=(10, 5))
axs[0].imshow(img_arr, cmap='gray')
axs[0].set_title('Imagem original')
axs[1].imshow(reconstructed_img_arr, cmap='gray')
axs[1].set_title('Imagem reconstruída')
plt.show()
