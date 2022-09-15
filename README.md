# Installation

## System Setup
Ensure that you have java installed, cmake, and a recent c++ compiler available.

## Clone Repos

1) Clone this repository somewhere
2) Enter the repository.
    1) Clone github.com/pwelke/graph-homomorphism-network.git
    3) Clone github.com/pwelke/HomSub.git


## Building Scala Part

To compile c++ part, enter the `HomSub` and compile the code
```
cd HomSub
sh build-third-party.sh
sh build.sh
```

## Python Setup

Create a virtual environment, using python 3.7 (!) and install dependencies

conda:
```
cd graph-homomorphism-network
conda create -n expectation_complete python==3.7
conda activate expectation_complete
pip install -r requirements_dev.txt
```


# Compute Embeddings

- Download data from [here](https://drive.google.com/file/d/15w7UyqG_MjCqdRL2fA87m7-vanjddKNh/view?usp=sharing) and unzip it into `graph-homomorphism-network/data`.
- run (in the virtual environment)
```
python experiments.py
```






