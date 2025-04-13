# Reporte Parcial 2
Realizado por Juan Esteban Gonzalez y Leonardo Luengas para la clase de Introducción a la Visión por Computadora de la carrera de Matemáticas Aplicadas y Ciencias de la Computación.

## ⚠️IMPORTANTE⚠️
Para correr el notebook es **necesario** subir un archivo "kaggle.json" que tenga las credenciales de kaggle para poder usar la API y traer el dataset con el que vamos a trabajar. La segunda celda de código
  ```python
    from google.colab import files
    files.upload()
  ```
recibe este archivo y no va a correr el resto del notebook hasta que se suban las credenciales.
## Resumen del Proyecto
Este proyecto busca entrenar un modelo de Aprendizaje No Supervizado en la detección de huecos en calles y carreteras. El objetivo del modelo es determinar si dentro de una imagen de una calle o una carretera hay algún tipo de hueco. Para esto utilizamos un dataset de 681 imágenes donde alrededor del 50% (329 imágenes) de las imágenes corresponden a calles con huecos y el resto de las imágenes (352 imágenes) corresponden a calles sin huecos. Este dataset se encuentra en la siguiente [URL](https://www.kaggle.com/datasets/atulyakumar98/pothole-detection-dataset).

Implementamos un modelo de Gaussian Mixture con dos componentes correspondientes a cada clase del problema de detección de huecos. 

## Desarrollo del Proyecto
### Pipeline de Preprocesamiento
Nuestro pipeline de preprocesamiento consiste de 4 pasos.
1. ``DownScale()`` que se encarga de reducir el tamaño de todas las imágenes a 512x512 pixeles. Esto fue necesario dado que el tiempo de preprocesamiento para las imágenes con resolución original era demasiado largo y colapsaba la RAM del sistema.
2. ``ToGrayscale()`` que le aplica a las imágenes un filtro de blanco y negro.
3. ``GaussianBlur()`` que aplica un filtro gaussiano de kernle 5x5 y una desviación de 1. Encontramos que era necesario realizar este filtrado dado que la calle presentaba pequeñas irregularidades que hacían que el modelo no se enfocara en detectar el hueco. De esta forma, eliminamos el ruido dentro de la imágen sin eliminar los detalles importantes que queremos que el modelo identifique.
4. ``ApplyCanny()`` que aplica un filtro de Canny a las imágenes. Nuestro razonamiento detrás fue pensar en que el modelo tenía que detectar solamente la presencia de la *silueta* de un hueco, olvidando el resto de los detalles que pueden estar presentes en la escena.
### Pipeline de Feature Detection y Embedding
Nuestro pipeline de Feature Detection y Embedding solo implementa el algoritmo de SIFT para extraer los descriptores de la escena y el algoritmo de Bag of Visual Words para generar un embedding de menor dimensión (10) que capture las características comunes de las imágenes.

Para explorar este embedding utilizamos el algoritmo de PCA restrigindo a dos y tres componentes principales respectivamente para poder comprender la forma que tiene el embedding. Nos dimos cuenta que la mayoría de la varianza estaba en las primeras componentes. De esta forma redujimos el tamaño del bag of visual words a 10.
### Resultados del Gaussian Mixture Model (GMM)
Para evaluar el desempeño del modelo aprovechamos que el dataset dividia los tipos de imágenes y construimos un conjunto de labels verdaderos para todas las imágenes en el dataset. Asignamos el label de 0 para las imágenes en las que no hay huecos y 1 a las imágenes con huecos.

Incialmente, corrimos un modelo sin ninguna optimización de hiperparámetros y nos dio la siguiente tabla de métricas.
|                |precision  |  recall | f1-score  | support|
|----------------|----------|----------|-----------|--------|
|          0    |   0.69  |    0.75  |    0.72  |     112|
|           1    |   0.73   |   0.66   |   0.69     |  113|
|    accuracy    |          |          |   0.71   |    225|
|   macro avg     |  0.71    |  0.71   |   0.71      | 225|
|weighted avg     |  0.71    |  0.71    |  0.71     |  225|

Inicialmente, estos resultados son muy prometedores y la curva ROC resultante junto a la métrica AUC

![image](https://github.com/user-attachments/assets/1554b809-6f9d-42a3-9a4b-ee87c3b16055)

indica que tenemos un modelo que es más propenso a asignarle a una imágen la label de tener hueco. Esto es deseable dado que es más importante, considerando las aplicaciones industriales de este tipo de modelos en calles reales, detectar correctamemte los huecos más allá de asignar incorrectamente a calles en buenas condiciones el label de hueco. Es decir, es más seguro actuar como si la calle tuviera un hueco (reduciendo la velocidad, evadiendo, etc.) y, por lo tanto, la métrica de false positive rate no es tan relevante para nuestra aplicación. Por eso podemos tolerar un false positive rate alto, para maximizar la métrica de true positive en la curva ROC. A pesar de esto, podemos ver que el modelo tiene un buen desempeño para ambas clases, reflejado en un alto f1-score.

Realizamos una implementación de ``GridSearchCV()`` para optimizar los hiperparámetros de ``covariance_type`` y ``reg_covar`` para mejorar el desempeño del modelo. Nuestro método de grid_search buscaba maximizar la métrica de f1 score pero realmente no encontró un modelo con mejor desempeño que el ya encontrado anteriormente. Las métricas encontradas son las siguientes con su respectiva curva ROC:

|                |precision  |  recall | f1-score  | support|
|----------------|----------|----------|-----------|--------|
|          0    |   0.54  |    0.97  |    0.70  |     112|
|           1    |   0.88   |   0.19   |   0.31     |  113|
|    accuracy    |          |          |   0.58   |    225|
|   macro avg     |  0.71    |  0.58   |   0.50      | 225|
|weighted avg     |  0.71    |  0.58    |  0.50     |  225|

![image](https://github.com/user-attachments/assets/5ba1f76a-a4b1-43a1-9809-ea416ef88387)


## Conclusiones

El modelo tiene un buen desempeño para el objetivo de detectar huecos. Se hizo una prueba con una imágen que no había visto en el entrenamiento y la clasificó correctamente. Los resultados arrojados por ``GridSearchCV()`` nos desconciertan pero no sabemos exactamente que fue lo que ocurrió en el método para no encontrar el modelo más óptimo. Creemos que GMM no se presta muy bien para optimización de hiperparámetros. Incialmente, no tiene muchos hiperpárametros que optimizar más allá del numero de componentes, el cual ya estaba fijado al ser un problema de clasificación binaria.
