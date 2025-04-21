# Clasificación de Hojas de Tomate — Detección de Enfermedades

Este proyecto tiene como objetivo desarrollar un sistema de clasificación de hojas de tomate sanas y enfermas, utilizando técnicas de procesamiento de imágenes y modelos de machine learning. Se parte del dataset **Tomato Leaf Disease Detection** de Kaggle y se aplica un pipeline completo de preprocesamiento, extracción de características y evaluación de clasificadores.

---

## Objetivos

- Preprocesar imágenes de hojas de tomate para mejorar la calidad visual y la extracción de patrones.
- Evaluar distintas técnicas de procesamiento (filtros, bordes, ecualización, SIFT).
- Entrenar modelos supervisados para clasificar hojas sanas vs enfermas.
- Comparar métricas de rendimiento de distintos clasificadores.

---

## Temas Aplicados

| Técnica | Descripción |
|--------|-------------|
| **Transformaciones geométricas** | Aumento de datos mediante rotaciones, traslaciones, etc. |
| **Ecualización de histograma** | Mejora el contraste de la imagen |
| **Filtrado Gaussiano** | Reducción de ruido |
| **Detección de bordes (Canny)** | Extrae contornos y estructuras clave |
| **SIFT (Scale-Invariant Feature Transform)** | Extrae características locales |
| **Modelado Supervisado** | Entrenamiento y evaluación de modelos |

---

## Resultados y Discusión

El pipeline no solo permitió mejorar la calidad de los datos visuales, sino también evaluar modelos de clasificación en un conjunto consistente y bien preprocesado. A continuación, se presentan los resultados comparativos de los modelos entrenados:

| Modelo               | Accuracy | Precision | Recall | F1-Score |
|----------------------|----------|-----------|--------|----------|
| **Logistic Regression (logreg)** | 0.84     | 0.84      | 0.84   | 0.84     |
| **Gradient Boosting (gb)**       | 0.99     | 0.99      | 0.99   | 0.99     |
| **Naive Bayes (nb)**             | 0.70     | 0.75      | 0.70   | 0.69     |
| **Multi-layer Perceptron (mlp)** | 0.99     | 0.99      | 0.99   | 0.99     |
| **Extra Trees (et)**             | 0.98     | 0.98      | 0.98   | 0.98     |

### Discusión

- El **MLP** y el **gb** obtuvieron el mejor rendimiento global (99% 
accuracy), sin embargo, el mejor modelo usando el área bajo la curva fue
 **et**.
- **Naive Bayes** y **logreg**, en cambio, mostraron limitaciones claras, especialmente **nb** que fue el peor modelo por bastante.

Estos resultados reflejan que el preprocesamiento aplicado (aumento, filtros, características locales) ayudó a enriquecer la información útil para la tarea de clasificación.

---

## Dataset y Recursos

- **Dataset**: [Tomato Leaf Disease Detection (Kaggle)](https://www.kaggle.com/datasets/kaustubhb999/tomatoleaf)
- **Librerías principales**:
  - `OpenCV`
  - `scikit-learn`
  - `matplotlib`
  - `numpy`
  - `joblib`

---

## Conclusiones

El pipeline desarrollado proporciona una base sólida para sistemas de detección automática de enfermedades en plantas. La integración de técnicas de procesamiento de imagen con modelos de clasificación probados puede extenderse a otros cultivos o implementarse en entornos reales mediante aplicaciones móviles o plataformas web agrícolas.

---

## Autores

Alejandro Vega y José Mejía

