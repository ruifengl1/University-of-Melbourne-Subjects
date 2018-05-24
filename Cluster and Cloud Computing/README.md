# HPC Instagram GeoProcessing  COMP90024

The task in this project is to implement parallelized application leveraging the
HPC facility SPARTAN. Application will search a large geocoded Instagram dataset
to identify Instagram usage (aka posts) hotspots around Melbourne.

## Getting Started

This zip file includs files

1. ```ass1_1n1c.slurm```  is used as script, and is to invoke assignment1.py with 1 node and 1 core

2. ```ass1_1n8c.slurm```  is used as script, and is to invoke assignment1.py with 1 node and 8 cores

3. ```ass1_2n8c.slurm```  is used as script, and is to invoke assignment1.py with 2 node and 8 cores

4. ```assignment1.py``` is the program that supposed to be run

5. The analysis have been given in the ```Assignment 1 report```

6. The output files for each test

## Building your application

1. login to the spartan server using ssh on terminal

2. ```sbatch ass1_1n1c.slurm``` to run application with 1 node and 1 core

3. ```sbatch ass1_1n8c.slurm``` to run application with 1 node and 8 cores

4. ```sbatch ass1_2n8c.slurm``` to run application with 2 nodes and 8 cores

5. waiting for the outputfiles

### Installing
Before running program using python, it must install open-mpi or mpich to build mpi4py.

```
brew install open-mpi or brew install mpich

pip install mpi4py
```    
## Running the tests

Type the command below to run the ```ass1.slurm``` script on the Spartan. The slurm file would run the assignment1.py with specified nodes and cores.

```
sbatch ass1.slurm
```
Or you may want to run on the single node(local computer), type the command below with specified cores avaliable
```
mpirun -np 4 python3 assignment1.py
```

### Test's results

With running posts in bigInstagram,  we could indentify these posts around Melbourne areas using melbGrid, A1-A4, B1-B4,C1-C5,D3-D5.

It takes about 50 seconds to run with 1n1c, 45 seconds with 1n8c and  46 with 2n8c (refer to output file).

## Authors
- Lawrence luo -- * initial work *
