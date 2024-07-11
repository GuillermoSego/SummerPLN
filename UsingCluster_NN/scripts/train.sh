#!/bin/bash

# Activar el entorno virtual
source venv_example/bin/activate

# Ejecutar el script de entrenamiento
python src/train.py

# Desactivar el entorno virtual
deactivate