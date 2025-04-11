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
| **Gradient Boosting (gb)**       | 0.93     | 0.93      | 0.93   | 0.93     |
| **Naive Bayes (nb)**             | 0.70     | 0.75      | 0.70   | 0.68     |
| **Multi-layer Perceptron (mlp)** | 0.95     | 0.95      | 0.95   | 0.95     |
| **Extra Trees (et)**             | 0.89     | 0.89      | 0.89   | 0.89     |

### Discusión

- El **MLP** obtuvo el mejor rendimiento global (95% accuracy), demostrando gran capacidad de generalización.
- **Gradient Boosting** fue también altamente efectivo (93% accuracy).
- **Naive Bayes**, en cambio, mostró limitaciones claras, especialmente en el recall de la clase positiva.
- El modelo **Extra Trees** demostró buena robustez sin necesidad de una arquitectura tan compleja.

Estos resultados reflejan que el preprocesamiento aplicado (aumento, filtros, características locales) ayudó a enriquecer la información útil para la tarea de clasificación.

---

## Dataset y Recursos

- 📂 **Dataset**: [Tomato Leaf Disease Detection (Kaggle)](https://www.kaggle.com/datasets/kaustubhb999/tomatoleaf)
- 📚 **Librerías principales**:
  - `OpenCV`
  - `imgaug`
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

