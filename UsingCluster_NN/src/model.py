import torch
import torch.nn as nn

class MLP(nn.Module):
    # Constructor
    def __init__(self, indim, hidden, out):
        super(MLP, self).__init__()  # Iniciador

        self.estructura = nn.Sequential(  # Aplica instrucciones de manera secuencial
            nn.Flatten(),
            nn.Linear(indim, hidden),  # hidden layer
            nn.ReLU(),                 # activation
            nn.Linear(hidden, out)     # output layer
        )

    def forward(self, x):
        x = self.estructura(x)  # Ejecutamos la estructura
        return x