import torch
import numpy as np
print("CUDA доступна: ", torch.cuda.is_available())
print("Девайс: ", torch.cuda.get_device_name(0) if torch.cuda.is_available() else "CPU")