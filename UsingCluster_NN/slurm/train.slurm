#!/bin/bash
#SBATCH --job-name=train_job
#SBATCH --output=slurm_output/train_%j.out
#SBATCH --error=slurm_output/train_%j.err
#SBATCH --partition=gpu
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=32G
#SBATCH --gres=gpu:1
#SBATCH --time=04:00:00

# Cargar módulos necesarios (ajustar según el clúster)
module load python/3.8
module load cuda/11.2

# Activar el entorno virtual
source /home/tu_usuario/my_deep_learning_project/venv_example/bin/activate

# Navegar al directorio del proyecto
cd /home/tu_usuario/my_deep_learning_project

# Ejecutar el script de entrenamiento
python src/train.py --config config.yaml