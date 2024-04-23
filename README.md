# Selection with Additive Noise Distortion

SAND is a feature selection algorithm for neural networks based on simple addition of a noise layer.

## Experiments
This project was built using `Python 3.9.2`

To download the datasets run `sh sand/experiments/get_all_data.sh`

To run the full experiments for `SAND`, run `python -m sand.experiments.experiment`

**Note:** You can change the algorithm in the `experiment` file to run the experiments for other methods

## Acknowledgements

This repository is an edited clone of [Sequential Attention](https://github.com/google-research/google-research/tree/master/sequential_attention). The original code has been modified to suit the specific needs of this project. All credit for the original code goes to the authors of the original repository.