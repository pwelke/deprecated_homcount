# Installation

## System Setup
Ensure that you have python installed, cmake, and a recent c++ compiler available.
Currently, java is also a dependency, but it is superfluous.

## Clone Repos

1) Clone this repository somewhere
2) Enter the repository.
    1) Clone github.com/pwelke/HomSub.git
    2) Clone github.com/pwelke/graph-homomorphism-network.git

```
git clone git@github.com:pwelke/homcount.git
cd homcount
git clone git@github.com:pwelke/HomSub.git
git clone git@github.com:pwelke/graph-homomorphism-network.git
```


## Building HomSub

To compile c++ part, enter the `HomSub` and compile the code

```
cd HomSub
git submodule init
git submodule update
sh build-third-party.sh
sh build.sh
```

## Python Setup

Create a virtual environment, using python 3.7 (!) and install dependencies, e.g. with anaconda:

```
cd graph-homomorphism-network
conda create -n expectation_complete python==3.7
conda activate expectation_complete
pip install -r requirements_dev.txt
```

# Compute Embeddings

- Download data from [here](https://drive.google.com/file/d/15w7UyqG_MjCqdRL2fA87m7-vanjddKNh/view?usp=sharing) and unzip it into `graph-homomorphism-network/data`.
- Run (in the virtual environment) `python experiments.py`, to only compute the embeddings of the selected datasets (if not already done) and save them in `graph-homomorphism-network/data/precompute`.
- Run (in the virtual environment) `python evaluation.py`, to compute a number of embeddings of the selected datasets (if not already done) and save them in `graph-homomorphism-network/data/precompute`. After that, run 10-fold cross validations for the MLP and SVM classifiers. 
- Note that there is currently a race condition with a temp file in . Hence, you cannot run multiple experiments simultaneously on the project folder. A workaroud would be to copy the full project folder multiple times.






