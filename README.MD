# Proyecto de Visión por Computador Clásica

Este repositorio presenta diferentes técnicas clásicas de visión por computador y un pipeline de Machine Learning para clasificación y/o segmentación de imágenes. Se incluyen transformaciones geométricas, filtrado, extracción de características, Bag of Visual Words y modelos de clasificación (SVM, Random Forest, etc.). Además, se han guardado los modelos con los mejores hiperparámetros para que el usuario pueda utilizarlos sin reentrenar.

## 📋 Descripción General

A través del notebook se muestra el flujo completo de un proyecto de visión por computadora, donde se realizan:

1. **Transformaciones geométricas y Data Augmentation**: rotaciones, escalados o desplazamientos para aumentar la robustez del modelo.  
2. **Filtrado y Convolución**: aplicación de filtros de suavizado y resaltado de bordes (Prewitt, Sobel.).  
3. **Detección de Bordes y Umbralización**: uso de Canny, Laplacian, Otsu para segmentación y resaltar contornos.  
4. **Ecualización de Histogramas**: mejora de contraste y/o iluminación en las imágenes.  
5. **Feature Detection y Descriptores (SIFT)**: extracción de puntos clave relevantes en las imágenes.  
6. **Bag of Visual Words (BoVW) o VLAD**: construcción de un “vocabulario visual” a partir de descriptores para usar con clasificadores.  
7. **Machine Learning Pipeline en Scikit-Learn**: entrenamiento de diversos clasificadores (SVM, RandomForest, DecisionTree, XGBoost, KNN, etc.)
8. **Optimizacion de hiperparámetros**: se hizo busqueda de hiperparametros para encontrar los que maximizan la calidad del modelo
9. **Aprendizaje no supervisado**: uso de KMeans o MiniBatchKMeans para segmentación de color, agrupamiento o etiquetado automático de texturas.

## 🛠️ Librerías Principales

se han utilizado las siguientes librerías:

- **os, glob, shutil, random**: para manejo de archivos y rutas.  
- **cv2 (OpenCV)**: operaciones de filtrado, convolución y transformaciones de imagen.  
- **numpy**: para operaciones numéricas vectorizadas.  
- **matplotlib**: para visualización de imágenes y resultados.   
- **joblib**: para guardar y cargar modelos entrenados.  
- **scikit-learn (sklearn)**:  
  - Modelos de ML clásicos (SVC, RandomForest, KNN, DecisionTree, etc.)  
  - Búsqueda de hiperparámetros (`GridSearchCV`, `RandomizedSearchCV`)  
  - Métricas (`accuracy_score`, `confusion_matrix`, etc.)  
  - Transformaciones (`StandardScaler`, `LabelEncoder`, `PCA`)  
- **xgboost**: implementación de XGBClassifier.  
- **scipy**: para estadísticas y distribuciones (`uniform`, `randint`).  



## 🚀 Estructura de Procesamiento y Modelado

1. **Carga de Datos**  
   - Lectura de imágenes desde rutas definidas, con carpetas separadas por clases.
   - Las imagenes fueron obtenidas del siguiente repositorios de Kaggle https://www.kaggle.com/datasets/shuvokumarbasak4004/rose-leaf-disease-dataset?utm_source=chatgpt.com&select=Rose

2. **Preprocesamiento y Extracción de Características**  
   - Transformaciones geométricas y augmentación.  
   - Filtrado (Prewitt, Sobel) para resaltar bordes.  
   - Detección de bordes (Canny, Laplacian, etc.).  
   - Ecualización de histogramas para mejorar iluminación.  
   - Extracción de puntos clave (SIFT).  
   - Construcción de Bag of Visual Words (BoVW) con KMeans o MiniBatchKMeans.

3. **Entrenamiento de Modelos**  
   - Pipeline de Scikit-Learn (con transformaciones como StandardScaler, PCA, etc.).  
   - Clasificadores: SVM, Random Forest, DecisionTree, KNN, XGBoost.  
   - Ajuste de hiperparámetros con `GridSearchCV` y `RandomizedSearchCV`.  
   - Evaluación con accuracy, matriz de confusión, ROC/AUC, etc.

4. **Modelos Guardados**  
   - Se guardan los mejores modelos en la carpeta `modelos/` para que puedas cargarlos sin reentrenar:
  

5. **Aprendizaje no supervisado**  
   - Segmentación o clustering con KMeans y MiniBatchKMeans.  
   - Evaluación con métricas como homogeneity_score, adjusted_rand_score.


