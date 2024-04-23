"""Hyperparameters for feature selection experiments"""

LEARNING_RATE = {
    'mice': 1e-3,
    'mnist': 1e-3,
    'fashion': 1e-3,
    'isolet': 1e-3,
    'coil': 1e-3,
    'activity': 1e-3,
}

BATCH = {
    'mice': 64,
    'mnist': 64,
    'fashion': 64,
    'isolet': 64,
    'coil': 64,
    'activity': 64,
}

EPOCHS = {
    'mice': 400,
    'mnist': 100,
    'fashion': 200,
    'isolet': 400,
    'coil': 1000,
    'activity': 200,
}

EPOCHS_FIT = {
    'mice': 200,
    'mnist': 50,
    'fashion': 100,
    'isolet': 200,
    'coil': 500,
    'activity': 100,
}

DEEP_LAYERS = {
    'mnist': '261',
    'fashion': '261', 
    'mice': '25', 
    'coil': '133', 
    'isolet': '205', 
    'activity': '187', 
}