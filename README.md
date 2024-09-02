# Proyecto Tecnológico. Procesamiento del Lenguaje Natural
Guillermo Segura Gómez

## Introducción
Durante el proyecto tecnológico me propuse entender y replicar el código descrito en el artículo "Connecting Large Language Models With Evolutionary Algorithms Yields Powerful Prompt Optimizers". Este trabajo se centra en optimizar los prompts utilizados en modelos de lenguaje grandes (LLMs) para mejorar su rendimiento en tareas específicas, utilizando algoritmos genéticos o evolutivos. 

Como complementó también se revisó el artículo “Towards Optimizing with Large Language Model” el cual implementa mediante lenguaje natural diferentes algoritmos matemáticos conocidos, utilizando LLMs, demostrando la eficiencia de los grandes modelos de lenguaje para realizar este tipo de algoritmos. 

El objetivo principal fue reproducir los resultados presentados en el artículo, enfocándonos particularmente en la tarea de simplificación de textos utilizando la métrica SARI. Para ello, se implementó y ajustó el código fuente proporcionado en el respositorio, adaptándolo a un entorno de prueba local. Los pasos clave que se realizaron fueron los siguientes:

1. Configuración del Entorno: Instalación y configuración de las dependencias necesarias.
2. Entendimiento del Código: Comprensión y análisis de las clases principales del código, como `Evaluator` y `Evoluter`, para entender cómo se generan y evalúan los prompts.
3. Adaptación y Simplificación del Código: Se modificó el código para ejecutarlo de manera local en un notebook de Jupyter, utilizando el IDE Visual Studio Code, ajustando las configuraciones para adaptarse las limitaciones computacionales del equipo en el que se corrió (Macbook Air M1).
4. Ejecución de Pruebas: Se realizaron múltiples pruebas con diferentes configuraciones de ejemplos y épocas para evaluar el rendimiento del modelo en la tarea de simplificación. Se compararon los resultados obtenidos con los reportados en el artículo.
5. Análisis de Resultados: Se evaluaron los resultados obtenidos analizando las puntuaciones SARI y los prompts generados para determinar la efectividad de las configuraciones probadas.

## Investigación del estado del arte

### Optimización de prompts

La optimización de prompts en PLN se refiere al proceso de diseñar y ajustar cuidadosamente las entradas (prompts) que se utilizan para guiar a un modelo de lenguaje en la generación de respuestas o en la realización de tareas específicas.

Desafíos en la Optimización de Prompts:
Espacio de Búsqueda Amplio: El espacio de posibles prompts es extremadamente grande, ya que incluye todas las combinaciones posibles de palabras y frases en un idioma dado.
Sensibilidad del Modelo: Los modelos de lenguaje pueden ser altamente sensibles a cambios sutiles en los prompts, lo que hace que la búsqueda de un prompt óptimo sea complicada.
Evaluación Costosa: Evaluar la calidad de un prompt puede ser costoso en términos de tiempo computacional, ya que cada evaluación puede requerir una inferencia completa del modelo de lenguaje.


### Introducción a los Algoritmos Genéticos
Los algoritmos genéticos (AG) son una técnica de optimización inspirada en el proceso de selección natural y genética biológica. Utilizan mecanismos como la selección, el cruce (crossover) y la mutación para evolucionar soluciones a lo largo de varias generaciones. Los AG son particularmente útiles para problemas de optimización en espacios de búsqueda grandes y complejos.

#### Componentes Clave de un Algoritmo Genético:

* Población Inicial: Un conjunto de posibles soluciones (individuos) al problema.
* Función de Fitness: Una medida que evalúa la calidad de cada solución.
* Selección: Un proceso para seleccionar las mejores soluciones para reproducirse y formar la siguiente generación.
* Crossover: Un operador que combina dos soluciones (padres) para crear una nueva solución (hijo).
* Mutación: Un operador que introduce variaciones aleatorias en las soluciones para mantener la diversidad genética.
* Iteración: El proceso se repite a lo largo de varias generaciones hasta que se alcanza un criterio de parada.

## Resultados

Para llevar a cabo los experimentos, se utilizó una MacBook Air M1 que cuenta con 8 GB de RAM y un procesador de 8 núcleos. Aunque el equipo no es de alta gama para tareas intensivas de aprendizaje automático, es suficiente para ejecutar pruebas y comparaciones. Para realizar las pruebas se utilizó la tarea de simplificación. Se probó con el modelo GPT-3.5 turbo. La métrica de evaluación para la simplificación es SARI.

### Métrica SARI

La métrica SARI (salida del sistema frente a referencias y frente a la oración de entrada) se utiliza para evaluar los sistemas automáticos de simplificación de textos. Esta métrica compara las oraciones simplificadas generadas por el sistema con las oraciones de referencia y las oraciones originales. Evalúa explícitamente la calidad de las palabras que se añaden, eliminan y mantienen por el sistema.

SARI se puede calcular de la siguiente manera:

**SARI = F1add + F1keep + Pdel**

donde:

- **F1add**: Es la puntuación F1 de n-gramas para las operaciones de adición.
- **F1keep**: Es la puntuación F1 de n-gramas para las operaciones de mantenimiento.
- **Pdel**: Es la precisión de n-gramas para las operaciones de eliminación.

### Resultados

Comparando SARI, los resultados fueron los siguientes:

| Configuración         | Mejor Puntuación SARI | Puntuación promedio SARI | Mejor Prompt                                                                 |
|-----------------------|-----------------------|--------------------------|-------------------------------------------------------------------------------|
| Artículo EvoPrompt GA  | 47.36                 | -                        | -                                                                           |
| 2 ejemplos, 20 épocas  | 39.82                 | 38.53                    | Given a complex English sentence, simplify it to make it easier to understand. |
| 2 ejemplos, 50 épocas  | 36.43                 | 35.51                    | Take a challenging English sentence and simplify it to make it easier to comprehend. |
| 20 ejemplos, 2 épocas  | 32.91                 | 31.52                    | Rephrase and simplify the given English sentence while retaining its original meaning. |
| 10 ejemplos, 2 épocas  | 33.12                 | 32.67                    | Simplify the English text without changing its meaning.                     |

### Discusión de Resultados

En el artículo de referencia, el método EvoPrompt GA alcanzó una puntuación SARI de 47.36 en la tarea de simplificación. Esta puntuación es el punto de referencia para evaluar el rendimiento del modelo local en las pruebas realizadas.

Para las pruebas se utilizaron dos configuraciones diferentes:

1. Pocos ejemplos, muchas épocas.
2. Muchos ejemplos, pocas épocas.

Aunque las puntuaciones SARI obtenidas son inferiores a las reportadas en el artículo (47.36), es importante considerar las limitaciones del entorno de prueba. Estas incluyen:

- Un número reducido de ejemplos (solo 2 en el primer ejemplo) en comparación con datasets más grandes utilizados en investigaciones formales.
- Limitaciones computacionales que restringen el número de épocas y la capacidad de realizar múltiples iteraciones de refinamiento del modelo.

A pesar de estas limitaciones, los resultados obtenidos son valiosos y, sobre todo, comparables, para entender cómo el modelo responde a diferentes configuraciones y prompts. Se destaca que el mejor prompt en ambas configuraciones está enfocado en la simplicidad y comprensión del inglés, lo cual es consistente con los objetivos de la tarea de simplificación.

## Referencias

[1] Guo, Qingyan, et al. "Connecting large language models with evolutionary algorithms yields powerful prompt optimizers." arXiv preprint arXiv:2309.08532 (2023).

[2] Guo, Pei-Fu, et al. "Towards optimizing with large language models." arXiv preprint arXiv:2310.05204 (2023).