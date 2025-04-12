# Proyecto de Clasificación de Madurez en Frutas

## Descripción  
Este proyecto busca clasificar el estado de madurez (maduro/inmaduro) en frutas como:  
🍍 Piña | 🍎 Manzana | 🍌 Banano | 🐉 Pitahaya | 🍇 Uvas  
🍋 Limón | 🥭 Mango | 🍊 Naranja | � Papaya | � Fresa | 🍈 Granada  

**Técnicas utilizadas**:  
- Visión por computadora  
- Machine Learning (SVC)  

---

## Objetivos  
✅ Aplicar preprocesamiento de imágenes para optimizar resultados  
✅ Clasificar madurez utilizando Support Vector Classifier (SVC)  
✅ Encontrar el mejor modelo mediante búsqueda aleatoria de hiperparámetros  

---

## Pipeline de Procesamiento  

### 1. Transformaciones Geométricas  
**Propósito**: Aumentar el dataset mediante data augmentation  

**Operaciones aplicadas**:  
- ↻ Rotaciones (±15°)  
- ⇅ Flips (horizontal/vertical)  
- 🔍 Zooms (in/out)  

**Output**: `resultados_simplificados/`  

---

### 2. Filtrado y Convolución  
**Propósito**: Reducción de ruido post-aumento  

**Proceso**:  
- Filtro Gaussiano (σ=0.65) → Balance entre suavizado y preservación de detalles  

**Output**: `dataset_suave/`  

---

### 3. Detección de Bordes  
**Propósito**: Resaltar cambios texturales  

**Método**:  
- Operador Laplace (kernel 3×3)  
  *Justificación*: Eficiencia computacional vs. calidad  

**Output**: `database_bordes/`  

---

### 4. Ecualización de Histogramas  
**Propósito**: Corrección de iluminación  

**Técnica**:  
- CLAHE (Contrast Limited AHE)  
  *Ventajas*:  
  - Distribución óptima de brillo  
  - Minimiza artefactos de sobre-ecualización  

**Output**: `dataset_clahe/`  

---

### 5. Extracción de Características  
**Propósito**: Generar descriptores para BoVW  

**Algoritmos**:  
- SIFT/SURF  
- *Limitación*: 25 descriptores/imagen (restricción RAM)  

---

### 6. Bag of Visual Words (BoVW)  
**Propósito**: Adaptar datos para ML tradicional  

**Proceso**:  
1. K-means (k=250 clusters)  
2. Generación de histogramas de frecuencia  

---

### 7. Modelado Machine Learning  

 Pipeline Scikit-Learn  

Pipeline([
    ('scaler', StandardScaler()),
    ('svc', SVC(kernel='linear'))
])


 Búsqueda: 3 iteraciones × 2-Fold CV

**Criterio:** Máximo accuracy

**Métricas:**
- Matriz de confusión
- Accuracy (train/test)

⚠️ **Limitado por recursos computacionales**

## Resultados

**Best Model:** `{poly}` con `C={0.21}`, `γ={0.006}`

**Performance:**
- Train Accuracy: `99.60%`
- Test Accuracy: `55.52%`
---
# Análisis de Métricas del Modelo

## Rendimiento General
📉 **Accuracy**: 55.5 %  
- Equivalente a un clasificador aleatorio (límite inferior aceptable)
- **Interpretación**: El modelo no aprende patrones significativos

## Métricas por Clase
| Métrica       | Test | Train |
|---------------|----------------------|-------------------|
| Precisión     | 55.5%                  | 99.6%               |


🔍 **Hallazgos clave**:
### Análisis de Overfitting
La gran discrepancia entre el accuracy de entrenamiento (99.6%) y test (55.5%) indica un **sobreajuste severo** (*overfitting*). El modelo ha memorizado los datos de entrenamiento en lugar de aprender patrones generalizables.

### Causas Probables

1. **Limitación de descriptores (25 features)**
   - La reducción a solo 25 descriptores puede estar eliminando información crítica

2. **Problemas en calidad de datos**
   - Al ser datos de web scraping, pueden contener:
     - Texto de marcas de agua
     - Formatos inconsistentes
     - Ruido en las muestras

---
# Referencias
Ahmed, M. S. (2022). Fruit Image Dataset (22 Classes) [Dataset]. Kaggle. https://www.kaggle.com/datasets/mdsagorahmed/fruit-image-dataset-22-classes
  