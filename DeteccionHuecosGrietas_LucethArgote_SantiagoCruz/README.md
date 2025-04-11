# Clasificación de Imágenes de Pavimento: Huecos, Grietas o Estado Normal

Luceth Argote - Santiago Cruz

Este proyecto tiene como propósito el desarrollo de un modelo de clasificación automática para detectar **anomalías en pavimento** utilizando técnicas de visión por computador y aprendizaje automático. Se busca no solo obtener un modelo con buen desempeño, sino también explorar cómo influyen diferentes técnicas de preprocesamiento en la calidad final de la clasificación.

---

## 🎯 Objetivos

- Generar un modelo de clasificación capaz de distinguir entre imágenes de pavimento con **huecos**, **grietas** o en **estado normal**.
- Comparar diversos enfoques de preprocesamiento de imágenes para evaluar su impacto en el rendimiento del modelo.
- Implementar un pipeline reproducible que incluya desde la carga y transformación de datos hasta la optimización de hiperparámetros.
- Analizar métricas de desempeño a nivel global y por clase, con el fin de identificar posibles sesgos o debilidades del modelo.

---

## 🛠️ Aplicaciones

La automatización de la detección de daños en el pavimento tiene un gran potencial en múltiples áreas:

- **Mantenimiento predictivo**: permite a los gobiernos y empresas anticiparse a los problemas antes de que se vuelvan graves, reduciendo costos operativos.
- **Drones y vehículos inteligentes**: los sistemas de visión pueden ser integrados en drones o carros autónomos para monitorear el estado de las vías en tiempo real.
- **Smart Cities**: en ciudades inteligentes, este tipo de sistema puede integrarse en infraestructuras de análisis urbano para planificar intervenciones.
- **Seguridad vial**: alertas automáticas sobre el estado del pavimento pueden ayudar a prevenir accidentes de tráfico.

---

## 📦 Requisitos

Para ejecutar correctamente los notebooks y scripts de este repositorio, es necesario tener instaladas las siguientes bibliotecas de Python:

- `scikit-learn < 1.6`
- `pandas`
- `numpy`
- `tqdm`
- `xgboost`
- `opencv-python (cv2)`
- `matplotlib`

Se recomienda crear un entorno virtual y utilizar `pip` o `conda` para instalar los paquetes necesarios.

---

## 📁 Estructura del Proyecto

Este proyecto está dividido en varios notebooks y un archivo de funciones auxiliares:

- `exploratorio_sobel_prewitt.ipynb`:  
  Análisis exploratorio del comportamiento visual de los filtros **Sobel** y **Prewitt**, utilizados para detectar bordes en las imágenes.

- `exploracion_umbral_modelo.ipynb`:  
  Comparación de varios métodos de preprocesamiento (Canny, Sobel, Otsu, SIFT, ORB) aplicados a imágenes. Aquí se construye un modelo base con **XGBoost**.

- `optimizacion_hiperparametros.ipynb`:  
  Desarrollo de un pipeline que incluye preprocesamiento de imágenes, extracción de características mediante **Bag of Visual Words**, y búsqueda de hiperparámetros usando **RandomizedSearchCV** y **GridSearchCV**.

- `entrega_taller.ipynb`:  
  Ejecución final de un `GridSearchCV` focalizado únicamente en la mejora del modelo, utilizando la configuración final más efectiva.

- `funciones.py`:  
  Librería personalizada con funciones para:
  - Cargar las imágenes del dataset.
  - Visualizar imágenes seleccionadas.
  - Aplicar el pipeline de procesamiento.
  - Aplicar el pipeline de Bag of Visual Words.

---

## 📊 Métricas

Se evaluaron tres etapas principales del modelo y se resumen sus métricas más relevantes:

- **Modelo base (`exploracion_umbral_modelo`)**:
  - Accuracy general: **0.72**
  - Precision, Sensibilidad y F1 por clase: ≥ **0.59**

- **Modelo optimizado (`optimizacion_hiperparametros`)** con `RandomizedSearchCV`:
  - Accuracy general: **0.74**
  - Precision, Sensibilidad y F1 por clase: ≥ **0.62**

- **Modelo final (`entrega_taller`)** con `GridSearchCV`:
  - Accuracy general: **0.78**
  - Precision, Sensibilidad y F1 por clase: ≥ **0.62**

Estas métricas indican una mejora progresiva en el rendimiento del modelo conforme se aplicaron técnicas más avanzadas de procesamiento y ajuste de hiperparámetros.

---

## 🔗 Referencia

Las imágenes utilizadas para este proyecto fueron tomadas del siguiente artículo académico. Únicamente se emplearon las imágenes disponibles en la carpeta **"Training"** del conjunto de datos.

> Chu, H., Saeed, M.R., Rashid, J., Mehmood, M.T., Ahmad, I. et al. (2023).  
> *Deep Learning Method to Detect the Road Cracks and Potholes for Smart Cities*.  
> Computers, Materials & Continua, 75(1), 1863–1881.  
> [https://doi.org/10.32604/cmc.2023.035287](https://doi.org/10.32604/cmc.2023.035287)

---

## ✅ Conclusión

Este proyecto demuestra cómo una combinación adecuada de preprocesamiento, selección de características y técnicas de optimización puede conducir a modelos de clasificación visual robustos y aplicables a problemas reales. La metodología desarrollada permite extender el análisis a nuevos tipos de anomalías o adaptarse fácilmente a otros contextos visuales.
