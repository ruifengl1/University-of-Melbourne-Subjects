#!/bin/bash
#SBATCH -p physical 
#SABTCH --time=0-12:00:00
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=4
#SBATCH --output=bigInstagram_2n8c.out

module load Python/3.4.3-goolf-2015a
time mpiexec python assignment1.py melbGrid.json bigInstagram.json
