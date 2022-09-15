# Installation

## System Setup
Ensure that you have python installed, cmake, and a recent c++ compiler available.

## Clone Repos

1) Clone this repository somewhere
2) Enter the repository.
    3) Clone github.com/pwelke/HomSub.git
    1) Clone github.com/pwelke/graph-homomorphism-network.git


## Building Scala Part

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
- Run (in the virtual environment)
```
python experiments.py
```
- Note that there is currently a race condition with a temp file. Hence, you cannot run multiple experiments simultaneously on the project folder. A workaroud would be to copy the full project folder multiple times.






