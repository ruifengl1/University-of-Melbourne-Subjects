#!/bin/bash
#SBATCH -p physical 
#SABTCH --time=0-12:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --output=bigInstagram_1n1c.out

module load Python/3.4.3-goolf-2015a
time mpiexec python assignment1.py melbGrid.json bigInstagram.json
