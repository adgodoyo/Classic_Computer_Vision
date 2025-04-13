# Proyecto: Detección de Huecos y Grietas en Carreteras  
Taller 2 - Introducción a la Visión por Computadora

## Descripción General

Este proyecto consiste en la detección y clasificación de defectos en carreteras, específicamente huecos y grietas, a partir de imágenes.

El dataset utilizado fue obtenido del paper:  
*Deep Learning Method to Detect the Road Cracks and Potholes for Smart Cities.* Se usaron las imágenes del set Test y Validation.

## Librerías Utilizadas

- OpenCV
- Albumentations
- NumPy
- Scikit-learn
- Matplotlib
- XGBoost

## Objetivo del Proyecto

Desarrollar un pipeline de clasificación de imágenes que permita identificar el estado de un segmento de carretera en base a:

- Imágenes de entrada.
- Procesamiento y extracción de características.
- Clasificación.

## Estructura del Notebook

### 1. Transformaciones Geométricas y Data Augmentation
Aplicación de técnicas de aumento de datos como rotaciones, escalados, flips, y cambios de brillo/contraste para generar un dataset más amplio.

### 2. Filtrado y Convolución
Uso de filtros como Sobel para realce de bordes y detección de contornos que resalten los defectos en la carretera.

### 3. Detección de Bordes y Umbralización
Aplicación de Otsu para destacar zonas importantes de las imágenes.

### 4. Feature Detection y Descriptores
Extracción de puntos clave utilizando algoritmos como SIFT y SURF para describir patrones característicos de huecos y grietas.

### 5. Bag of Visual Words (BoVW)
Construcción de un vocabulario visual mediante clustering (KMeans) sobre los descriptores para representar las imágenes como histogramas.

### 6. Machine Learning Pipeline
Integración de las etapas anteriores en un pipeline de Scikit-Learn para automatizar el flujo de preprocesamiento y clasificación.

### 7. Optimización de Hiperparámetros
Uso de búsqueda en rejilla (`HalvingGridSearchCV` y `HalvingRandomSearchCV`) para encontrar los mejores parámetros del clasificador.

### 8. Resultados 

| Métrica    | XGBoost (Parámetros Default) | XGBoost (Random Grid Search) |
|------------|-------------------------------|-------------------------------|
| Accuracy   | 0.8127                        | 0.8021                        |
| Precision  | 0.8044                        | 0.7928                        |
| Recall     | 0.8127                        | 0.8021                        |
| F1-Score   | 0.8047                        | 0.7908                        |

Aunque inicialmente se pensaba que el ajuste de hiperparámetros mediante Random Grid Search iba a mejorar el rendimiento del modelo, los resultados obtenidos muestran que con los parámetros por defecto de XGBoost se logró un mejor desempeño en todas las métricas evaluadas sobre el conjunto de prueba.


## Autores

- Jerónimo Manriquez  
- Wilberson Osorio  

Curso de Visión por Computador  
Universidad del Rosario — 2025