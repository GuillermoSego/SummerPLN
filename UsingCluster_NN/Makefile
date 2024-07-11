# Define variables
VENV := venv_example
PYTHON := /opt/homebrew/bin/python3
PIP := $(VENV)/bin/pip

# Crear un entorno virtual
venv: $(VENV)/bin/activate

$(VENV)/bin/activate:
	$(PYTHON) -m venv $(VENV)
	$(PIP) install --upgrade pip

# Instalar dependencias
install: venv
	$(PIP) install -r requirements.txt

# Limpiar archivos generados
clean:
	rm -rf $(VENV)
	rm -rf checkpoints/*
	rm -rf logs/*

# Definir la tarea por defecto
.DEFAULT_GOAL := install