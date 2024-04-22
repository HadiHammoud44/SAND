# coding=utf-8
# Copyright 2024 The Google Research Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Run feature selection with Sequential Attention."""

import os

from absl import app

from sequential_attention.experiments import hyperparams


def get_cmd(params):
  """Get command for running experiments with input parameters."""
  experiments_dir = os.path.dirname(os.path.realpath(__file__))
  experiment_file = os.path.join(experiments_dir, 'run4.py') ########### CHANGED 
  cmd = ['python', experiment_file]
  for param in params:
    cmd.append(f'--{param}={params[param]}')
  return ' '.join(cmd)


def main(_):
  base_name = 'STD1_20' ######################################### CHANGED
  base_dir = './BINARIZE'
  parameters = []
  def get_params(seed, name):
    return {
        'data_name': name,
        'algo': 'sand',  # sa, lly, seql, gl, omp
        'deep_layers': '25', ######################### CHANGED
        'alpha': 0,
        'batch_size': hyperparams.BATCH[name],
        'num_epochs_select': 2000,
        'num_epochs_fit': hyperparams.EPOCHS_FIT[name],
        'learning_rate': hyperparams.LEARNING_RATE[name],
        'decay_steps': hyperparams.DECAY_STEPS[name],
        'decay_rate': hyperparams.DECAY_RATE[name],
        'num_selected_features': 20,
        'seed': seed,
        'enable_batch_norm': False,
        'num_inputs_to_select_per_step': 1,
        'model_dir': f'{base_dir}/{name}/{base_name}_seed_{seed}/',
        'sigma': 1.0,
        'wrt': 'std',
    }

  for seed in [0]:
    parameters += [
        get_params(seed, name)
        for name in ['mice']
    ]

  for params in parameters:
    cmd = get_cmd(params)
    print(cmd)
    os.system(cmd)


if __name__ == '__main__':
  app.run(main)
