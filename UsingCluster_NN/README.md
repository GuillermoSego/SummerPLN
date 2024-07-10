# Redes Neuronales en el cluster de CIMAT
Guillermo Segura Gómez
Maestría en Ciencias de la Computación y Matemáticas Industriales
Centro de Investigación en Matemáticas

## Descripción

Este proyecto de deep learning está diseñado para entrenar un modelo utilizando datos de imágenes. El proyecto está organizado para ejecutarse tanto de manera local como en un clúster de computación con soporte para GPUs.

## Estructura del Proyecto

```plaintext
my_deep_learning_project/
│
├── data/
│   ├── raw/                # Datos crudos descargados
│   ├── processed/          # Datos procesados
│
├── notebooks/              # Notebooks Jupyter para experimentación
│   ├── exploration.ipynb
│
├── src/                    # Código fuente del proyecto
│   ├── __init__.py
│   ├── data_loader.py      # Código para cargar y procesar datos
│   ├── model.py            # Definición del modelo
│   ├── train.py            # Script de entrenamiento
│   ├── evaluate.py         # Script de evaluación
│
├── scripts/                # Scripts para ejecutar tareas específicas
│   ├── preprocess.sh
│   ├── train.sh
│
├── slurm/                  # Scripts SLURM para ejecutar en el clúster
│   ├── train.slurm
│
├── requirements.txt        # Dependencias del proyecto
├── config.yaml             # Archivo de configuración
├── README.md               # Descripción del proyecto
├── Makefile                # Archivo Makefile para automatizar tareas
└── setup.py                # Script de instalación del paquete
```

## Requisitos

- Python 3.8+
- pip

Las dependencias adicionales están listadas en `requirements.txt`.

## Instalación

1. Clona el repositorio:

   ```bash
   git clone https://github.com/GuillermoSegoi/UsingCluster_NN.git
   cd my_deep_learning_project
   ```

2. Configura un entorno virtual e instala las dependencias:

   ```bash
   make setup
   ```

## Uso

### Entrenamiento Local

Para entrenar el modelo localmente, utiliza el comando:

```bash
make run
```

### Entrenamiento en el Clúster

1. Sube el proyecto al clúster:

   ```bash
   scp -r my_deep_learning_project <user>@<host>:~/projects/
   ```

2. Envía el trabajo al clúster utilizando SLURM:

   ```bash
   sbatch slurm/train.slurm
   ```

## Configuración

El archivo `config.yaml` contiene todos los parámetros de configuración necesarios para el proyecto. Asegúrate de ajustarlo según tus necesidades antes de ejecutar el entrenamiento.

```yaml
# config.yaml

data:
  raw_dir: "data/raw"
  processed_dir: "data/processed"

model:
  type: "ResNet50"
  input_size: [224, 224, 3]
  num_classes: 10

training:
  batch_size: 32
  epochs: 50
  learning_rate: 0.001
  checkpoint_dir: "checkpoints/"
```

## Estructura del Código

- **src/data_loader.py**: Funciones para cargar y procesar datos.
- **src/model.py**: Definición del modelo de deep learning.
- **src/train.py**: Script principal para el entrenamiento del modelo.
- **src/evaluate.py**: Script para evaluar el modelo (opcional).

## Scripts

- **scripts/preprocess.sh**: Script para preprocesar los datos.
- **scripts/train.sh**: Script para ejecutar el entrenamiento utilizando el entorno virtual.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o envía un pull request.

## Contacto

Para preguntas o sugerencias, por favor contacta a [guillermo.segura@cimat.mx](mailto:guillermo.segura@cimat.mx).
