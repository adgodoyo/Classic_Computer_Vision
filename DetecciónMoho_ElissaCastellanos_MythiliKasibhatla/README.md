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

- **Modelos:** KNN, Random Forest, Logistic Regression, Support Vector Machine y Gradient Boosting.
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

5. **Clasificación utilizando Pipeline, GridCV de Scikit-learn**
   - StandardScaler: Normaliza los histogramas BoVW para mejorar el rendimiento de los clasificadores sensibles a la escala.
   - *Pipeline* de Scikit-Learn: Se integraron pasos de preprocesamiento y clasificación para asegurar una validación cruzada coherente.
   - Se evaluaron cinco modelos de clasificación con *GridSearchCV* (validación cruzada con cv=3):
  
| Modelo               | Accuracy en Validación |
|----------------------|------------------------|
| K-Nearest Neighbors  | 0.8333                 |
| Random Forest        | 0.8000                 |
| Logistic Regression  | 0.8000                 |
| Support Vector Machine (SVM) | 0.7750         |
| Gradient Boosting    | 0.7750                 |

### Resultados del Mejor Modelo: K-Nearest Neighbors (KNN)

**Accuracy en validación:** 0.8333  
**Accuracy en test:** 0.8667

#### Classification Report

| Clase   | Precisión | Recall | F1-Score | Soporte |
|---------|-----------|--------|----------|---------|
| Fresh   | 0.81      | 0.97   | 0.88     | 30      |
| Rotten  | 0.96      | 0.77   | 0.85     | 30      |
| **Accuracy total**       |        |        | **0.87**     | **60**    |
| Macro avg | 0.88      | 0.87   | 0.87     | 60      |
| Weighted avg | 0.88   | 0.87   | 0.87     | 60      |

#### Matriz de Confusión

|               | Predicho Fresh | Predicho Rotten |
|---------------|----------------|-----------------|
| Actual Fresh  | 29             | 1               |
| Actual Rotten | 7              | 23              |

#### Análisis

El modelo KNN ha demostrado ser el más eficaz en validación y prueba, alcanzando un **accuracy del 86.67% en el conjunto de test**. La clase *Fresh* fue identificada con alta recall (0.97), lo que indica que el modelo detecta casi todos los casos verdaderos de fruta fresca. En contraste, la clase *Rotten* tiene una precisión notable (0.96), lo que significa que la mayoría de las predicciones de fruta podrida fueron correctas, aunque su recall (0.77) es más bajo, indicando algunos falsos negativos.

La matriz de confusión confirma este comportamiento: se clasificó correctamente la mayoría de los ejemplos, aunque 7 frutas podridas fueron clasificadas erróneamente como frescas. Aun así, el balance general entre precisión y recall sugiere que KNN es un modelo robusto para este problema.


## Conclusión
El sistema propuesto demuestra ser eficaz en la identificación de frutas deterioradas mediante técnicas de visión por computadora. La combinación de SIFT y BoVW permite representar de forma robusta las características de deterioro, y los clasificadores supervisados logran buenos resultados. Este enfoque puede extenderse a otros alimentos o defectos visuales.

### Posibles mejoras
Sería recomendable **aumentar el recall de la clase "podrida"**, especialmente en contextos donde detectar productos en mal estado sea crítico. También sería bueno correr el modelo con una base de datos más grande. De modo que se pueda visualizar el funcionamiento en un conjunto de datos más robusto.
