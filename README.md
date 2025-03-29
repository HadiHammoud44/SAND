# Selection with Additive Noise Distortion

SAND is a feature selection algorithm for neural networks based on simple addition of a noise layer.

## Experiments
This project was built using `Python 3.9.2`

To download the datasets run `sh sand/experiments/get_all_data.sh`

To run the experiments for `SAND` on the 6 standard datasets, run `python -m sand.experiments.experiment`

**Note:** To run the experiments for `SAND` on the other datasets, change the dataset name and the corresponding number of features to select in the `experiment` file. Additionally, you can change the algorithm to run the experiments for other methods.

## SAND vs STG

<table>
  <thead>
    <tr>
      <th rowspan="2">Dataset</th>
      <th align="center" rowspan="2">Metric</th>
      <th colspan="2">Average ± Std</th>
    </tr>
    <tr>
      <th>STG</th>
      <th>SAND</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Mice</td>
      <td align="center">Accuracy</td>
      <td>0.989 ± 0.006</td>
      <td>0.988 ± 0.006</td>
    </tr>
    <tr>
      <td>Activity</td>
      <td align="center">Accuracy</td>
      <td>0.927 ± 0.006</td>
      <td>0.923 ± 0.004</td>
    </tr>
    <tr>
      <td>Isolet</td>
      <td align="center">Accuracy</td>
      <td>0.936 ± 0.005</td>
      <td>0.926 ± 0.005</td>
    </tr>
    <tr>
      <td>Coil</td>
      <td align="center">Accuracy</td>
      <td>0.997 ± 0.004</td>
      <td>0.998 ± 0.003</td>
    </tr>
    <tr>
      <td>Madelon</td>
      <td align="center">Accuracy</td>
      <td>0.642 ± 0.018</td>
      <td>0.732 ± 0.021</td>
    </tr>
    <tr>
      <td>California Housing</td>
      <td align="center">Mean Absolute Error</td>
      <td>0.577 ± 0.119</td>
      <td>0.521 ± 0.027</td>
    </tr>
  </tbody>
</table>





## Acknowledgements

This repository is an edited clone of [Sequential Attention](https://github.com/google-research/google-research/tree/master/sequential_attention). The original code has been modified to suit the specific needs of this project. All credit for the original code goes to the authors of the original repository.
