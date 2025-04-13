# Clasificación de guayabas frescas y podridas

## _Descripción del proyecto_

La detección de frutas dañadas es muy importante para la producción agrícola y el procesamiento de frutas. Generalmente, esta detección se realiza manualmente, lo cual es un proceso ineficiente e impreciso.

Es por eso que en este proyecto se usó un conjunto de datos con imágenes de guayabas, las cuales están separadas en dos directorios según si la fruta está [fresca](https://github.com/adgodoyo/Classic_Computer_Vision/tree/grupo2_SamuelMoreno/DeterioroAlimentos_SamuelMoreno/imagenes/fresh) o [podrida](https://github.com/adgodoyo/Classic_Computer_Vision/tree/grupo2_SamuelMoreno/DeterioroAlimentos_SamuelMoreno/imagenes/rotten) y se buscó clasificar dichas imágenes según su categoría correcta. A continuación se muestran ejemplos de cada clase:

<p align="center">
  <img src="https://drive.google.com/uc?id=1dIYE4VozxHlxV7LMkzvWp-V5VFFRcR25" alt="fresh" width="280"></img>&emsp;&emsp;<img src="https://drive.google.com/uc?id=1oLhezZfGHfvm16BaiunVgqW7G-1lBAen" alt="rotten" width="320"></img>
</p>

Teniendo esto en cuenta, el objetivo principal a lo largo del estudio fue crear una aplicación práctica que incluyera un flujo de ejecución completo y funcional con transformaciones de datos, selección de características y un modelo de clasificación binaria.

## _Temas aplicados_

- **Transformaciones geométricas:** Al inicio se redimensionaron las imágenes para que todas tuvieran la misma cantidad de pixeles. Luego se aplicaron rotaciones, accercamientos y traslaciones de forma aleatoria para aumentar el conjunto de datos.

- **Ecualización de histogramas:** La preparación de datos comenzó con la definición de una función que recibe los hiperparámetros del objeto _CLAHE_ y aplica la transformación sobre un arreglo de imágenes para mejorar el contraste antes de aplicarles los otros filtros.

- **Filtrado y convolución:** Luego se definió otra función que aplica un filtro gaussiano para suavizar las imágenes del arreglo y disminuir el ruido (también recibe los hiperparámetros respectivos).

- **Detección de bordes:** El último paso de la preparación consistió en usar el algoritmo de Canny para detectar los bordes en cada una de las imágenes.

- **Pipeline de ejecución:** Para el modelamiento, se construyó un `pipeline` que incluye las tres transformaciones descritas anteriormente (esto se hizo para que el flujo de ejecución sea funcional y sólo se necesite pasar las imágenes crudas al objeto `Pipeline`). Seguido de esto, se normalizan los datos y se seleccionan las primeras $1000$ componentes principales. Al final del flujo se agregó un bosque aleatorio como clasificador y se definió con una semilla para que sus resultados de entrenamiento sean fácilmente replicables.

- **Optimización de hiperparámetros:** Durante el entrenamiento, se buscó la mejor combinación de hiperparámetros de entre $54$ opciones diferentes por medio de una validación cruzada de $6$ particiones con `GridSearchCV` ($324$ versiones en total). En cada paso del entrenamiento se mostraron las métricas de entrenamiento y validación.

## _Discusión de resultados_

La combinación de hiperparámetros que dio los mejores resultados (precisión de $83.8\\%$ en el conjunto de validación) fue la siguiente:

```py
equalize(tileGridSize = (8, 8))
detect_edges(threshold = 120)
RandomForestClassifier(n_estimators = 60, max_features = 0.2)
```

El modelo entrenado también obtuvo un desempeño satisfactorio con las imágenes del conjunto de prueba, ya que se obtuvo un accuracy de $84.1\\%$. Adicionalmente, en el [notebook](https://github.com/adgodoyo/Classic_Computer_Vision/blob/grupo2_SamuelMoreno/DeterioroAlimentos_SamuelMoreno/src/Taller_2.ipynb) se evidencia que el modelo clasifica exitosamente varias imágenes seleccionadas de forma aleatoria.

## _Referencias_

- [Fresh and Rotten Fruits Dataset for Machine-Based Evaluation of Fruit Quality](https://data.mendeley.com/datasets/bdd69gyhv8/1)
- [Joblib - running Python functions as pipeline jobs](https://joblib.readthedocs.io/en/latest/index.html#module-joblib)
- [Matplotlib: Visualization with Python](https://matplotlib.org/)
- [Numpy](https://numpy.org/)
- [OpenCV-Python Tutorials](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html)
- [scikit-learn: Machine Learning in Python](https://scikit-learn.org/stable/)
