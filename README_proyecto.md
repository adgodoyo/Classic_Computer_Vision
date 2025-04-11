# Mythili Kasibhatla & Elissa Castellanos
# Detección de Moho y Deterioro en Alimentos

## Introducción

La detección automatizada de moho y deterioro en frutas mediante visión por computadora es un campo crítico para reducir el desperdicio de alimentos y garantizar estándares de calidad. En este trabajo, nos centramos en desarrollar un sistema de clasificación robusto para distinguir entre frutas frescas y podridas (manzanas, plátanos y naranjas), utilizando técnicas avanzadas de procesamiento de imágenes y aprendizaje automático.

## Objetivos

- Desarrollar un pipeline de procesamiento de imágenes que permita extraer características relevantes para detectar deterioro.
- Evaluar modelos de clasificación supervisada con descriptores visuales.
- Proponer una solución escalable para sistemas industriales o aplicaciones móviles.

## Temas Aplicados

### 1. Preprocesamiento de Imágenes

- **Filtros y Convolución:** Aplicación de filtros Sobel y Prewitt en las direcciones X e Y para resaltar características morfológicas clave.
- **Detección de Bordes y Umbralización:** Uso de Canny y Otsu para segmentar imágenes en regiones relevantes.
- **Ecualización de Histogramas:** Redistribución de niveles de intensidad para mejorar el contraste y la visibilidad de defectos.

### 2. Extracción de Características

- **SIFT (Scale-Invariant Feature Transform):** Extracción de puntos clave invariantes a escala, rotación e iluminación.
- **Bag of Visual Words (BoVW):** Vectorización de imágenes mediante agrupación de descriptores SIFT con KMeans, generando histogramas de palabras visuales.

### 3. Clasificación Supervisada

- **Modelos:** (Los 5 que usaste jajaja)
- **Optimización:** Grid Search para ajuste de hiperparámetros.
- **Evaluación:** Métricas como precisión y recall.



## Dataset

Se utilizó un subconjunto del dataset público [Fruits Fresh and Rotten (Kaggle)](https://www.kaggle.com/datasets/sriramr/fruits-fresh-and-rotten-for-classification). De las 13,000 imágenes originales, se seleccionaron 500 para facilitar el procesamiento y validación.

## Ejecución del Pipeline

1. **Montaje del dataset en Google Colab**
```python
from google.colab import drive
drive.mount('/content/drive')
dataset_path = "/content/drive/MyDrive/dataset_simplified"
```

2. **Preprocesamiento de Imágenes**
   - Filtros Sobel y Prewitt
   - Detección de bordes (Canny)
   - Umbralización (Otsu)
   - Ecualización de histogramas

3. **Extracción de Características**
```python
def extract_sift_features_from_images(image_list):
    sift = cv2.SIFT_create()
    descriptors_list = []
    for img in image_list:
        keypoints, descriptors = sift.detectAndCompute(img, None)
        if descriptors is not None:
            descriptors_list.append(descriptors)
    return descriptors_list
```

4. **Representación BoVW y Clasificación**
   - Agrupación de descriptores con KMeans
   - Generación de histogramas
   - Clasificación con SVM y Random Forest

5. **Acá va lo tuyo**

## Conclusión

El sistema propuesto demuestra ser eficaz en la identificación de frutas deterioradas mediante técnicas de visión por computadora. La combinación de SIFT y BoVW permite representar de forma robusta las características de deterioro, y los clasificadores supervisados logran buenos resultados. Este enfoque puede extenderse a otros alimentos o defectos visuales.
