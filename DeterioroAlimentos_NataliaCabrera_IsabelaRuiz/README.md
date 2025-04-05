
# 🍎 Clasificación de Manzanas: Fresh vs Rotten

## 👩‍💻 Autoras
**Isabela Ruiz** y **Natalia Cabrera**

---

## Video

https://drive.google.com/file/d/1l_XUNhV8vdx_ONVcIPBKpsIh-nUi48WK/view

---

## 🎯 Descripción del Proyecto

Este proyecto consiste en desarrollar una aplicación de visión por computador para **clasificar imágenes de manzanas como frescas o podridas**. Se implementó un pipeline completo utilizando técnicas de extracción de características, modelos de clasificación y selección de atributos.

El enfoque principal fue aplicar un modelo tipo **Bag of Visual Words (BoVW)** basado en descriptores **SIFT**, combinado con un clasificador **SVM** y técnicas de selección de características.

---

## 🧠 Temas Aplicados

| Tema                          | Aplicación en el Proyecto                                               |
|------------------------------|--------------------------------------------------------------------------|
| Extracción de características | Se usó **SIFT** para detectar puntos clave y describir texturas en las imágenes. |
| Bag of Visual Words (BoVW)   | Se agruparon los descriptores usando **KMeans** para construir un vocabulario visual. |
| Selección de características | Se utilizó `SelectKBest` con `f_classif` para reducir la dimensionalidad del histograma. |
| Clasificación                | Se entrenó un **SVM (Support Vector Machine)** con `GridSearchCV` y `RandomizedSearchCV`. |
| Evaluación de modelos        | Se usaron **matrices de confusión** y **reportes de clasificación** con `precision`, `recall` y `f1-score`. |

---

## 📊 Métricas y Resultados

Se evaluó el modelo sobre el conjunto completo de imágenes cargadas (**200 en total: 100 frescas y 100 podridas**). A continuación, se resumen los principales resultados:

- **Precisión (accuracy):** entre **0.70 y 0.85**, dependiendo de los hiperparámetros.
- **Mejor modelo:** obtenido usando `RandomizedSearchCV`, ajustando automáticamente el número de características (`k`) y el parámetro `C` del SVM.
- **Errores comunes:** algunas manzanas podridas fueron clasificadas como frescas (y viceversa), probablemente por similitudes visuales.

---

## 📦 Dataset y Librerías Usadas

**Dataset:**
- `swoyam2609/fresh-and-stale-classification` vía [`kagglehub`](https://github.com/mohithsudev/kagglehub)
- Contiene imágenes divididas en carpetas: `freshapples/` y `rottenapples/`

**Librerías principales:**
- `OpenCV` (extracción de SIFT)
- `scikit-learn` (KMeans, SelectKBest, SVM, GridSearchCV, RandomizedSearchCV)
- `matplotlib` y `seaborn` (visualización de resultados)

---

## 💬 Discusión

Se logró implementar un pipeline funcional de clasificación visual utilizando métodos tradicionales de visión por computador y aprendizaje automático. El sistema fue capaz de distinguir entre manzanas frescas y podridas con buena precisión, demostrando la viabilidad de enfoques clásicos en aplicaciones.


---

## 🖼️ Proof to Action: Interfaz Gráfica con Gradio

Como parte final del proyecto, se desarrolló una **interfaz gráfica con Gradio** que permite al usuario:

- Cargar imágenes desde la carpeta `imagenes/`
- Ver en tiempo real la predicción del sistema: si la manzana está **fresca** o **dañada**
- Obtener la **probabilidad asociada** a la predicción (precisión del modelo sobre esa imagen)

Esta interfaz facilita el uso práctico del modelo en un entorno más interactivo, ideal para fines educativos, demostraciones o integración futura en un sistema real.

