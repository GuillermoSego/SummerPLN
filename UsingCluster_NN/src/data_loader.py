import yaml
from torchvision import datasets, transforms

def load_config(config_path="./config.yaml"):
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    return config

def get_datasets(dir):
    # Transformaciones para convertir las imágenes a tensores
    transform = transforms.Compose([transforms.ToTensor()])

    # Cargar los datos previamente descargados
    train_dataset = datasets.MNIST(root=dir, train=True, transform=transform, download=False)
    test_dataset = datasets.MNIST(root=dir, train=False, transform=transform, download=False)
    return train_dataset, test_dataset