#!/bin/bash
# virtualenv SA_sub_env
# source SA_sub_env/bin/activate
# pip install --editable .

# # get data
# sh sequential_attention/experiments/get_all_data.sh

# run experiments
python -m sequential_attention.experiments.run --num_epochs=3 --data_name=mice
