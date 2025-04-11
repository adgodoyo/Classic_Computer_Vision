# 🧠 Sistema de Detección de Anomalías en Ropa

Este proyecto implementa un sistema de visión por computador para identificar prendas de ropa anómalas a partir de imágenes. Fue desarrollado como parte de un ejercicio práctico para aplicar técnicas clásicas de visión computacional y aprendizaje automático.

---

## 🎯 Objetivos

- Detectar prendas de ropa anómalas utilizando características visuales extraídas con métodos clásicos.
- Comparar el desempeño de un modelo base y uno optimizado con validación cruzada y aumento de datos.
- Evaluar métricas de desempeño clave para priorizar la detección efectiva de anomalías.

---

## 🛠️ Temas aplicados

A lo largo del proyecto se utilizaron técnicas de:

- **Extracción de características**: Histogramas de Gradientes Orientados (HOG) con `skimage.feature`.
- **Clasificación**: Modelos de Random Forest con `sklearn.ensemble`.
- **Optimización de hiperparámetros**: `GridSearchCV` para mejorar el desempeño del modelo.
- **Validación cruzada**: para evaluar la robustez del modelo.
- **Visualización**: uso de `matplotlib` para analizar resultados.
- **Aumento de datos**: rotaciones, volteos e iluminación simulada para enriquecer el dataset.

---

## 📈 Métricas y discusión de resultados

### ✅ Comparación de resultados

|                       | Modelo 1 (sin optimización) | Modelo 2 (opt.) |
|-----------------------|-----------------------------|-----------------|
| *Accuracy*            | 0.95                        | *0.97* ✅       |
| *Precision (Clase 1)* | 0.98                        | **0.90*         |
| *Recall (Clase 1)*    | 0.51                        | *0.72* ✅       |
| *F1-score (Clase 1)*  | 0.67                        | *0.80* ✅       |
| *Falsos negativos*    | 191                         | *111* ✅        |
| *Falsos positivos*    | 5                           | 31              |
| *Macro F1 avg*        | 0.82                        | *0.89* ✅       |

---

## 📌 Conclusiones

1. *El segundo modelo es mejor* porque:
   - Aumenta considerablemente el *recall* de la clase 1 (ropa anómala): 0.72 vs 0.51, lo cual es *clave* en este tipo de tareas donde no detectar una anomalía puede ser más grave que detectarla erróneamente.
   - Mejora el *F1-score* global de la clase 1, lo que implica mejor balance entre precisión y sensibilidad.
   - Reduce significativamente los *falsos negativos* (111 vs 191), que son los errores más costosos aquí.

2. Aunque la precisión de la clase 1 baja (de 0.98 a 0.90), el incremento en *recall y F1* hace que el segundo modelo sea más robusto para detectar anomalías.

---

## 🏁 Veredicto

✅ *El modelo 2 es preferible* en contextos donde detectar anomalías es prioritario, incluso a costa de algunos falsos positivos adicionales.

---

## 📚 Referencias

- Dataset personalizado construido a partir de imágenes simuladas / etiquetadas manualmente.
- Librerías principales:
  - [`scikit-learn`](https://scikit-learn.org/)
  - [`scikit-image`](https://scikit-image.org/)
  - [`OpenCV`](https://opencv.org/)
  - [`matplotlib`](https://matplotlib.org/)
  - [`numpy`](https://numpy.org/)
