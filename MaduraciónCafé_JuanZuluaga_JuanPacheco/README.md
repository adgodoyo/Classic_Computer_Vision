# Detección de Granos Maduros de Café con Aprendizaje No Supervisado 
### By: Juan José Zuluaga y Juan Sebastián Pacheco

## 📌 Descripción de la aplicación y objetivos

Este proyecto tiene como objetivo implementar una herramienta automatizada para detectar granos maduros de café en imágenes de cafetos mediante técnicas de aprendizaje no supervisado. La necesidad surge en el contexto de la industria cafetera, donde una estimación precisa del estado de madurez de los granos es crucial para la planificación de la cosecha, la logística y el cumplimiento de contratos de exportación.

El modelo desarrollado busca reemplazar métodos tradicionales de muestreo manual, que resultan costosos e imprecisos, por un sistema que analiza imágenes y determina automáticamente la presencia de granos maduros.

---

## 🧠 Temas aplicados

Este proyecto aplica diversos conceptos de visión computacional y machine learning, principalmente:

- **Preprocesamiento de imágenes**:
  - Aplicación de filtros de suavizado y detección de bordes para facilitar la segmentación.
- **Segmentación**:
  - Identificación de los píxeles que corresponden a granos maduros mediante el espacioo de color LAB (principalmente en el rango de color rojo, es decir, el canal A).
- **Aprendizaje no supervisado**:
  - Uso de **KMeans**, adaptado mediante un `Pipeline` de `sklearn`, para clasificar los colores presentes en la imagen.
- **Transformadores personalizados**:
  - Implementación de una clase propia que hereda de `BaseEstimator` y `TransformerMixin` para adaptar el uso de `cv2.KMeans` a la estructura de `sklearn.pipeline`.
- **Procesamiento de contornos**:
  - Detección y dibujo de contornos para destacar los granos sobre la imagen original.

---

## 📊 Métricas y discusión de resultados

La evaluación del sistema se realizó de manera visual, analizando el resultado de la segmentación y la cantidad de granos detectados en diversas imágenes de prueba. Los resultados muestran una segmentación efectiva de los granos maduros, especialmente en imágenes con buena iluminación y contraste.

Algunos puntos destacados:
- El modelo responde bien a la identificación de tonos rojizos característicos del grano maduro.
- La detección mediante contornos permite contar y visualizar los granos de forma clara.
- La precisión puede verse afectada por condiciones de iluminación extremas o solapamiento de objetos similares en color.

---

## 📚 Referencias y herramientas especiales

- **Librerías utilizadas**:
  - `opencv-python (cv2)`
  - `numpy`, `matplotlib`
  - `scikit-learn`
- **Uso especial**:
  - Se creó una clase personalizada que hereda de `BaseEstimator` y `TransformerMixin` para poder incluir `cv2.KMeans` dentro de un `Pipeline` de `scikit-learn`. Esto permite estructurar de manera modular y extensible el flujo de transformación y clustering, facilitando su integración y ajuste.
