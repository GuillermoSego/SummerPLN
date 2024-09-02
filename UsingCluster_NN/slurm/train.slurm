#!/bin/bash

# Partición en la que se va a ejecutar
#SBATCH --partition=GPU

# Nombre del trabajo
#SBATCH --job-name=GuillermoS_NN

# Número de tareas (usualmente 1 para trabajos de GPU)
#SBATCH --ntasks=1

# Archivo de log donde quedará lo que imprima su software por pantalla
#SBATCH --output=result_python.log

# Archivo de error donde se guardarán los errores del trabajo
#SBATCH --error=error_python.log

# Memoria máxima a utilizar en cada nodo (opcional)
#SBATCH --mem=0

# Tiempo máximo de ejecución
#SBATCH --time=01:00:00

# Cambiar al directorio de trabajo
cd /home/est_posgrado_guillermo.segura/UsingCluster_NN

# Activar el entorno virtual
# source venv_example/bin/activate

# Verificar la ubicación de python y pip (opcional)
which python3
which pip

# Verificar la versión de Python (opcional, para asegurarse de que se usa el correcto)
python3 --version

pip list

# Ejecutar el script de Python
python3 src/train.py

# Desactivar el entorno virtual
# deactivate
