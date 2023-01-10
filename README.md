# Expectation Complete Graph Representations

This repository contains the code to compute graph representations that are complete in expectation. If you use this code in your work or find it useful in any other way, please consider citing our paper:

Pascal Welke*, Maximilian Thiessen*, and Thomas Gärtner: 
[Expectation Complete Graph Representations Using Graph Homomorphisms.](https://openreview.net/forum?id=Zf-Mn6xzD2B)

[presented at [GLFrontiers@NeurIPS2022](https://glfrontiers.github.io/)] [presented at [LOG2022](https://logconference.org/)]

# Installation

## System Setup
Ensure that you have python installed, cmake, and a recent c++ compiler available.
Currently, java is also a dependency, but it is superfluous.

## Clone Repo

To run the code in this repository, clone it somewhere and initialize the git submodules
```
git clone git@github.com:pwelke/homcount.git
cd homcount
git submodule init
git submodule update
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
python setup.py install
```

# Compute Embeddings and Evaluate Results

- Download data from [here](https://drive.google.com/file/d/15w7UyqG_MjCqdRL2fA87m7-vanjddKNh/view?usp=sharing) and unzip it into `graph-homomorphism-network/data`.
- Run (in the virtual environment) `python experiments.py`, to only compute the embeddings of the selected datasets (if not already done) and save them in `graph-homomorphism-network/data/precompute`.
- Run (in the virtual environment) `python evaluation.py`, to compute a number of embeddings of the selected datasets (if not already done) and save them in `graph-homomorphism-network/data/precompute`. After that, run 10-fold cross validations for the MLP and SVM classifiers. 
- Note that there is currently a race condition with a temp file in . Hence, you cannot run multiple experiments simultaneously on the project folder. A workaroud would be to copy the full project folder multiple times.
- Currently, the average accuracies have to be manually collected from the output of evaluation.py.






