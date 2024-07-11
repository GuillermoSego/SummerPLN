import os
import yaml
import time
import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from model import MLP 
from evaluate import evaluate
from data_loader import get_datasets, load_config

def train(config):

    # Hiperparámetros
    _INPUT_SIZE_ = config['model']['input_size']
    _HIDDEN_SIZE_ = config['model'].get('hidden_size', 512)  # Valor predeterminado si no está en config
    _NUM_CLASSES_ = config['model']['num_classes']
    _BATCH_SIZE_ = config['training']['batch_size']
    _NUM_EPOCHS_ = config['training']['epochs']
    _LEARNING_RATE_ = config['training']['learning_rate']

    # Configuración de dispositivo
    if torch.cuda.is_available():
        device = torch.device("cuda")
    elif torch.backends.mps.is_available():
        device = torch.device("mps")
    else:
        device = torch.device("cpu")

    # Cargar datasets
    train_dataset, test_dataset = get_datasets(config['data']['raw_dir'])
    # Configurar dataloader
    train_loader = DataLoader(train_dataset, batch_size=_BATCH_SIZE_, shuffle=True)
    test_loader = DataLoader(test_dataset, batch_size=_BATCH_SIZE_, shuffle=False)

    # Instancia del modelo al dispositivo
    model = MLP(_INPUT_SIZE_, _HIDDEN_SIZE_, _NUM_CLASSES_).to(device)
    Loss = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=_LEARNING_RATE_)

    # Configuración nombre del modelo y archivos
    named_tuple = time.localtime()
    time_string = time.strftime("%H:%M:%S", named_tuple)

    # Crear directorio de checkpoints y logs si no existen
    os.makedirs(config['training']['checkpoint_dir'], exist_ok=True)
    os.makedirs(config['training']['log_dir'], exist_ok=True)
    
    log_file = os.path.join(config['training']['log_dir'], time_string + ' training_log.csv')

    # Abrir archivo de logs
    with open(log_file, 'w') as f:
        f.write('epoch,loss,accuracy\n')

    # Ciclo de entrenamiento
    for epoch in range(_NUM_EPOCHS_): 

        avg_loss = 0  # Inicializar avg_loss para cada época

        # Iteramos sobre los batchs
        for i, (x, labels) in enumerate(train_loader):

            # Mover tensores al dispositivo
            x = x.to(device)
            labels = labels.to(device)

            # Calcular la predicción el modelo y la pérdida
            pred_vec = model(x)
            loss     = Loss(input = pred_vec, target = labels)
            avg_loss += loss

            optimizer.zero_grad() # Reinicar gradiente
            loss.backward() # Calcular los gradientes
            optimizer.step() # Realizar el siguiente paso en el descenso de grad

        # Calcular el promedio de la pérdida
        avg_loss /= len(train_loader) 

        # Evaluar el modelo en el conjunto de prueba
        accuracy = evaluate(model, test_loader, device)
        
        # Escribir resultados en el archivo de logs
        with open(log_file, 'a') as f:
            f.write(f'{epoch+1},{avg_loss:.4f},{accuracy:.4f}\n')
        
    # Guardar los parámetros del modelo
    checkpoint_path = os.path.join(config['training']['checkpoint_dir'], time_string + ' model.pth')
    torch.save(model.state_dict(), checkpoint_path)

if __name__ == "__main__":
    config = load_config()
    train(config)