import pandas as pd
import numpy as np
import cv2
import os
import matplotlib.pyplot as plt
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.cluster import KMeans, MiniBatchKMeans

def load_images (img_directorio_path:str, classes:list):
    '''Recibe una carpeta con subcarpetas de cada clase y retorna un dataframe'''
    images_color = []
    images_gray = []
    labels = []
    for clase in classes:
        class_dir = os.path.join(img_directorio_path, clase)
        for archivo in os.listdir(class_dir):
            if archivo.lower().endswith(('.png', '.jpg', '.jpeg')):
                ruta_img = os.path.join(class_dir, archivo)
                images_color.append(cv2.imread(ruta_img, cv2.IMREAD_COLOR_RGB))
                images_gray.append(cv2.imread(ruta_img, cv2.IMREAD_GRAYSCALE))
                labels.append(clase)

    df = pd.DataFrame({'imagen color':images_color, 
                       'imagen gris': images_gray,
                       'clase':labels})
    return df


def show_images(lista_imagenes: list, nombres: list, gray: bool = True, size: int = 2) -> None:
    '''Muestra imágenes en subplots. 
       lista_imagenes: lista de listas de imágenes (columnas = clases, filas = ejemplos).
       nombres: nombre de cada clase.
    '''
    filas = len(lista_imagenes[0])
    columnas = len(lista_imagenes)

    fig, axes = plt.subplots(filas, columnas, figsize=(size * columnas, size * filas))

    # Aseguramos que axes siempre sea un arreglo 2D
    if filas == 1 and columnas == 1:
        axes = np.array([[axes]])
    elif filas == 1:
        axes = np.array([axes])
    elif columnas == 1:
        axes = np.array([[ax] for ax in axes])

    for i in range(columnas):
        for j in range(filas):
            axes[j, i].imshow(lista_imagenes[i][j], cmap='gray' if gray else None)
            axes[j, i].set_title(nombres[i] if j == 0 else "")
            axes[j, i].axis('off')

    plt.tight_layout()
    plt.show()


class ImagePreprocessor(BaseEstimator, TransformerMixin):
    '''Se define una clase la cual permite generar un preprocesamiento de las imagenes y 
    que este sea aceptado por el Pipeline de sklearn
    
    Se establecieron:
    * brightness: alfa de brillo
    * contrast: beta de constraste
    * blur: se establece un blur donde la primera coordenada es el tamaño del filtro y la segunda el sigma, si es (0,0) no se aplica
    * sobel: se establece un valor donde determina el tamaño del sobel, si es 0 no lo aplica
    * canny: se establece un canny, si es (0,0) no se aplica
    * otsu: se establece un filtro otsu
    * laplacian: se establece laplacian con el valor del ksize, si es 0 no lo aplica'''

    def __init__(self, brightness=1.0, contrast=1.0, blur=(0, 0), sobel=0, canny=(0, 0), otsu=False, laplacian=0):
        self.brightness = brightness
        self.contrast = contrast
        self.blur = blur
        self.sobel = sobel
        self.canny = canny
        self.otsu = otsu
        self.laplacian = laplacian

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        processed = []
        for img in X:
            img = cv2.convertScaleAbs(img, alpha=self.brightness, beta=self.contrast) #cambios de brillo y contraste

            if self.blur != (0,0):
                img = cv2.GaussianBlur(img, (self.blur[0], self.blur[0]), self.blur[1]) #blur

            if self.sobel != 0:
                sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=self.sobel)  #filtro Sobel
                sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=self.sobel)
                img = cv2.magnitude(sobelx, sobely).astype(np.uint8)

            if self.canny != (0,0):
                img = cv2.Canny(img, self.canny[0], self.canny[1])   #Umbral Canny

            if self.otsu:
                _, img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)  #Umbral Otsu

            if self.laplacian != 0:
                img = cv2.Laplacian(img, cv2.CV_64F, ksize=self.laplacian) #Umbral Laplacian

            processed.append(img.astype(np.uint8))
        return processed

class BagOfVisualWords(BaseEstimator, TransformerMixin):
    '''Se establece un método para poder obtener el bag de visual words dentro del pipeline
    
    Se establecieron:
    * n_clusters: número de clusters del kmeans usado, por defecto 3
    * feature_detector: detección de características, por defecto SIFT
    * max_descriptors: Sobre el descriptor, número de descriptores que seran usados por imagen para los procesos'''
    def __init__(self, n_clusters=3, feature_detector='SIFT', max_descriptors=1000):
        self.n_clusters = n_clusters
        self.feature_detector = feature_detector
        self.max_descriptors = max_descriptors


    def _get_detector(self):                                        #detector de características
        if self.feature_detector == 'SIFT':
            return cv2.SIFT_create()
        elif self.feature_detector == 'ORB':
            return cv2.ORB_create()
        else:
            raise ValueError(f'Detector "{self.feature_detector}" no soportado')
        
    def fit(self, X, y=None):  

        '''Proceso central que realiza el entrenamiento del kmeans con todos los descriptores'''    

        detector = self._get_detector()
        all_descriptors = []

        for img in X:
            keypoints, descriptors = detector.detectAndCompute(img, None)
            
            if descriptors is not None: #Se seleccionan los descriptores más relevantes
                keypoints_ordenados = sorted(keypoints, key=lambda kp: kp.response, reverse=True)[:self.max_descriptors]  
                descriptors_ordenados = np.array([descriptors[keypoints.index(kp)] for kp in keypoints_ordenados])
                all_descriptors.append(descriptors_ordenados)

        # Concatenar todos los descriptores en una sola matriz
        all_descriptors = np.vstack(all_descriptors)
        
        # Clustering con Kmeans
        self.kmeans = KMeans(n_clusters=self.n_clusters, random_state=42)

        self.kmeans.fit(all_descriptors)
        return self

    def transform(self, X, y=None):

        '''Para cada imagen, le realiza su BoVW'''

        detector = self._get_detector()
        histograms = []

        for img in X:
            keypoints, descriptors = detector.detectAndCompute(img, None)

            if descriptors is not None:
                keypoints_ordenados = sorted(keypoints, key=lambda kp: kp.response, reverse=True)[:self.max_descriptors]
                descriptors_ordenados = np.array([descriptors[keypoints.index(kp)] for kp in keypoints_ordenados])
                words = self.kmeans.predict(descriptors_ordenados)
                hist, _ = np.histogram(words, bins=np.arange(self.n_clusters + 1))
            else:
                hist = np.zeros(self.n_clusters)

            histograms.append(hist)

        return np.array(histograms) 
        


