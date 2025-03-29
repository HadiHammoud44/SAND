"""Hyperparameters for feature selection experiments"""

LEARNING_RATE = {
    'mice': 1e-3,
    'isolet': 1e-3,
    'coil': 1e-3,
    'activity': 1e-3,
    'california_housing': 1e-3,
    'madelon': 1e-3,
}

BATCH = {
    'mice': 64,
    'isolet': 64,
    'coil': 64,
    'activity': 64,
    'california_housing': 64,
    'madelon': 64,
}

EPOCHS = {
    'mice': 400,
    'isolet': 400,
    'coil': 1000,
    'activity': 200,
    'california_housing': 200,
    'madelon': 500,
}

EPOCHS_FIT = {
    'mice': 200,
    'isolet': 200,
    'coil': 500,
    'activity': 100,
    'california_housing': 100,
    'madelon': 250,
}

DEEP_LAYERS = {
    'mice': 25, 
    'coil': 133, 
    'isolet': 205, 
    'activity': 187, 
    'california_housing': 3,
    'madelon': 166,
}

SIGMA = {
    'mice': 1.5,
    'isolet': 1.5,
    'coil': 1.5,
    'activity': 1.5,
    'california_housing': 1.5,
    'madelon': 1.5,
}

LAMBDA = {
    'mice': 0.048,
    'isolet': 2.2,
    'coil': 0.4,
    'activity': 0.6,
    'california_housing': 0.2,
    'madelon': 1.9,
}