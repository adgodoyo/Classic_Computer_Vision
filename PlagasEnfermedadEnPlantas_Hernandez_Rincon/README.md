# Proyecto de Visión Computacional: Detección de Enfermedades en plantas de Manzanas

Este proyecto corresponde al Parcial 2 de la asignatura de Visión Computacional, cuyo objetivo es desarrollar un prototipo funcional de clasificación de imágenes.

---

## 👥 Integrantes del equipo
- Valentina Hernandez Quintana
- Laura Alejandra Rincón Castaño

---

## 🎯 Descripción de la Aplicación y Objetivos

La aplicación consiste en un sistema automático de clasificación de imágenes de hojas de manzano que determina si una hoja está sana o afectada por la enfermedad **Cedar Apple Rust**.

Objetivos:
- Diseñar un flujo de trabajo que integre técnicas clásicas de visión computacional.
- Construir un clasificador eficaz que generalice sobre imágenes nuevas.
- Evaluar el rendimiento mediante métricas estándar y validación cruzada.

---

## 🧠 Temas Aplicados

1. **Transformaciones Geométricas y Data Augmentation**
   - Técnicas aplicadas: rotación, flip horizontal, escalado, ajuste de brillo
   - Librería utilizada: `albumentations`
   - Aplicado sobre el set de entrenamiento para aumentar la diversidad visual

2. **Filtrado y Convolución**
   - Filtros: Sobel X, Sobel Y, Laplaciano
   - Permite detectar contornos, estructuras y bordes importantes

3. **Detección de Bordes y Umbralización**
   - Canny Edge Detection y Umbralización de Otsu
   - Usado para realzar características de contraste e iluminación variable

4. **Ecualización de Histogramas**
   - Mejora el contraste antes de la extracción de características
   - Aplicado sobre imágenes en escala de grises y canal Y de imágenes a color

5. **Feature Detection y Descriptores (SIFT)**
   - Uso de `cv2.SIFT_create()` para detectar puntos clave y extraer descriptores locales

6. **Bag of Visual Words (BoVW)**
   - KMeans sobre descriptores SIFT (50 clusters)
   - Representación vectorial homogénea por imagen mediante histogramas

7. **Machine Learning Pipeline en Scikit-Learn**
   - Pipeline modular con `StandardScaler` + `SVM`
   - Evaluado sobre datos de prueba

8. **Optimización de Hiperparámetros**
   - `GridSearchCV` con validación cruzada (5 folds)
   - Búsqueda sobre parámetros `C`, `kernel`, y `gamma` del clasificador SVM

9. **Aprendizaje no Supervisado**
   - Clustering con `KMeans` aplicado sobre descriptores BoVW
   - Visualización en 2D mediante PCA
   - Comparación visual entre clusters y clases reales

---

## 📊 Métricas y Discusión de Resultados

- **Clasificación binaria clara:** modelo logra separar eficazmente hojas sanas de enfermas

### 🧪 Limitaciones
- El modelo depende de calidad visual clara para extraer descriptores.
- Si no se detectan puntos clave, no se puede clasificar la imagen.

---

## 📚 Referencias

### Datasets:
- [New Plant Diseases Dataset (Kaggle)](https://www.kaggle.com/datasets/vipoooool/new-plant-diseases-dataset)

### Librerías Especiales:
- `kagglehub` para descarga directa desde Google Colab
- `albumentations` para aumentos geométricos de imagen
- `opencv-contrib-python` para uso de SIFT (versión contrib)

---

## 💻 Requisitos
- Python 3.10+

---

## 🔮 Posibles Mejoras Futuras
- Soporte para múltiples enfermedades y otras frutas u hortalizas
- Entrenamiento con redes neuronales ligeras (MobileNet, EfficientNet)


