# nlu-cw
Natural Language Understanding coursework (spring 2018).

### Python Virtual Environment 
For this assignment you will be using Python along with a few open-source packages. These packages cannot be installed directly, so you will have to create a virtual environment. We are using virtual environments to make the installation of packages and retention of correct versions as simple as possible. For this assignment we are going to use Miniconda + Python 3.5.

Open a terminal on a DICE machine and follow these instructions. We are expecting you to enter these commands in one-by-one. Waiting for each command to complete will help catch any unexpected warnings and errors.
Note: You can skip step (1) and (2) if you already have Miniconda installed in your machine.

1. Open a terminal on DICE machine and type the following command:
```
$> wget https:repo.continuum.io/minicondaMiniconda3-latest-Linux-x86 64.sh 
$> bash Miniconda3-latest-Linux-x86 64.sh
```
2. Restart your terminal.
3. Create conda virtual environment:
```
$> conda create -n nlu python=3.5
```
4. Activate conda environment:
```
$> source activate nlu
```
5. Install packages that we need:
```
$> conda install numpy gensim pandas
```
