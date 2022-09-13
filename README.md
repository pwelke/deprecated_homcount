# Installation

## System Setup
Ensure that you have java installed, use java8 (!) and have scala and sbt installed.

```
apt-get install openjdk8-headless
apt-get install scala
```

To install [sbt](https://repo.scala-sbt.org/), you may 
```
echo "deb https://repo.scala-sbt.org/scalasbt/debian all main" | sudo tee /etc/apt/sources.list.d/sbt.list
echo "deb https://repo.scala-sbt.org/scalasbt/debian /" | sudo tee /etc/apt/sources.list.d/sbt_old.list
curl -sL "https://keyserver.ubuntu.com/pks/lookup?op=get&search=0x2EE0EA64E40A89B84B2DF73499E82A75642AC823" | sudo apt-key add
sudo apt-get update
sudo apt-get install sbt 
```

Set your default java and javac to version 8 (requires manual intervention)
```
sudo update-alternatives --config java
sudo update-alternatives --config javac
```

## Clone Repos

1) Clone this repository somewhere
2) Enter the repository.
    c) Clone github.com/pwelke/graph-homomorphism-network.git
    a) Clone github.com/maksim96/DISC.git


## Building Scala Part

To compile the scala part (DISC), run

## Python Setup

Create a virtual environment, using python 3.7 (!) and install dependencies

conda:
```
cd graph-homomorphism-network
conda create -n expectation_complete python==3.7
conda activate expectation_complete
pip install -r requirements_dev.txt
```

or via venv:
```
cd graph-homomorphism-network
python3.7 -m venv graph_homs_learning3-7
source ./graph_homs_learning3-7/bin/activate
pip install -r requirements_dev.txt
```



# Compute Embeddings

- Download data from [here](https://drive.google.com/file/d/15w7UyqG_MjCqdRL2fA87m7-vanjddKNh/view?usp=sharing) and unzip it into `graph-homomorphism-network/data`.
- set the parameter in `DISC/disc_local.properties` according to the number of cores of your machine
- run (in the virtual environment)
```
python experiments.py
```






