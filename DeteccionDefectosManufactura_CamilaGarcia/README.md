# Detección de Defectos en Manufactura - Taller 2

**Autora:** María Camila García Ramírez  
**Curso:** Visión por computadora
**Proyecto:** Clasificación automática de defectos en láminas de acero usando visión por computador.

---

## Objetivo

Desarrollar un prototipo funcional capaz de clasificar imágenes de láminas metálicas con defectos industriales, utilizando técnicas clásicas de visión por computador e inteligencia artificial.

---

## Temas aplicados

-  **Ecualización de histograma**
-  **Filtros Gaussianos**
-  **Detección de bordes (Canny)**
-  **Umbralización adaptativa (Otsu)**
-  **Bag of Visual Words con descriptores ORB + KMeans**
-  **Clasificación con Random Forest**
-  **Pipeline de Scikit-learn**
-  **Optimización de hiperparámetros con GridSearchCV**

---

## Flujo del prototipo

1. Preprocesamiento de imágenes: ecualización, suavizado, bordes y umbralización.
2. Extracción de características locales (ORB).
3. Vectorización de imágenes con Bag of Visual Words.
4. Entrenamiento de un clasificador Random Forest.
5. Optimización de hiperparámetros con `GridSearchCV`.
6. Clasificación automática de nuevas imágenes.

---

## Uso

El código se realizó en google colab, por lo tanto tiene conexiones directas con google drive, se recomienda subir los archivos de la carpeta de imágenes al drive y cambiar las ruta, los nombres son los mismos. 

Se sube archivos .py, .ipynb y un archivo con nombre modelos donde entrené varios modelos y seleccioné el mejor para aplicar al proyecto.

## Video

Debido a el peso del video, se encuentra en el siguiente link
https://youtu.be/-fmcp6UlB-4
