import cv2
import matplotlib.pyplot as plt
import numpy as np

# Cargar imagen original
img = cv2.imread('E:/downloads/archive (12)/Train_images/Train_images/spiral/100380.jpg')  # Usa el path real
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # OpenCV carga en BGR

# Crear lista con la imagen original y transformaciones
transformaciones = [("Original", img)]

# Rotaciones
transformaciones.append(("Rot 90", cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)))
transformaciones.append(("Rot 180", cv2.rotate(img, cv2.ROTATE_180)))
transformaciones.append(("Rot 270", cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)))

# Espejos
transformaciones.append(("Flip Horizontal", cv2.flip(img, 1)))
transformaciones.append(("Flip Vertical", cv2.flip(img, 0)))

# Visualización
fig, axs = plt.subplots(2, 4, figsize=(15, 8))
axs = axs.ravel()

for i, (title, image) in enumerate(transformaciones):
    axs[i].imshow(image)
    axs[i].set_title(title)
    axs[i].axis('off')

plt.tight_layout()
plt.show()