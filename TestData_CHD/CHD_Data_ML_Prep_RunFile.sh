#!/bin/bash
#BSUB -q i2c2_normal
#BSUB -R "rusage[mem=100G]"
#BSUB -M 128GB
python /home/dattarij/CHD_Data_ML_Prep.py